"""In-memory GramHelp security boundary, not a chatbot or auth provider.

Session must originate from trusted authentication middleware. The LLM may
propose tool arguments; it must never construct Session or call approve_ticket.
All amounts and identities below are fictional. No network access is used.
"""
from collections import defaultdict, deque
from dataclasses import dataclass
from html import escape
import secrets
import time


class Denied(ValueError):
    """A policy decision failed closed."""


@dataclass(frozen=True)
class Session:
    subject: str
    role: str


@dataclass(frozen=True)
class Ticket:
    title: str
    body: str


@dataclass(frozen=True)
class Proposal:
    id: str
    owner: str
    ticket: Ticket


@dataclass(frozen=True)
class Document:
    id: str
    text: str
    audience: str
    reviewed: bool


def render_output(text: str) -> str:
    """Escape all model text for an HTML text context (not JS/URL contexts)."""
    return escape(text, quote=True)


class Gateway:
    """Single-process mock services with enforcement outside model decisions."""
    def __init__(self, clock=time.monotonic, limit=30):
        self.clock = clock
        self.limit = limit
        self.principals = {'student-a': 'student', 'student-b': 'student', 'staff-a': 'staff'}
        self.balances = {'student-a': 1200, 'student-b': 750}
        self.tickets = []
        self.documents = {}
        self.proposals = {}
        self.approvals = {}
        self.requests = defaultdict(deque)
        self.audit = []

    def _record(self, action, outcome, reason):
        # No student identifier, balance, text, proposal ID, or approval secret.
        self.audit.append({'action': action, 'outcome': outcome, 'reason': reason})

    def _deny(self, action, reason):
        self._record(action, 'deny', reason)
        raise Denied(reason)

    def _enter(self, session, action):
        if (not isinstance(session, Session) or not isinstance(session.subject, str)
                or session.subject not in self.principals
                or self.principals[session.subject] != session.role):
            self._deny(action, 'invalid_session')
        now = self.clock()
        queue = self.requests[session.subject]
        while queue and queue[0] <= now - 60:
            queue.popleft()
        if len(queue) >= self.limit:
            self._deny(action, 'rate_limit')
        queue.append(now)

    def balance(self, session, target):
        action = 'balance.read'
        self._enter(session, action)
        if session.role != 'student' or target != session.subject:
            self._deny(action, 'subject_mismatch')
        self._record(action, 'allow', 'own_account')
        return self.balances[session.subject]

    def propose_ticket(self, session, ticket):
        action = 'ticket.propose'
        self._enter(session, action)
        if (not isinstance(ticket, Ticket) or not isinstance(ticket.title, str)
                or not isinstance(ticket.body, str) or not ticket.title.strip()
                or not ticket.body.strip() or len(ticket.title) > 120 or len(ticket.body) > 2000):
            self._deny(action, 'invalid_schema')
        p = Proposal(secrets.token_urlsafe(16), session.subject, ticket)
        self.proposals[p.id] = p
        self._record(action, 'allow', 'proposal_only')
        return p

    def _proposal(self, session, proposal, action):
        if (not isinstance(proposal, Proposal) or proposal.owner != session.subject
                or self.proposals.get(proposal.id) != proposal):
            self._deny(action, 'proposal_mismatch')

    def approve_ticket(self, session, proposal):
        """Trusted human-confirmation entry point; never expose as an LLM tool.

        A production UI must display these exact fields before invoking this.
        This local method simulates that separate human event.
        """
        action = 'ticket.approve'
        self._enter(session, action)
        self._proposal(session, proposal, action)
        token = secrets.token_urlsafe(32)
        self.approvals[token] = (proposal, self.clock() + 300)
        self._record(action, 'allow', 'explicit_approval')
        return token

    def execute_ticket(self, session, proposal, approval):
        action = 'ticket.execute'
        self._enter(session, action)
        self._proposal(session, proposal, action)
        record = self.approvals.get(approval)
        if record is None or record[0] != proposal or self.clock() >= record[1]:
            self._deny(action, 'approval_missing_mismatched_or_expired')
        # Single-use proposal and approval; no network side effects in this lab.
        del self.approvals[approval]
        del self.proposals[proposal.id]
        self.tickets.append({'owner': session.subject, 'ticket': proposal.ticket})
        self._record(action, 'allow', 'approved_creation')
        return len(self.tickets)

    def publish_document(self, session, document):
        action = 'document.publish'
        self._enter(session, action)
        if session.role != 'staff': self._deny(action, 'staff_only')
        if (not isinstance(document, Document) or document.reviewed is not True
                or document.audience not in {'public', 'staff'}
                or not isinstance(document.id, str) or not document.id.strip()
                or not isinstance(document.text, str) or not document.text.strip()
                or len(document.text) > 10000):
            self._deny(action, 'invalid_or_unreviewed_document')
        if document.id in self.documents: self._deny(action, 'duplicate_document')
        self.documents[document.id] = document
        self._record(action, 'allow', 'reviewed_publication')

    def retrieve(self, session):
        action = 'document.retrieve'
        self._enter(session, action)
        docs = [d for d in self.documents.values()
                if d.audience == 'public' or session.role == 'staff']
        self._record(action, 'allow', 'acl_filtered')
        return docs


class VulnerableGateway:
    """Deliberately unsafe comparison baseline; synthetic data only."""
    def __init__(self):
        self.balances = {'student-a': 1200, 'student-b': 750}
        self.tickets = []

    def balance(self, session, target):
        return self.balances[target]

    def execute_ticket(self, session, ticket):
        self.tickets.append(ticket)
        return len(self.tickets)

# GramHelp control lab

## Design and scope
Implement option 2 selected by the user: an executable, dependency-free Python control lab, synthetic data, threat model, editable data-flow diagram, reproducible evidence, and a Google Docs submission. This is a local simulation, not a deployed chatbot, PDF parser, embedding service, authentication provider, or LLM evaluation. Preserve Lab1 and master. All published commits must resolve to omariomari2 as author and committer.

## Implementation plan
- [ ] Model and document GramHelp's seven required components and trust boundaries; map eight threats to OWASP 2025; define residual risks and a red-team procedure.
- [ ] Write failing behavioral tests for balance isolation, ticket approval binding/replay/expiry, document publication and authorization, safe output, quotas, and audit redaction. Implement controls and vulnerable baselines. Run the full suite.
- [ ] Add synthetic document fixtures and a reproducible baseline/protected demonstration; save measured results with environment and scope limitations.
- [ ] Create a native Google Doc with a diagram and four-column threat table; read back, export and inspect the submission.
- [ ] Publish atomic commits on original-work, verifying identities, branch contents and preserved Lab1.

## Interfaces and checks
`gramhelp.py`: Session, Ticket, Document, Denied, Gateway; balances(session, target), propose_ticket(session, ticket), approve_ticket(session, proposal), execute_ticket(session, proposal, approval), publish_document(session, document), retrieve(session), render_output(text), audit events. `demo.py` consumes these public interfaces and emits results.json and results.md. Tests use real in-memory implementations and an injected clock.

## Review focus
Missing/unknown principals fail closed; approvals cannot transfer between users or payloads; expiry/replay do not create side effects; document approval does not imply prompt safety; quotas apply before actions and do not leak payloads to logs. No real student records, credentials or model requests.

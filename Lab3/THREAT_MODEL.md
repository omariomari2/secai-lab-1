# GramHelp threat model

Bright Omari Owusu � SecAI+ Lab 3 � October 28, 2026

## Scope, assets, and assumptions
GramHelp retrieves university policy documents, reads the authenticated student's balance, and opens help-desk tickets. Staff upload PDFs for automatic indexing in the scenario. The proposed secure design adds a quarantine/review gate before that automatic indexing. Assets are student financial privacy, accurate policy guidance, document integrity, ticket integrity, service availability, and service credentials.

The diagram is editable in [architecture.mmd](architecture.mmd); [architecture.png](architecture.png) is the submission figure. TB1 separates clients from university services; TB2 separates the application from a potentially external model provider; TB3 separates the chatbot from restricted internal APIs; TB4 separates uploaded content from the searchable index. Retrieved text remains untrusted even after review. Identity must come from authentication middleware, never a prompt or model-produced tool argument. Students may read only their own balances. Staff publishing privileges do not grant student financial access. The model receives neither service tokens nor approval secrets.

The prototype uses preconstructed sessions as a test seam, in-memory document retrieval rather than embeddings, and explicit human-event simulation rather than a confirmation web UI. Model hosting, malware/PDF scanning, university SSO, persistent storage, distributed rate limits, and real ticket/balance services are design requirements, not implemented integrations.

## Threat/control table

| Threat | OWASP ID (2025) | Control | Residual risk |
| --- | --- | --- | --- |
| T1. A policy PDF embeds instructions to read another student's balance or open unwanted tickets: indirect prompt injection. | LLM01:2025 Prompt Injection | Treat retrieved chunks as data; isolate them from instructions. Enforce subject-scoped balance access and exact-action ticket approval outside the LLM. | High: a reviewed or compromised document can still cause misleading answers or manipulate a user into approving an action. Delimiters and scanning do not eliminate injection. |
| T2. The LLM requests another student's balance or includes financial data in an unrelated response. | LLM02:2025 Sensitive Information Disclosure | Bind API subject to the authenticated session; use a read-only student-scoped credential. Minimize model context and redact audit payloads. | Medium: the current student's data could still leak through conversation context, model-provider retention, or a compromised session. |
| T3. A staff-account compromise publishes false policy content into the RAG corpus. | LLM04:2025 Data and Model Poisoning | Quarantine uploads; scan PDFs; require independent review, source/version metadata, and a rollback path. Prototype implements a review flag and prevents silent replacement. | Medium: authorized reviewers can accept plausible false policy. The prototype flag is not an independent review workflow or malware scanner. |
| T4. Model output contains active HTML or script that reaches a web page or ticket display. | LLM05:2025 Improper Output Handling | Render escaped text, validate ticket types/lengths, and never evaluate generated code. Apply context-specific escaping at every downstream UI sink. | Low to medium: HTML text escaping does not protect JavaScript, URL, or rich-text contexts; real ticket rendering remains to be tested. |
| T5. The chatbot creates unwanted tickets because it has excessive permissions or autonomy. | LLM06:2025 Excessive Agency | Separate read-only balance and create-only ticket identities; allowlist tools. Require a human approval bound to user and exact ticket, expiring after 300 seconds and consumed once. | Medium: users may approve deceptive contents; stolen sessions and concurrent execution need additional safeguards. |
| T6. Retrieval returns staff-only chunks to a student because vector metadata filtering is absent. | LLM08:2025 Vector and Embedding Weaknesses | Enforce ACL filtering before returning chunks; bind filtering to authenticated identity and preserve ACLs through indexing. | Medium: incorrect source labels, embedding leakage, or a misconfigured production index can defeat filtering. Prototype tests document-level filtering only. |
| T7. The chatbot invents a payment deadline or cites obsolete university policy. | LLM09:2025 Misinformation | Require current approved sources and citations; abstain when evidence is absent/conflicting; route financial disputes to staff. | High: plausible, cited but false guidance can survive review. No real LLM answer-quality evaluation is included. |
| T8. Repeated prompts, large inputs, or tool loops consume inference budget or flood ticketing. | LLM10:2025 Unbounded Consumption | Per-user quotas, input limits, bounded tool calls and tokens, provider cost caps, timeouts and alerting. Prototype enforces 30 gateway requests per rolling 60 seconds and bounded ticket/document text. | Medium: distributed attackers and expensive individual requests can bypass local counters; production needs shared limits and provider budgets. |

## Highest remaining risk and red-team test
The highest remaining risk is indirect prompt injection through an apparently approved policy document that changes advice or persuades a student to approve an unwanted ticket. Confidentiality and tool-action controls reduce impact, but do not establish that an answer is trustworthy. T7 is a related answer-integrity outcome of this attack path.

Test only a local/staging system with synthetic records. Index a benign policy alongside fixtures/injected-policy.txt, mark the fixture as approved to simulate review failure, and ask a normal balance-policy question. Include paraphrased and instruction-like variants in a later real-model evaluation. Inspect retrieved document IDs, citations, model answer, proposed tool calls, final side effects and sanitized policy decisions. An attack succeeds if another student's balance is returned, a ticket is created without exact approval, or the response presents injected instructions as authoritative policy. A useful answer citing the benign source is the positive control.

The deterministic lab supplies the malicious tool arguments directly. Expected results: other-student balance access is denied; an unapproved ticket is denied; exact approved creation works once; replay and changed payloads are denied. It deliberately confirms that an approved malicious document is retrievable. For a future LLM test, repeat each prompt with a fixed model/version/settings and record every response; do not report an attack-success rate until those trials actually run.

## Evidence and limits
Run `python -m unittest discover -s Lab3 -v` from the repository root, then `python Lab3/demo.py`. Unit tests verify both legitimate behavior and rejection paths. Demo evidence is saved in evidence/results.json and evidence/results.md, without real student data or secrets. These tests verify a single-process policy boundary; they do not prove prompt-injection resistance, SSO security, distributed atomicity, PDF scanner effectiveness, or safe model-provider handling.

## References
- Assignment: SecAI+ Lab 3, Threat-Model an AI Chatbot, Canvas assignment 641289.
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- OWASP Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- OWASP 2025 publication: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/

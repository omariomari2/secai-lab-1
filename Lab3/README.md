# Lab 3: Threat-model an AI chatbot

This original coursework models GramHelp, a hypothetical student-services RAG chatbot. It pairs a threat model with an executable Python security boundary and a deliberately vulnerable comparison baseline. All identities, balances and policies are synthetic.

## Run
Python 3.10 or later; no third-party packages, API keys or network access required.

```sh
python -m unittest discover -s Lab3 -v
python Lab3/demo.py
```

Run from the repository root. See [measured results](evidence/results.md), [threat model](THREAT_MODEL.md), [editable diagram](architecture.mmd), and [diagram image](architecture.png). `gramhelp.py` implements controls; `test_gramhelp.py` checks legitimate and adversarial paths; `fixtures/` contains synthetic source documents. `PLAN.md` records scope and implementation progress.

## What the implementation demonstrates
- Authenticated-subject checks prevent a student's balance request from targeting another student.
- Ticket proposals cause no creation until a separate human-confirmation event grants exact-payload approval. Approvals are user-bound, expire in 300 seconds, and cannot be replayed.
- Staff role, explicit review and known document scopes gate publication; ACLs filter retrieval.
- Model output is escaped for an HTML text sink; action schemas and local quotas bound misuse.
- Audit records contain actions, outcomes and reason codes, excluding text, balances and approval secrets.

## Honest boundaries
There is no LLM, embedding index, PDF parser, live API or authentication server. Tests supply adversarial tool calls directly. Reviewed malicious text remains retrievable by design: a review flag does not detect prompt injection. `approve_ticket` must remain inaccessible to the model; a production UI must separately authenticate the human and display exact contents. Session objects are trusted middleware outputs, not browser/model inputs. The gateway is single-process and not safe for concurrent production use without transactional persistence. Real output sinks, provider budgets, prompt behavior and policy accuracy remain untested.

The [submission is maintained in Google Docs](https://docs.google.com/document/d/1bS9dOAbAj8PoKHydCnXIOeG6lfAIMDQNfWzDU0Dty-Q/edit). A visually checked four-page export is in [submission.pdf](submission.pdf). No real university policy or student information is included.

The optional `render_architecture.py` authoring utility requires Pillow and Arial fonts at the Windows paths in the script; the checked-in PNG and Mermaid source can be used without it. Runtime and tests remain standard-library only.

# SecAI+ CertMaster Perform

Hands-on progress and evidence from CompTIA SecAI+ CertMaster Perform V1.

## Progress

| Item | Status | Verified score | Evidence |
| --- | --- | --- | --- |
| 1.1.11 Explore the SecAI+ Lab Environment | Previously completed; observed on dashboard | 100% | Dashboard observation, November 7, 2026 |
| 1.1.12 Lesson Review | Previously completed; observed on dashboard | 90% | Dashboard observation, November 7, 2026 |
| 1.2.8 Prompt Engineering | Completed this session | 6/6 (100%) | [Score screenshot](evidence/activity-1.2.8-score.png) |
| 1.2.9 Perform Prompt Engineering and Bias Detection | In progress | Not yet scored | [Lab setup](evidence/lab-start.png) |

Course progress was 6% at the start of the session. Videos are being skipped as requested; this does not imply that the platform marks them complete.

## Activity 1.2.8

Completed all six stages in the coach's sequence: zero-shot, system/role, role plus context, template/format, one-shot, and multi-shot. The platform awarded one point for each stage.

Prompts progressively added a SOC analyst role, healthcare incident context, an explicit output schema, and input/output examples. They required the model to distinguish observed evidence from hypotheses and preserve original log details.

An important observation: the coach's sample outputs sometimes introduced hosts, IPs, timestamps, and events absent from the supplied logs. A positive prompt-design score does not establish factual accuracy of those generated examples. Validate AI security conclusions against the source logs.

## Evidence policy

Screenshots are captured from the actual platform. Setup images show work in progress; only score reports support completion claims. No access tokens, authenticated iframe URLs, or account credentials are included in notes.

Updates are edited locally and committed as coherent batches on `original-work`.

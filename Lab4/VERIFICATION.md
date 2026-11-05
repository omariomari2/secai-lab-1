# Claim verification

Verdicts evaluate the atomic excerpt, not whether an attack occurred. Correct means supported by supplied evidence or the cited official source; unsupported means unproved hypothesis or judgment, even where reasonable. No incorrect factual claim was identified. Recommendations are proposals and receive no completed-action verdict. L1–L6 refer to the six source lines in order. Checked November 4, 2026 (America/Chicago).

## Claims 1–9

| ID / claim | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| V01  /  Three SSH password failures; root twice, admin once. | Correct | L1–L3 | Exactly these three failed-password records occur. |
| V02  /  Failures came from 185.220.101.4. | Correct | L1–L3 | The source field is identical in all three records. |
| V03  /  Failures occurred over five seconds. | Correct | L1, L3 | 02:13:49 minus 02:13:44 = 5 seconds. |
| V04  /  Thirteen seconds later SSH accepted a password for jdoe. | Correct | L3–L4 | 02:14:02 minus 02:13:49 = 13 seconds; accepted password is explicit. |
| V05  /  jdoe login came from that same address. | Correct | L1–L4 | L4 source is 185.220.101.4; identity of the person is not established. |
| V06  /  At 02:14:40 sudo recorded jdoe requesting /usr/bin/wget as root. | Correct | L5 | USER=root, account jdoe and COMMAND are explicit. No process outcome appears. |
| V07  /  Command intended retrieval of http://203.0.113.50/x.sh. | Correct | L5; MITRE T1105 | The command contains wget and this URL; intention does not prove a network request completed. |
| V08  /  Line does not establish successful retrieval, contents, or script execution. | Correct | L5; full L1–L6 | No output, exit status, file content or execution record is provided. |
| V09  /  At 09:02:11 SSH accepted public-key authentication for mlee from 10.0.4.22. | Correct | L6 | All fields match the record. |

## Claims 10–18

| ID / claim | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| V10  /  10.0.4.22 is a private address. | Correct | RFC 1918 §3; L6 | 10.0.4.22 falls within 10.0.0.0–10.255.255.255. Private addressing does not establish authorization. |
| V11  /  No evidence links mlee login to earlier sequence or establishes authorization. | Correct | L1–L6 | Different account/source/time; no correlation or approval records supplied. Absence of evidence is not proof of independence. |
| V12  /  Early sequence is consistent with password guessing. | Unsupported | L1–L3; T1110.001 | Reasonable attack hypothesis. Failures alone do not prove intent, password values, automation, or guessing. |
| V13  /  Sequence is consistent with use of a valid account. | Correct | L4; T1078 | L4 supports accepted authentication for jdoe. This observation does not assert adversarial use. |
| V13a  /  Separate hypothesis: Adversarial use of jdoe’s accepted credentials occurred. | Unsupported | L4; T1078 | Actual account abuse is unproved; authorization and actor identity are unknown. |
| V14  /  Sequence is consistent with an attempted privileged file download. | Correct | L5 | A root-context wget command is recorded. This is a command-level attempt, not proof of process/network success. |
| V15  /  Unauthorized access is plausible. | Unsupported | L1–L5 | Reasonable hypothesis from clustered failures, acceptance, and privileged command; no authorization evidence. |
| V16  /  Authorization, credential theft, and compromise are unconfirmed. | Correct | Full L1–L6 | No approval records, credential acquisition, or independent compromise evidence supplied. |
| V17  /  Three failures do not establish a sustained brute-force campaign. | Correct | L1–L3 | The evidence contains only three failures across five seconds; no sustained activity is demonstrated. |
| V18  /  A .sh filename does not prove malicious content. | Correct | L5 | Only a URL filename is visible; contents are absent. |

## Claims 19–27

| ID / claim | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| V19  /  High triage priority, provisional. | Unsupported | L1–L5 | Analyst risk judgment, not measured incident severity. Urgent review is reasonable given accepted credentials and root-context command; authorization and outcome remain unknown. |
| V20  /  Successful password login immediately follows failures from same source. | Correct | L1–L4 | Next supplied event is L4, 13 seconds after last failure; immediately means sequence proximity, not zero delay. |
| V21  /  Login is followed by a root-context download command. | Correct | L4–L5 | Command occurs 38 seconds after accepted login. Session linkage is plausible but not proven by a shared session identifier. |
| V22  /  Potential impact is substantial if unauthorized. | Unsupported | L5 | Risk assessment: root-context activity could affect the host; neither unauthorized use nor actual impact is established. |
| V23  /  Actual download success, execution, persistence and data theft are not shown. | Correct | Full L1–L6 | No corresponding outcome, execution, persistence or exfiltration evidence appears. |
| V24  /  T1110.001 — Password Guessing exists with this title. | Correct | Official MITRE T1110.001 | Canonical ID and sub-technique name verified; see ATT&CK table. |
| V25  /  T1110.001 tentatively explains failures; intent and scale unconfirmed. | Unsupported | L1–L3; official MITRE | Conditional hypothesis consistent with guessing; authentication failures alone are insufficient for confirmation. |
| V26  /  T1078 — Valid Accounts exists with this title. | Correct | Official MITRE T1078 | Canonical ID and technique name verified. |
| V27  /  T1078 applies if accepted credentials were used adversarially; acceptance alone is not abuse. | Correct | L4; official MITRE | The official T1078 description requires adversarial account abuse; the excerpt correctly makes applicability conditional and does not equate acceptance with abuse. |
| V27a  /  Separate hypothesis: T1078 Valid Accounts occurred as adversarial account abuse. | Unsupported | L4; official MITRE T1078 | Authentication is accepted, but adversarial credential use and account type are unverified. |

## Claims 28–33

| ID / claim | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| V28  /  T1548.003 — Sudo and Sudo Caching exists with this title. | Correct | Official MITRE T1548.003 | Canonical ID and sub-technique name verified. |
| V29  /  Root-context sudo is recorded; adversarial privilege escalation is a hypothesis. | Correct | L5; official MITRE | L5 records sudo with USER=root. Calling adversarial escalation a hypothesis correctly states the evidence limit; no caching or sudoers abuse is shown. |
| V29a  /  Separate hypothesis: Adversarial privilege escalation under T1548.003 occurred. | Unsupported | L5; official MITRE T1548.003 | Root-context sudo use alone does not establish malicious elevation, caching or sudoers abuse. |
| V30  /  T1105 — Ingress Tool Transfer exists with this title. | Correct | Official MITRE T1105 | Canonical ID and technique name verified. |
| V31  /  wget suggests attempted inbound transfer if adversarial; completion unproven. | Correct | L5; official MITRE | The command supports an attempted inbound-transfer candidate. The excerpt correctly conditions adversarial applicability and states completion is unproved. |
| V31a  /  Separate hypothesis: Adversarial Ingress Tool Transfer under T1105 occurred. | Unsupported | L5; official MITRE T1105 | Command recorded; malicious purpose, completed transfer and compromised environment remain unverified. |
| V32  /  T1021.004 — SSH exists with this title. | Correct | Official MITRE T1021.004 | Canonical ID and sub-technique name verified. |
| V33  /  SSH is observed; adversarial remote-service use is conditional; lateral movement is not established. | Correct | L1–L4, L6; official MITRE | SSH is recorded in L1–L4 and L6. The excerpt correctly leaves adversarial use conditional and lateral movement unestablished; MITRE lists the Lateral Movement tactic. |
| V33a  /  Separate hypothesis: Adversarial SSH lateral movement under T1021.004 occurred. | Unsupported | L1–L4, L6; official MITRE T1021.004 | No adversarial movement between hosts or linked internal pivot is demonstrated. Protocol observation alone is insufficient. |

## Recommendations: scope only

| ID | Recommendation excerpt | Classification | Scope / limitation |
| --- | --- | --- | --- |
| R1 | Preserve authentication, sudo, process, network and file evidence; establish host/timezone; correlate surrounding events. | Proposal | L1–L6 supply only a narrow excerpt. No preservation or correlation is claimed completed. |
| R2 | Verify jdoe login/command with owner and approved activity records; independently validate mlee source/key. | Proposal | Authorization and relationship are unknown. No owner contact or validation is claimed completed. |
| R3 | Check wget outcome, destination file/hash/contents/ownership, subsequent process activity, other sessions and privilege changes without executing file. | Proposal | L5 gives no outcome or file evidence. No retrieval, execution, inspection or investigation is claimed completed. |
| R4 | If unauthorized activity is confirmed or active risk requires containment, isolate host, terminate suspicious sessions and revoke affected credentials through response procedures. | Conditional proposal | Containment is not a completed action and does not assert confirmed compromise. Ticket below lists exactly the first three actions; this is a later conditional option from the frozen response. |

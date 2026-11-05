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
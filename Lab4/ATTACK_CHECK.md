# MITRE ATT&CK check

All five IDs and canonical names were checked on the official MITRE ATT&CK pages on November 4, 2026 (America/Chicago). Existence is verified; adversarial applicability is conditional. Parent-prefixed page titles are shown separately from canonical technique names. These are hypotheses, not a confirmed attack chain.

| ID / canonical name | Official page title / URL | Existence vs appropriateness; supporting lines |
| --- | --- | --- |
| T1110.001 — Password Guessing | Brute Force: Password Guessing<br>https://attack.mitre.org/techniques/T1110/001/ | L1–L3: Exists; tentative. Three failures could reflect guessing, but intent, password values and scale unknown. |
| T1078 — Valid Accounts | Valid Accounts<br>https://attack.mitre.org/techniques/T1078/ | L4: Exists; conditional on adversarial credential use. Accepted login alone is insufficient; account type unknown. |
| T1548.003 — Sudo and Sudo Caching | Abuse Elevation Control Mechanism: Sudo and Sudo Caching<br>https://attack.mitre.org/techniques/T1548/003/ | L5: Exists; conditional on adversarial elevation. Sudo root context recorded; caching, sudoers abuse and unauthorized escalation unproven. |
| T1105 — Ingress Tool Transfer | Ingress Tool Transfer<br>https://attack.mitre.org/techniques/T1105/ | L5: Exists; attempted-transfer hypothesis only. MITRE describes adversarial inbound files and names wget. Completion, content and compromised environment unproven. |
| T1021.004 — SSH | Remote Services: SSH<br>https://attack.mitre.org/techniques/T1021/004/ | L1–L4, L6: Exists; weak/conditional candidate. MITRE tactic is Lateral Movement. SSH alone does not demonstrate adversarial movement between hosts; do not report confirmed lateral movement. |

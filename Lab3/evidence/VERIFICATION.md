# Verification record

Executed with Python 3.13 on Windows. All data is synthetic.

- `python -m unittest discover -s Lab3 -v`: 19 tests passed.
- `python Lab3/demo.py`: 11 of 11 expected outcomes reproduced.
- The baseline permits cross-student balance lookup and ticket creation without approval; the protected gateway denies those same requests.
- Reviewed malicious content remains retrievable; no claim of semantic injection detection or model robustness is made.
- Independent code review identified a null-role/unknown-principal comparison bug. A regression test reproduced the bypass before the membership check was corrected. The full suite passed afterward.
- Google Docs readback confirmed a native diagram image and two native four-column tables covering eight threats. The exported PDF was rendered and all pages visually inspected for legibility and intact tables.

Limits: no real LLM, embedding model, PDF scanner, SSO, remote services, concurrent workers, provider cost budget, or production deployment was exercised. In-memory quotas reset on restart. Human approval is a separately invoked simulation method, not a deployed confirmation interface. The test session constructor assumes trusted authentication middleware.

# Incident 002: Potential LSASS Credential Dumping

**Detection ID:** T1003.001  
**Tool/Source:** Splunk  
**Analyst:** Giovanna Lorenzetti  
**Date:** 2025-07-16

---

## Summary
Splunk alert triggered for suspicious access to `lsass.exe` using access rights commonly associated with credential dumping.

---

## Observables
- **Process:** procmon.exe
- **Target:** lsass.exe
- **Granted Access:** 0x1010
- **User:** User01
- **Time:** 2025-07-15T13:00:00Z

---

## Enrichment
- VirusTotal result: clean
- No unusual behavior in adjacent process tree

---

## Investigation
- Verified source binary signed and used by approved monitoring tool
- Process launched during known testing window by IT admin

---

## Outcome
✅ **Closed as expected behavior** — part of internal diagnostics by administrator.

---

## Recommendations
- Suppress alert for this binary in future
- Confirm whitelist policy with detection engineering team

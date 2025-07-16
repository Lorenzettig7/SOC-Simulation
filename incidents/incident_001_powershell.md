# Incident 001: Suspicious PowerShell Execution

**Detection ID:** T1059.001  
**Tool/Source:** Splunk  
**Analyst:** Giovanna Lorenzetti  
**Date:** 2025-07-16

---

## Summary
An alert triggered for base64-encoded PowerShell execution, often associated with obfuscation or malicious script activity.

---

## Observables
- **Process:** powershell.exe
- **Command Line:** powershell -enc aQBmACgAIAA...
- **User:** User01
- **Host:** HostA
- **Time:** 2025-07-15T12:45:00Z

---

## Enrichment
- VirusTotal returned 1/72 detections for IP: 8.8.8.8  
- No matches on base64-decoded script

---

## Investigation
- Parent process: `explorer.exe`
- User confirmed execution of internal automation script
- Decoded PowerShell content matched expected behavior

---

## Outcome
✅ **Closed as false positive** — script was part of scheduled automation with IT approval.

---

## Recommendations
- Add hash to allow list
- Consider excluding automation context from alert rule

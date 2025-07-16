# Incident 003: AWS Root Console Login

**Detection ID:** T1078  
**Tool/Source:** CloudTrail / Splunk  
**Analyst:** Giovanna Lorenzetti  
**Date:** 2025-07-16

---

## Summary
CloudTrail detected a login to the AWS root account via the web console from a foreign IP address with MFA disabled.

---

## Observables
- **User:** Root
- **IP:** 202.54.1.1
- **Region:** us-east-1
- **Time:** 2025-07-16T18:00:00Z
- **MFA:** No

---

## Investigation
- IP traced to Asia-Pacific region — unusual for this account
- No documentation or tickets related to this login
- No API activity followed — likely just console access

---

## Outcome
🚩 **Escalated to Security Engineering** — pending credential rotation and potential forensic review.

---

## Recommendations
- Enforce MFA on root
- Rotate all associated IAM keys
- Alert team leads for immediate review

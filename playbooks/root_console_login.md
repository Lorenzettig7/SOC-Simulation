# Triage Playbook: AWS Root Console Login

## MITRE ATT&CK ID
- T1078 – Valid Accounts

## Detection Logic
Triggers when the AWS root user logs into the management console.

## Sample SPL Query
```spl
index=main sourcetype=aws:cloudtrail eventName="ConsoleLogin" userIdentity.type="Root"
```

## Triage Steps
1. **Verify Login Context**
   - Confirm if this was expected (e.g. emergency maintenance)
   - Check timestamp and source IP geolocation

2. **Review MFA Status**
   - Was MFA enabled? (Should always be on for root)

3. **Search for Follow-Up Activity**
   - API calls after login
   - IAM changes, credential updates, billing modifications

## Escalation Guidance
🚩 Escalate if:
- MFA was not used
- Login was outside of standard IP/geolocation range
- No approved justification

✅ Close if:
- Confirmed admin action with documented purpose

## Suggested Response
- Alert SecOps
- Rotate root credentials
- Audit CloudTrail logs

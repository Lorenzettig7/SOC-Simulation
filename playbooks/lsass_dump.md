# Triage Playbook: LSASS Memory Access (Credential Dumping)

## MITRE ATT&CK ID
- T1003.001 – OS Credential Dumping: LSASS Memory

## Detection Logic
This alert detects when a process attempts to access lsass.exe with suspicious access rights.

## Sample SPL Query
```spl
index=main sourcetype=_json TargetImage="*lsass.exe" (GrantedAccess="0x1010" OR GrantedAccess="0x1410")
```

## Triage Steps
1. **Confirm the Access**
   - Identify the source process: is it legitimate (e.g., antivirus)?
   - Check the user and host context

2. **Investigate the Source**
   - Look for known dumping tools: mimikatz, procdump, etc.
   - Use hashes or command lines to search VirusTotal or hybrid-analysis

3. **Check for Follow-up Activity**
   - Lateral movement?
   - Use of dumped credentials?
   - RDP or SMB access?

## Escalation Guidance
🚩 Escalate if:
- Process is unknown or unsigned
- Command line or binary resembles mimikatz/procdump
- Unusual admin context

✅ Close if:
- Activity is from trusted EDR, AV, or backup agent
- Logs match documented routine scanning

## Suggested Response
- Capture memory + analyze binary
- Rotate affected credentials
- Monitor for lateral movement

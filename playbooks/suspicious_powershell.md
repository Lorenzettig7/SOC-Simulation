# Triage Playbook: Suspicious PowerShell Command Execution

## MITRE ATT&CK ID
- T1059.001 – Command and Scripting Interpreter: PowerShell

## Detection Logic
This alert triggers when PowerShell is launched with base64-encoded commands, which may indicate obfuscated or malicious behavior.

## Sample SPL Query
```spl
index=main sourcetype=_json Image="*powershell.exe" CommandLine="*-enc*" OR CommandLine="*FromBase64String*"
```

## Triage Steps
1. **Validate the Event**
   - Confirm it's a real PowerShell execution event
   - Check user context (administrator? system?)

2. **Decode the Command**
   - Extract the base64 string and decode it using:
     ```bash
     echo "<base64>" | base64 -d
     ```
   - Look for signs of malware, recon, or lateral movement

3. **Review Context**
   - What parent process launched PowerShell? (`explorer.exe`, `cmd.exe`, `wscript.exe`)
   - Is the user known and expected to use scripting?

4. **Search for Related Activity**
   - Lateral movement?
   - Credential access?
   - Network connections?

## Escalation Guidance
- 🚩 Escalate if:
  - Decoded script contains obfuscated commands or payloads
  - PowerShell launched by `wscript.exe`, `Excel`, or suspicious processes
  - User was not expected to run scripts

- ✅ Close if:
  - Decoded content is legitimate
  - Action matches normal behavior (e.g., IT automation with audit trail)

## Suggested Response
- Capture memory and process tree
- Notify user and disable the account if suspicious
- Block command via AppLocker or Defender policies

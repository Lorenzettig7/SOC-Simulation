# SOC Analyst Detection and Response Platform

## Overview
This project simulates a real-world Tier 2 SOC analyst workflow, including:
- Log ingestion (Sysmon, CloudTrail)
- Detection engineering (Sigma + SPL)
- Threat intelligence enrichment (VirusTotal, AbuseIPDB)
- MITRE ATT&CK alignment
- Triage playbooks and incident response documentation

## Folder Structure
- `logs/`: Sample ingested logs
- `enrichment/`: Python scripts for threat intel enrichment
- `sigma-rules/`: Sigma rules (base and Falcon-style)
- `splunk-queries/`: SPL queries for detection
- `playbooks/`: Triage and response guides
- `mitre_mapping/`: ATT&CK Navigator layer files
- `incidents/`: Sample incident summaries
- `cloud-logs/`: Simulated AWS CloudTrail events
- `detection_pipeline_diagram.png`: Visual diagram of the detection pipeline

# AEGIS-9 Certification Overview

This document summarizes our AEGIS-9 certification: what the standard covers, the level we hold, and how the assessment cycle works.

## What is AEGIS-9?

AEGIS-9 (Assurance, Evidence, Governance & Infrastructure Security standard, revision 9) is an independent security assurance framework administered by the **Meridian Assurance Consortium (MAC)**. It evaluates an organization's security posture across five control families and assigns a tier rating from Bronze to Falcon.

## Our Certification Status

- **Tier achieved: Falcon** — the highest of the four AEGIS-9 tiers (Bronze, Silver, Gold, Falcon).
- **Certificate ID: AEG-2025-7741**, issued by the Meridian Assurance Consortium.
- **Assessment window: 14 months**, with the current certificate valid until **September 2027**.
- Assessed by Meridian-accredited lead auditor firm **Castellan & Gray LLP**.

## The Five Control Families

### CF-1: Identity Fortification

All production access requires hardware-token MFA and is brokered through a central identity plane. AEGIS-9 requires demonstrating zero standing administrative privileges; we operate just-in-time elevation with a maximum grant of 4 hours.

### CF-2: Evidence Continuity

Control evidence must be machine-collected, timestamped, and immutable. Our compliance platform snapshots evidence every 6 hours into write-once storage with a 7-year retention period, exceeding the AEGIS-9 minimum of 5 years.

### CF-3: Change Provenance

Every production change must be traceable to a reviewed and approved request. We satisfy this through protected branches, mandatory independent review, and signed commits across all release repositories.

### CF-4: Resilience Demonstration

AEGIS-9 Falcon tier requires a live failover demonstration during the assessment, not just documentation. Our most recent demonstration achieved full regional failover in **8 minutes**, well under the Falcon threshold of 30 minutes.

### CF-5: Disclosure Readiness

Certified organizations must publish a vulnerability disclosure channel and triage external reports within 48 hours. Our median triage time over the last assessment window was 9 hours.

## Renewal Cycle

The certification renews on a 14-month cycle with a mid-cycle checkpoint at month 7. Failing the checkpoint downgrades the tier by one level until remediated; we have passed every checkpoint since first certification.

## Requesting Proof of Certification

The AEGIS-9 certificate and the Castellan & Gray assessment letter are available to customers under NDA through the trust portal.

# SOC 2 Compliance Overview

This document summarizes our SOC 2 program: what is in scope, the controls we operate, and how the audit cycle works.

## Report Type and Cadence

We maintain a **SOC 2 Type II** report covering the Security, Availability, and Confidentiality trust service criteria. The observation window is twelve months, and a new report is issued annually by an independent AICPA-accredited audit firm. Bridge letters are available on request for the gap between the report date and the current date.

## Scope

The report covers the production environment serving customer workloads, including the application, its supporting cloud infrastructure, CI/CD pipeline, and the corporate identity provider. Development and staging environments that never hold customer data are out of scope.

## Key Controls

### Access Control

- All production access requires single sign-on with hardware-backed MFA; password-only access is disabled everywhere.
- Access follows least privilege and is granted through role-based groups, never to individuals directly.
- Quarterly access reviews are performed for every production system; review evidence is retained with ticket references.
- Access is revoked within one business day of personnel offboarding, verified by an automated deprovisioning check.

### Change Management

- Every production change ships through a pull request with at least one independent reviewer and passing automated tests.
- Direct pushes to release branches are blocked by branch protection.
- Infrastructure changes go through the same review pipeline as application code, using infrastructure-as-code.

### Encryption

- Customer data is encrypted in transit with TLS 1.2 or higher and at rest with AES-256.
- Encryption keys are managed by the cloud provider's key management service with automatic annual rotation; key material is never handled manually.

### Availability and Resilience

- Production runs across multiple availability zones with automated failover.
- Backups run daily, are encrypted, and are restore-tested quarterly. The recovery point objective is 24 hours and the recovery time objective is 8 hours.

### Vendor Management

- Subprocessors are reviewed before onboarding and re-assessed annually against their own SOC 2 or ISO 27001 reports.
- The current subprocessor list is published and customers are notified of additions in advance.

### Incident Response

- A documented incident response plan defines severity levels, on-call escalation, and communication timelines.
- Customers are notified of confirmed incidents affecting their data without undue delay, and no later than 72 hours after confirmation.
- Tabletop exercises are run twice a year and findings feed back into the plan.

## Personnel Security

- Background checks are completed for all employees prior to start, where permitted by local law.
- Security awareness training is required at onboarding and annually thereafter; completion is tracked and enforced.
- All employees sign confidentiality agreements as a condition of employment.

## Continuous Monitoring

Control health is monitored continuously through an automated compliance platform that ingests evidence from the cloud provider, identity provider, and source control. Drift from the control baseline opens a ticket automatically and is triaged within one business day.

## Requesting the Report

The full SOC 2 Type II report is available to customers and qualified prospects under NDA through the trust portal.

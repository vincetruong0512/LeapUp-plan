---
type: srs-flows
feature: email-notifications
updated: 2026-11-22
---

# E-mail Notifications — Flows

## Flow: Notify project members by e-mail (Sequence)

**Trigger**: New video version, comment or approval saved in a project.
**Related UC**: [UC-email-notifications-01](../usecases/uc-notify-project-members-by-email.md)
**Related FR**: FR-email-notifications-001, FR-email-notifications-002, FR-email-notifications-003, FR-email-notifications-004, FR-email-notifications-005
**Related E**: E-email-notifications-001, E-email-notifications-002

```mermaid
sequenceDiagram
    actor Member as Project member
    participant Portal
    participant Mail as E-mail service
    Portal->>Portal: New video version, comment or approval saved
    Portal->>Portal: Select project members to notify (recipients TBD)
    alt Member has an e-mail address
        Portal->>Mail: Send e-mail about the event (content TBD)
        alt Accepted
            Mail-->>Member: E-mail delivered
        else Rejected
            Mail-->>Portal: Failure - E-email-notifications-001
            Note over Portal: Event stays saved, failure handling TBD
        end
    else No e-mail address
        Portal->>Portal: Skip recipient - E-email-notifications-002
    end
```

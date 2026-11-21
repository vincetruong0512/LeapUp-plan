# Use Case: UC-email-notifications-01 Notify project members by e-mail

> Scope: Leap Up Client Project Portal — email-notifications · Level: sea (user goal)

## Primary Actor

Client or Leap Up member (recipient)

## Trigger

In a project, a new video version is added, a comment is added, or an approval is recorded (quote P2 #4).

## Preconditions

- The recipient is a member of the project.
- The recipient's account has an e-mail address (FR-email-notifications-005).

## Guarantees

- **Minimal Guarantee:** The triggering video, comment or approval stays saved whatever happens to the e-mail; members of other projects receive nothing.
- **Success Guarantee:** Each recipient with an e-mail address has received an e-mail about the event.

## Main Success Scenario

1. A new video version, comment or approval is saved in a project.
2. Portal selects the project members to notify (recipients per trigger TBD).
3. Portal sends the e-mail through the e-mail service (content TBD).
4. The e-mail service accepts the message; the recipient receives it.

## Extensions

**2a. A recipient has no e-mail address:**
- 2a1. Portal skips that recipient (E-email-notifications-002).
- 2a2. Continue with the next recipient.

**3a. The e-mail service rejects the message:**
- 3a1. E-email-notifications-001; the event itself stays saved.
- 3a2. Failure handling TBD.

## Related Requirements

- FR: [FR-email-notifications-001](../srs/email-notifications-spec.md#3-functional-requirements-fr), [FR-email-notifications-002](../srs/email-notifications-spec.md#3-functional-requirements-fr), [FR-email-notifications-003](../srs/email-notifications-spec.md#3-functional-requirements-fr), [FR-email-notifications-004](../srs/email-notifications-spec.md#3-functional-requirements-fr), [FR-email-notifications-005](../srs/email-notifications-spec.md#3-functional-requirements-fr)
- BR: BR-email-notifications-001, BR-email-notifications-002
- Errors: E-email-notifications-001, E-email-notifications-002 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-002, US-003 · Diagram: [Notify project members by e-mail (Sequence)](../srs/email-notifications-flows.md)

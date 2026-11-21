# Use Case: UC-production-timeline-01 Follow the production timeline

> Scope: Leap Up Client Project Portal — production-timeline · Level: sea (user goal)

## Primary Actor

Client

## Trigger

The client wants to know where the production stands.

## Preconditions

- The client is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** Only members of the project see its timeline (FR-production-timeline-009).
- **Success Guarantee:** The client has seen the current stage, the date ranges and the milestones with owner, due date and status.

## Main Success Scenario

1. Client opens the project's Proposal / Production Timeline (entry TBD).
2. Portal shows the header and PRODUCTION STAGES: five cards with number, status, stage name and date range.
3. Portal shows Milestones with MILESTONE, OWNER, DUE, STATUS.

## Extensions

**3a. The project has no milestones:**
- 3a1. Portal shows an empty table (E-production-timeline-001).
- 3a2. Use case ends.

## Related Requirements

- FR: [FR-production-timeline-001](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-002](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-003](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-004](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-005](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-009](../srs/production-timeline-spec.md#3-functional-requirements-fr)
- BR: BR-production-timeline-001, BR-production-timeline-002
- Errors: E-production-timeline-001 (wording in the spec Error Matrix — TBD)
- Stories: US-001 · Diagram: [Follow the production timeline (Sequence)](../srs/production-timeline-flows.md)

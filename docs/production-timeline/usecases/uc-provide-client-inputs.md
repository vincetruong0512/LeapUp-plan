# Use Case: UC-production-timeline-03 Provide missing client inputs (OPEN C6)

> Scope: Leap Up Client Project Portal — production-timeline · Level: sea (user goal)

## Primary Actor

Client

## Trigger

An input the production needs is shown as Missing.

## Preconditions

- The client is signed in and is a member of the project.
- OPEN C6: Client Inputs is on the board but not in the quote.

## Guarantees

- **Minimal Guarantee:** An item stays "Missing" if its upload fails.
- **Success Guarantee:** The uploaded item shows "Received".

## Main Success Scenario

1. Client opens the timeline.
2. Portal shows Client Inputs with Received or Missing per item and the FEEDBACK RULE box.
3. Client uses "Upload inputs" for a Missing item.
4. Portal stores the input.
5. Portal shows the item as "Received".

## Extensions

**4a. The upload fails:**
- 4a1. Portal shows E-production-timeline-002; the item stays Missing.
- 4a2. Resume at step 3.

## Related Requirements

- FR: [FR-production-timeline-007](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-008](../srs/production-timeline-spec.md#3-functional-requirements-fr)
- BR: —
- Errors: E-production-timeline-002 (wording in the spec Error Matrix — TBD)
- Stories: US-003 · Diagram: [Provide missing client inputs (OPEN C6) (Activity)](../srs/production-timeline-flows.md)

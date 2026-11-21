# Use Case: UC-storyboard-review-02 Approve and lock the storyboard (OUT)

> Scope: Leap Up Client Project Portal — storyboard-review · Level: sea (user goal)

## Primary Actor

Client

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Leap Up | Production starts only on an approved, locked script, shots and VO (L479) |

## Trigger

The client has reviewed the frames and is ready to approve.

## Preconditions

- The client is signed in and is a member of the project.
- OUT: change request needed.

## Guarantees

- **Minimal Guarantee:** Nothing is approved or locked when the user may not approve or frames are not settled (rule TBD).
- **Success Guarantee:** The version is approved with who and when recorded; script, shots and VO are locked; any later change starts a new revision.

## Main Success Scenario

1. Client presses "Approve storyboard".
2. Portal checks the user may approve (C4).
3. Portal checks the frames are settled (rule TBD).
4. Portal approves the version and records who and when.
5. Portal locks script, shots and VO.

## Extensions

**2a. The user may not approve:**
- 2a1. Portal approves nothing and shows E-storyboard-review-004.
- 2a2. Use case ends.

**3a. Frames are not settled (rule TBD):**
- 3a1. Portal approves nothing and shows E-storyboard-review-001.
- 3a2. Client returns to the frames (use case "Review storyboard shots").

***a. A change is needed after the lock:**
- *a1. Portal does not change the locked version (E-storyboard-review-003).
- *a2. A new revision (version + 1) is started.

## Related Requirements

- FR: [FR-storyboard-review-009](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-010](../srs/storyboard-review-spec.md#3-functional-requirements-fr)
- BR: BR-storyboard-review-001, BR-storyboard-review-002
- Errors: E-storyboard-review-001, E-storyboard-review-003, E-storyboard-review-004 (wording in the spec Error Matrix — TBD)
- Stories: US-003 · Diagram: [Approve and lock the storyboard (OUT) (Activity)](../srs/storyboard-review-flows.md)

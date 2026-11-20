# My dispatch policy

Fill in this template yourself before asking the builders to implement it. Short bullets and a small table are enough. You may discuss ideas or ask AI to challenge them, but make and explain your own choices.

## Priorities

- What I prioritise: I prioritise callers while also making use of elevators that are already travelling in the caller's direction, rather than starting another elevator unnecessarily.

- My exact selection rule:
    1. Use eligible_ids(...) to identify eligible elevators. If no elevator is eligible, return WAIT. If only one is eligible, select it.
    2. If one eligible elevator is moving and the other is idle, prefer the moving elevator.
    3. If the moving elevator is more than 4 floors away and the idle elevator is at least 3 floors closer, select the idle elevator instead.
    4. If both eligible elevators have the same status (both idle or both moving), choose the one with the shorter distance to the caller. If the distance is equal, choose the one with the lower load.

- My deterministic tie-breaker: If both distance and load are equal, choose Elevator A.

- A tradeoff I accept: A caller may wait longer because I prefer an elevator that is already moving instead of the nearest one. This prioritises using an existing journey, but it may delay the new caller.

## Predictions before implementation

Use S1, one of S2/S3, and one valid scenario you create in scenarios.py. For your own case, change something meaningful: location, direction, load or scheduled stops. Name it S6.

| Scenario | My expected selection | Why it follows my policy | Benefit and cost / who is affected |
|---|---|---|---|
| S1 | [A] | A is moving down towards the caller and is 3 floors away. It is not more than 4 floors away, so I prefer A over the idle B. | Avoids starting B, but the caller may wait longer than if B were selected. |
| S2 or S3 | [A] | A is still eligible because 325 + 65 = 390 kg, which is within the 520 kg limit. It is moving towards the caller and is 3 floors away. | Uses A's existing journey, but passengers already inside A may experience an additional stop. |
| S6: my scenario | [B] | A is moving down and is 5 floors away. B is idle and only 1 floor away, making it 4 floors closer. Therefore, I select B. | The caller gets the nearer elevator, but B needs to start a new journey. |

## Another defensible policy

- An alternative priority: Balance the usage of both elevators over a 24-hour period. The system could choose the elevator that has been used less during the day to distribute usage more evenly and potentially reduce uneven wear over time.

- A scenario where it could choose differently, and why: In S1, if Elevator A had already been used much more than Elevator B during the day, this alternative policy might choose B instead, even though A is already moving towards the caller. This could balance usage between the two elevators, but it requires daily usage data that is not available in the supplied model.

If your predicted choices contradict your general rule, resolve that before implementation. If review later changes your mind, note the revision in EVIDENCE.md and update the policy and code together.

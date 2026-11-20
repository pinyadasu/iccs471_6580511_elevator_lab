# My dispatch policy

Fill in this template yourself before asking the builders to implement it. Short bullets and a small table are enough. You may discuss ideas or ask AI to challenge them, but make and explain your own choices.

## Priorities

- What I prioritise: [whose experience or which resource matters most]
- My exact selection rule: [ordered rules or a defined cost formula, applied after eligibility]
- My deterministic tie-breaker: [what happens if candidates remain equal]
- A tradeoff I accept: [who may receive worse service, or what may cost more]

## Predictions before implementation

Use S1, one of S2/S3, and one valid scenario you create in scenarios.py. For your own case, change something meaningful: location, direction, load or scheduled stops. Name it S6.

| Scenario | My expected selection | Why it follows my policy | Benefit and cost / who is affected |
|---|---|---|---|
| S1 | [A/B] | [reason] | [tradeoff] |
| S2 or S3 | [A/B] | [reason] | [tradeoff] |
| S6: my scenario | [A/B/WAIT] | [reason] | [tradeoff] |

## Another defensible policy

- An alternative priority: [briefly describe it]
- A scenario where it could choose differently, and why: [use or adapt a case]

If your predicted choices contradict your general rule, resolve that before implementation. If review later changes your mind, note the revision in EVIDENCE.md and update the policy and code together.

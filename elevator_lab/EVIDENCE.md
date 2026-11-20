# My experiment results

Fill in this template with actual observations. Short bullets are sufficient.

Name / student ID: Pinyada Suthisopha-aphorn (6580511)

Tool, visible software version and model(s): VS Code GitHub Copilot Agent mode (Agent mode version, coordinator and reviewer: Auto (GPT-5.6 Luna), both builders: Auto (MAI Code 2 Flash)) and Python 3.14.4 (python3).

Route: automatic workers

## Agent outputs

| Role | What it delivered | Brief excerpt or screenshot link |
|---|---|---|
| Dispatcher builder | Wrote the code in dispatcher.py to choose an elevator based on the rules in POLICY.md. It also checks which elevators can take the request using eligible_ids(). | [Builders launched](EVIDENCE_screenshot/builders_launched.png), [Builder workers](EVIDENCE_screenshot/builders_workers.png) |
| Display builder | Wrote the code in app.py to show all scenarios, elevator information, requests, and the selected elevator with a reason. | [Builders launched](EVIDENCE_screenshot/builders_launched.png), [Builder workers](EVIDENCE_screenshot/builders_workers.png) |
| Reviewer | Checked the completed code without changing any files. It found no code problems or policy conflicts, but pointed out one tradeoff in S1. | [Reviewer](EVIDENCE_screenshot/reviewer.png) |

## Compare with my predictions

Run `python app.py` after adding S6. Compare with the predictions you wrote in POLICY.md before implementation.

| Scenario | Expected selection | Actual selection and reason | Matches my policy? |
|---|---|---|---|
| S1 | A | A : It is already moving towards the caller and is 3 floors away, so I choose A instead of idle elevator B. | YES |
| S2 | A | A : After adding one passenger, its load is 390 kg (325 + 65), which is still within the limit. It is also moving towards the caller and is 3 floors away. | YES |
| S6 | B | B : A is 5 floors away, but B is idle and only 1 floor away. Since B is at least 3 floors closer, I choose B. | YES |

    Other scenario results:
    - S3: A
    - S4: B (A is already at maximum capacity)
    - S5: WAIT (no eligible elevator)


- Application run: `python3 app.py` displayed all 6 scenarios and their decisions.

- Supplied suite command and actual result: I ran `python3 -m unittest -v` from the `elevator_lab` folder. All 6 tests passed.

- One review finding or concern I checked: The reviewer pointed out that in S1, elevator B is closer than A, but my policy still chooses A because it is already moving towards the caller. I decided to keep this rule because I prefer using an elevator that is already on its way, even if the caller may have to wait longer.

- Change made, if needed: I did not change the code or policy because the reviewer found no code problems, and the results matched my predictions.

- Does my policy serve my stated priority? Yes. In S1, my policy chooses A because it is already moving towards the caller. This means B does not need to start a new trip. However, the caller may wait longer because B is closer. Also, my policy compares the number of floors, not the actual waiting time.

- What did I have to coordinate between the agents? The two builders worked on different files. The Display builder could not fully test the application until the Dispatcher builder finished. I waited for both agents, checked their work together, and then ran the tests and application. At first, I ran the tests from the wrong folder, so no tests were found. I ran them again from the elevator_lab folder and they passed.

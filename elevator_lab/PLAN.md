# My agent plan

Fill in the brackets before delegation. This is a template, not a completed plan.

- Dispatcher builder owns dispatcher.py: Write choose_elevator(...) based on the rules in my POLICY.md. Use eligible_ids(...) to check which elevators can take the request. Follow my selection rules and return WAIT if neither elevator is eligible. Explain why the elevator is selected.

- Display builder owns app.py: Write run_scenarios(...) based on SPEC.md. Show each scenario, the elevator information and the request. Then show which elevator is selected, or WAIT, with a short reason. Keep the scenarios in the same order.

- Reviewer is read-only after both outputs are integrated: Check that both files follow SPEC.md and that dispatcher.py follows my POLICY.md. Check for mistakes, missing requirements and whether the results match my rules. The reviewer should only give feedback and should not edit any files.

- Handoff steps: I will use Agent mode in VS Code to delegate the work to two separate builders. The first builder will work only on dispatcher.py, and the second will work only on app.py. I will give both builders the project instructions and files they need. After they finish, I will check their changes, combine the results if needed and run the tests. Then, I will ask a separate reviewer to check the completed code without editing any files.

- Final check: Run python -m unittest -v and python app.py. Compare the actual results for S1, S2 and S6 with my predictions in POLICY.md. If any result is different, check why and fix the policy or code if needed. Record the results and any changes in EVIDENCE.md.
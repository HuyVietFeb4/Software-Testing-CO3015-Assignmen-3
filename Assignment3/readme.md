# Level 1: Static Logic Testing
Level 1 is used for rapid validation of core logic. It uses hard-coded environmental data and only pulls input and expected_result from the CSV files.
```
cd level1
python .\assignment_setting_time_limit.py
python .\assignment_setting_grade.py
```
# Level 2: Data-Driven Autonomous Testing
Level 2 is a fully decoupled framework. All interaction metadata—including login credentials, URLs, and element IDs—are injected via CSV, allowing the same script to test different environments without code changes.
```
cd ..\level2
python .\assignment_setting_time_limit.py
python .\assignment_setting_grade.py
```
# Non-Functional Testing (Baseline: TC-003-001)
This suite evaluates the system's responsiveness and stability by repeatedly executing a baseline test case from Level 2.
```
cd ..\non_functional
python .\non_functional_runner.py
```
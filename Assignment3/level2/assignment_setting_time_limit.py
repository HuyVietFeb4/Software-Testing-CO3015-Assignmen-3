import csv
from time_limit.TimeLimitTest import TimeLimitTest

timeLimit = TimeLimitTest()
try:
    with open('assignment_setting_time_limit_test_data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print(f"{'ID':<12} | {'Input':<10} | {'Status'}")
        print("-" * 40)
        for row in reader:
            actual = timeLimit.run_automated_test(row)
            expected = row['expected_result']
            
            if expected == actual or expected in str(actual):
                status = "PASS"
            else:
                status = f"FAIL (Got: {actual})"
            
            print(f"{row['test_case_id']:<12} | {row['input_value']:<10} | {status}")
finally:
    timeLimit.quit()
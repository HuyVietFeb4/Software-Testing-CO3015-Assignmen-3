import csv
from time_limit.TimeLimitTest import TimeLimitTest

TimeTest = TimeLimitTest()

try:
    TimeTest.login()
    
    with open('assignment_setting_time_limit_test_data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        print(f"{'ID':<12} | {'Input':<10} | {'Status':<10}")
        print("-" * 40)

        for row in reader:
            test_id = row['test_case_id']
            test_input = row['input']
            expected = row['expected_result']

            # RUN the selenium function and get the OUTPUT
            actual_output = TimeTest.test_time_limit(test_input)

            # COMPARE
            if actual_output == expected:
                status = "PASS"
            else:
                status = f"FAIL (Got: {actual_output})"

            print(f"{test_id:<12} | {test_input:<10} | {status}")

finally:
    TimeTest.quit()
import csv
from grade.GradeTest import GradeTest

gradeTest = GradeTest()

try:
    gradeTest.login()
    
    with open('assignment_setting_grade_test_data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        print(f"{'ID':<12} | {'Input 1':<10} | {'Input 2':<10} | {'Status':<10}")
        print("-" * 40)

        for row in reader:
            test_id = row['test_case_id']
            test_input1 = row['input1']
            test_input2 = row['input2']
            expected1 = row['expected_result1']
            expected2 = row['expected_result2']

            actual_output = gradeTest.test_grade_settings(test_input1, test_input2)
            expected = f"Max: {test_input1}, Pass: {test_input2}.00"
            if actual_output == expected or expected1 == actual_output or expected2 == actual_output:
                status = "PASS"
            else:
                status = f"FAIL (Got: {actual_output})"
                print(f"Expected: {expected}")

            print(f"{test_id:<12} | {test_input1:<10} | {test_input2:<10} | {status}")

finally:
    gradeTest.quit()
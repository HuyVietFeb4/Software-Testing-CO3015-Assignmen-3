import csv
from grade.GradeTest import GradeTest

gradeTest = GradeTest()
try:
    with open('assignment_setting_grade_test_data.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print(f"{'ID':<12} | {'Input 1':<10} | {'Input 2':<10} | {'Status':<10}")
        print("-" * 80)
        for row in reader:
            actual = gradeTest.run_grade_test(row)
            if row['expected1'] in actual or row['expected2'] in actual:
                status = "PASS"
            else:
                status = "FAIL"
            print(f"{row['test_case_id']:<12} | {row['input1']:<10} | {row['input2']:<10} | {status}")
finally:
    gradeTest.quit()
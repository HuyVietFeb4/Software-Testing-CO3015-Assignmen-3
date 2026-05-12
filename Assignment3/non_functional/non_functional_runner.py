import csv
from respond_time_test import ResponseTimeEvaluator
from reliability_test import ReliabilityEvaluator

csv_path = 'assignment_setting_time_limit_test_data.csv'

def display_header(title):
    print(f"\n{'='*10} {title} {'='*10}")
    print(f"{'ID':<12} | {'Metric':<10} | {'Status'}")
    print("-" * 40)

try:
    # Run Performance Metrics
    display_header("PERFORMANCE (RESPONSE TIME)")
    perf_test = ResponseTimeEvaluator(threshold=2.0)
    with open(csv_path, mode='r', encoding='utf-8') as file:
        for row in csv.DictReader(file):
            res = perf_test.run_metrics(row)
            print(f"{res['id']:<12} | {res['value']:<8}s | {res['status']}")
    perf_test.tester.quit()

    # Run Reliability Metrics
    display_header("AVAILABILITY & RELIABILITY")
    rel_test = ReliabilityEvaluator()
    with open(csv_path, mode='r', encoding='utf-8') as file:
        for row in csv.DictReader(file):
            res = rel_test.run_metrics(row)
            print(f"{res['id']:<12} | {res['value']:<8}s | {res['status']}")
    rel_test.tester.quit()

except FileNotFoundError:
    print("Error: CSV file not found.")
finally:
    print("\nNon-Functional Testing Complete.")
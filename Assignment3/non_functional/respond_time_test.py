import time
from time_limit.TimeLimitTest import TimeLimitTest

class ResponseTimeEvaluator:
    def __init__(self, threshold=2.0):
        self.threshold = threshold
        self.tester = TimeLimitTest()

    def run_metrics(self, row):
        _, duration = self.tester.run_automated_test(row)
        
        status = "PASS" if duration <= self.threshold else "FAIL (SLOW)"
        
        return {
            "id": row['test_case_id'],
            "value": duration,
            "status": status,
            "type": "Response Time"
        }
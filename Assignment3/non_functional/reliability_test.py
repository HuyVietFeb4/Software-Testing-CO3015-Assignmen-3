import time
import statistics
from time_limit.TimeLimitTest import TimeLimitTest

class ReliabilityEvaluator:
    def __init__(self, inconsistency_threshold=0.5):
        self.tester = TimeLimitTest()
        self.history = []
        self.inconsistency_threshold = inconsistency_threshold

    def run_metrics(self, row):
        try:
            _, duration = self.tester.run_automated_test(row)
            self.history.append(duration)
            
            if len(self.history) > 1:
                mean_time = statistics.mean(self.history[:-1])
                deviation = abs(duration - mean_time)
                
                if deviation > self.inconsistency_threshold:
                    status = f"INCONSISTENT (Δ {deviation:.2f}s)"
                else:
                    status = "STABLE"
            else:
                status = "INITIALIZING" 
                deviation = 0

        except Exception as e:
            status = "SYSTEM FAILURE"
            duration = 0
            deviation = 999
            
        return {
            "id": row['test_case_id'],
            "value": round(duration, 3),
            "deviation": round(deviation, 3),
            "status": status,
            "type": "Reliability (Consistency)"
        }
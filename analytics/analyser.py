class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented")

    def print_results(self):
        for k, v in self.result.items():
            print(k, ":", v)


class SleepAnalyser(DataAnalyser):
    def analyse(self):
        low = []
        high = []

        for s in self.students:
            sleep = float(s["sleep_hours"])
            gpa = float(s["GPA"])

            if sleep < 6:
                low.append(gpa)
            else:
                high.append(gpa)

        avg_low = round(sum(low) / len(low), 2)
        avg_high = round(sum(high) / len(high), 2)

        self.result = {
            "analysis": "Sleep vs GPA",
            "low_sleep": avg_low,
            "high_sleep": avg_high,
            "gpa_difference": round(avg_high - avg_low, 2),
            "total_students": len(self.students)
        }

        return self.result

    def print_results(self):
        print("==== SLEEP ANALYSIS ====")
        super().print_results()

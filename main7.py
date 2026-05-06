import os
import csv
import json

CSV_FILE = "students.csv"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.json")


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print("File found: students.csv")
            return True
        print("Error: students.csv not found.")
        return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Output folder created: output/")
        else:
            print("Output folder already exists: output/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print("Error: file not found.")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)


# Task 1 — Base class
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


# Task 2 — Variant C Child class
class SleepAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        low_sleep_gpas = []
        high_sleep_gpas = []

        for student in self.students:
            try:
                sleep = float(student["sleep_hours"])
                gpa = float(student["GPA"])
            except ValueError:
                continue

            if sleep < 6:
                low_sleep_gpas.append(gpa)
            else:
                high_sleep_gpas.append(gpa)

        avg_low = round(sum(low_sleep_gpas) / len(low_sleep_gpas), 2)
        avg_high = round(sum(high_sleep_gpas) / len(high_sleep_gpas), 2)
        difference = round(abs(avg_high - avg_low), 2)

        self.result = {
            "analysis": "Sleep vs GPA",
            "total_students": len(self.students),
            "low_sleep": {
                "students": len(low_sleep_gpas),
                "avg_gpa": avg_low
            },
            "high_sleep": {
                "students": len(high_sleep_gpas),
                "avg_gpa": avg_high
            },
            "gpa_difference": difference
        }

        return self.result

    def print_results(self):
        print("=" * 30)
        print("SLEEP VS GPA REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"SleepAnalyser: Sleep vs GPA, {len(self.students)} students"


# Extra analyser for Task 5 polymorphism
class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = []

        for student in self.students:
            try:
                gpa = float(student["GPA"])
                gpas.append(gpa)
            except ValueError:
                continue

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas)
        }

        return self.result

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(self.result, f, indent=4)
            print("Result saved to output/result.json")
        except Exception as e:
            print(f"Error saving file: {e}")


# Task 4 — Association
class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser
        self.saver = saver

    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.result = self.analyser.result
        self.saver.save_json()
        print("Report complete.")


# Main
fm = FileManager(CSV_FILE)

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader(CSV_FILE)
dl.load()
dl.preview()


# Task 5 — Polymorphism
print("-" * 30)
print("Running all analysers:")
print("-" * 30)

analysers = [
    SleepAnalyser(dl.students),
    GpaAnalyser(dl.students)
]

for analyser in analysers:
    print(analyser)
    analyser.analyse()
    analyser.print_results()


# Task 4 — Report
main_analyser = SleepAnalyser(dl.students)
saver = ResultSaver(main_analyser.result, OUTPUT_FILE)
report = Report(main_analyser, saver)
report.generate()

import os
import csv
import json

CSV_FILE = "students.csv"
OUTPUT_FILE = "output/result.json"


# FileManager
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print("File found: students.csv")
            return True
        print("Error: file not found")
        return False

    def create_output_folder(self):
        print("Checking output folder...")
        if not os.path.exists("output"):
            os.makedirs("output")
            print("Output folder created")
        else:
            print("Output folder exists")


# DataLoader
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        with open(self.filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.students = list(reader)
        print("Loaded:", len(self.students))
        return self.students

    def preview(self):
        print("Preview:")
        for s in self.students[:5]:
            print(s["student_id"], s["GPA"])


# Base class
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented")

    def print_results(self):
        for k, v in self.result.items():
            print(k, ":", v)


# Variant C
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
            "low_sleep": avg_low,
            "high_sleep": avg_high,
            "gpa_difference": round(avg_high - avg_low, 2),
            "total_students": len(self.students)
        }

        return self.result

    def print_results(self):
        print("==== SLEEP ANALYSIS ====")
        super().print_results()


# ResultSaver
class ResultSaver:
    def __init__(self, result, path):
        self.result = result
        self.path = path

    def save_json(self):
        with open(self.path, "w") as f:
            json.dump(self.result, f, indent=4)
        print("Saved to JSON")


# Report
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
        print("Done")


# MAIN
fm = FileManager(CSV_FILE)

if not fm.check_file():
    exit()

fm.create_output_folder()

dl = DataLoader(CSV_FILE)
dl.load()
dl.preview()

analyser = SleepAnalyser(dl.students)
saver = ResultSaver(analyser.result, OUTPUT_FILE)

report = Report(analyser, saver)
report.generate()

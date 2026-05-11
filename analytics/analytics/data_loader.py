import csv


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

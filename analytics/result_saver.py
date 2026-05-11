import json


class ResultSaver:
    def __init__(self, result, path):
        self.result = result
        self.path = path

    def save_json(self):
        with open(self.path, "w") as f:
            json.dump(self.result, f, indent=4)

        print("Saved to JSON")

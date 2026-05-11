import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print("File found:", self.filename)
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

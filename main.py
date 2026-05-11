from analytics.file_manager import FileManager
from analytics.data_loader import DataLoader
from analytics.analyser import SleepAnalyser
from analytics.result_saver import ResultSaver
from analytics.report import Report

CSV_FILE = "students.csv"
OUTPUT_FILE = "output/result.json"

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

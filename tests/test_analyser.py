from analytics.analyser import SleepAnalyser

students = [
    {"sleep_hours": "5", "GPA": "3.0"},
    {"sleep_hours": "7", "GPA": "4.0"}
]

analyser = SleepAnalyser(students)
result = analyser.analyse()

print(result)

assert result["gpa_difference"] == 1.0

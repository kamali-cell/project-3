# Online Examination and Evaluation System - Core Engine
def calculate_score(correct_answers, total_questions):
    if total_questions == 0:
        return 0
    return (correct_answers / total_questions) * 100

print("Online Exam core functions initialized.")

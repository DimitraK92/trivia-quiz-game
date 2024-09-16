from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import signal, os

def handle_interrupt_signal(signum, frame):
    clear_console()
    exit(1)

signal.signal(signal.SIGINT, handle_interrupt_signal)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
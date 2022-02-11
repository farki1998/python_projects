from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
all_questions = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    all_questions.append(new_question)

quiz = QuizBrain(all_questions)
while quiz.still_has_questions:
    quiz.next_question()

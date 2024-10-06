import ast
import random

name = input("Enter your name: ")
print(f"Hello {name}, welcome to this quiz game.")


with open('questions.txt','r') as f:
    content = f.read()


questions_dict = ast.literal_eval(content)

questions = list(questions_dict.keys())
score = 0
random.shuffle(questions)
for question in questions:
    print(question)
    my_answer = input("Enter your answer: ").lower()
    
    
    if my_answer == questions_dict[question].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is: {questions_dict[question]}")


print(f"You got {score} answers correct out of {len(questions)}.")

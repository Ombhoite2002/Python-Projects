import ast

name = input("Enter your name: ")

print(f"Hello {name} welcom to this quiz game.")

with open('questions.txt','r') as f:
    content = f.read()

dict = ast.literal_eval(content)

questions = []
score = 0

for question in dict.keys():
    questions.append(question)

for question in questions:
    print(question)
    my_answer = input("Enter your Answer: ").lower()

    if my_answer == dict[question]:
        print("correct")
        score += 1
    else:
        print("incorrect")

print(f"You got {score} answers correct out of {len(questions)}.")

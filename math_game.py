import random
import time

OPERATORS = ["+", "-", "*"]
MIN_VALUE = 3
MAX_VALUE = 12
NUM_QUESTIONS = 10

PROMPTS = [
    "Try this one:",
    "Can you solve it?",
    "Next up:",
    "How about this:",
    "Alright, go!"
]

print(" Welcome to the Math Challenge! ")
print("Test your skills with quick math problems.")
print("You'll be timed, and mistakes will be counted!")
input("Press Enter when you're ready to begin...")

def create_question():
    num1 = random.randint(MIN_VALUE, MAX_VALUE)
    num2 = random.randint(MIN_VALUE, MAX_VALUE)
    op = random.choice(OPERATORS)
    
    question = f"{num1} {op} {num2}"
    result = eval(question)
    return question, result


def run_quiz():
    mistakes = 0
    print("\n Starting now...\n")
    start = time.time()

    for i in range(NUM_QUESTIONS):
        question, answer = create_question()
        while True:
            prompt = random.choice(PROMPTS)
            guess = input(f"{prompt} Problem #{i+1}: {question} = ")
            if guess.strip() == str(answer):
                print(" Correct!\n")
                break
            else:
                print(" Try again.\n")
                mistakes += 1

    end = time.time()
    duration = round(end - start, 2)
    score = NUM_QUESTIONS - mistakes
    percentage = (score / NUM_QUESTIONS) * 100

    print(" All done!")
    print("-----------------------------")
    print(f"Total Time: {duration} seconds")
    print(f"Mistakes: {mistakes}")
    print(f"Score: {score}/{NUM_QUESTIONS} ({percentage:.1f}%)")

    if percentage == 100:
        print(" Perfect! You're a math wizard!")
    elif percentage >= 80:
        print(" Great job!")
    elif percentage >= 50:
        print(" Not bad, keep practicing!")
    else:
        print(" Time to sharpen those skills!")


run_quiz()
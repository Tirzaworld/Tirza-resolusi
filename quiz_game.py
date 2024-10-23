
def quiz_game():
    print("Welcome to the Quiz Game!")
    score = 0
    questions = {
        "What is the capital of France? ": "Paris",
        "What is 2 + 2? ": "4",
        "What color do you get when you mix red and white? ": "pink"
    }

    for question, answer in questions.items():
        user_answer = input(question).strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"Your total score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()

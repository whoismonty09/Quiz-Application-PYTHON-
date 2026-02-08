questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 12", "C. 11", "D. 13"],
        "answer": "B"
    }
]

score = 0

print("Welcome to the Quiz Application!\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong answer!\n")

print(f"Quiz Finished! Your Score: {score}/{len(questions)}")

from string import ascii_lowercase
import random

NUM_QUESTIONS_PER_QUIZ = 5

QUESTIONS = { 

    "How many active teams were present in Quebec during the 2024 season": [

        "39", "40", "28", "42"
    ],

    "Who won the Chairman's Award at the 2022 Montreal Regional": [

        "2626 - Evolution", "3990 - Tech for Kids", "3544 - Spartiates", "3360 - Hyperion",

    ],

    "Who won the Impact Award at Worlds in 2023": [

        "321 - Robolancers", "2056 - OP Robotics", "5553 - Robo'Lyon", "16 - Bomb Squad"
    ],

    "Where where the 2 Quebec Regionals in 2020": [

        "Sherbrooke and Montreal", "Montreal and Quebec City", "Montreal and Trois-Rivières", "Quebec City and Gatineau"

    ],
    
    "Which Quebec team won Worlds and which year": [

        "296 - 2006", "2016 - 3990", "3996 - 2016", "7605 - 2019"
    ],

    "Which Quebec team was interviewed by FIRST Update Now in 2024": [

        "3117 - Harfangs", "5528 - Ultime AGT", "9624 - Dynamiques", "9406 - TechJunior"
    ],

    "Who won the Impact Award at Worlds in 2023": [

        "321 - Robolancers", "2056 - OP Robotics", "5553 - Robo'Lyon", "16 - Bomb Squad"
    ],
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS)) #gets the number of questions
questions = random.sample(list(QUESTIONS.items()), k=num_questions) #scrambles the questions

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1): #enumerate the qustions
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0] #defines the correct question
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")
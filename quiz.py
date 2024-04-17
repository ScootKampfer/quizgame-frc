# step 2

from string import ascii_lowercase

QUESTIONS = {

    "How many active teams were present in Quebec during the 2024 season": [

        "39", "40", "28", "42"
    ],

    "Who won the Chairman's Award at the 2022 Montreal Regional": [

        "2626 - Evolution",
        "3990 - Tech for Kids",
        "3544 - Spartiates",
        "3360 - Hyperion",
    ],

    "Who won the Impact Award at Worlds in 2023": [

        "321 - Robolancers", "2056 - OP Robotics", "5553 - Robo'Lyon", "16 - Bomb Squad"
    ],
}

for question, alternatives in QUESTIONS.items():

    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)

    for label, alternative in enumerate(sorted_alternatives):

        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]

    if answer == correct_answer:

        print("Correct!")
    else:

        print(f"The answer is {correct_answer!r}, not {answer!r}")
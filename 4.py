def quiz_user(questions_and_answers):
    num_correct_answers = 0
    total_questions = len(questions_and_answers)
    
    for qa in questions_and_answers:
        question = qa["question"]
        answer = qa["answer"]
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            num_correct_answers += 1
        else:
            print("Incorrect. The correct answer is:", answer)

    score = (num_correct_answers / total_questions) * 100
    return score

questions_and_answers = [
    {
        "question": "What color is the sky?",
        "answer": "Blue"
    },
    {
        "question": "How many legs does a cat have?",
        "answer": "Four"
    },
    {
        "question": "What is the opposite of hot?",
        "answer": "Cold"
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4"
    }
]

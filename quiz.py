print("Welcome to the quiz!")
playing = input("Do you want to play? ")

if playing.lower() == "yes":
    print("Great! Let's start.")
    print("I will ask you 5 questions.")
    print("You will answer with the letter of the answer, the name of the answer, or type 'skip' to skip the question.")
    print("Make sure to answer correctly to get the highest score.")
    print("If you answer incorrectly, you will lose 0.25 points.")
    print("Good luck!")
else:
    print("See you next time!")
    quit()

# Initialize score and counters
score = 0
correct_answers = 0
incorrect_answers = 0
skipped_questions = 0

# Question 1
print("Question 1: What is the capital of France?")
print("A: Madrid")
print("B: Paris")
print("C: London")
print("D: Berlin")

answer = input("Your answer: ")

if answer.lower() == "b" or answer.lower() == "paris":
    print("Correct!")
    score += 1
    correct_answers += 1
elif answer.lower() == "skip":
    print("You chose to skip this question.")
    skipped_questions += 1
else:
    print("Incorrect! The correct answer is Paris.")
    score -= 0.25
    incorrect_answers += 1

print("Your score is " + str(score))
print("Here is your next question:")

# Question 2
print("Question 2: What is the capital of Germany?")
print("A: Madrid")
print("B: Paris")
print("C: London")
print("D: Berlin")

answer = input("Your answer: ")

if answer.lower() == "d" or answer.lower() == "berlin":
    print("Correct!")
    score += 1
    correct_answers += 1
elif answer.lower() == "skip":
    print("You chose to skip this question.")
    skipped_questions += 1
else:
    print("Incorrect! The correct answer is Berlin.")
    score -= 0.25
    incorrect_answers += 1

print("Your score is " + str(score))
print("Here is your next question:")

# Question 3
print("Question 3: What is the capital of Italy?")
print("A: Madrid")
print("B: Rome")
print("C: London")
print("D: Berlin")

answer = input("Your answer: ")

if answer.lower() == "b" or answer.lower() == "rome":
    print("Correct!")
    score += 1
    correct_answers += 1
elif answer.lower() == "skip":
    print("You chose to skip this question.")
    skipped_questions += 1
else:
    print("Incorrect! The correct answer is Rome.")
    score -= 0.25
    incorrect_answers += 1

print("Your score is " + str(score))
print("Here is your next question:")

# Question 4
print("Question 4: What is the capital of Spain?")
print("A: Madrid")
print("B: Rome")
print("C: Madrid")
print("D: Berlin")

answer = input("Your answer: ")

if answer.lower() == "a" or answer.lower() == "madrid":
    print("Correct!")
    score += 1
    correct_answers += 1
elif answer.lower() == "skip":
    print("You chose to skip this question.")
    skipped_questions += 1
else:
    print("Incorrect! The correct answer is Madrid.")
    score -= 0.25
    incorrect_answers += 1

print("Your score is " + str(score))
print("Here is your next question:")

# Question 5
print("Question 5: What is the capital of Portugal?")
print("A: Madrid")
print("B: Dublin")
print("C: London")
print("D: Lisbon")

answer = input("Your answer: ")

if answer.lower() == "d" or answer.lower() == "lisbon":
    print("Correct!")
    score += 1
    correct_answers += 1
elif answer.lower() == "skip":
    print("You chose to skip this question.")
    skipped_questions += 1
else:
    print("Incorrect! The correct answer is Lisbon.")
    score -= 0.25
    incorrect_answers += 1

print("Your score is " + str(score))

# Final Summary
print("\nQuiz Summary:")
print("Correct answers: " + str(correct_answers))
print("Incorrect answers: " + str(incorrect_answers))
print("Skipped questions: " + str(skipped_questions))
print("Your final score is " + str(score))
if score == 5:
    print("Perfect score! Well done!")
elif score >= 4:
    print("Great job! Attempt to get a full score!")
elif score < 4 and score >= 3:
    print("You are doing well.")
elif score < 3 and score >= 2.5:
    print("You need to study more.")
else:
    print("You failed. Better luck next time.")

print("Thank you for playing the quiz!")

from questions import questions

user_name = input("Enter your name: ")
print(f"Welcome {user_name} to the Quiz Game!")

score = 0
for q in questions:
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    answer = input("Enter option number: ")
    if q["options"][int(answer)-1] == q["answer"]:
        score += 1

print(f"\nYour score: {score}/{len(questions)}")

with open("scores.txt", "a") as f:
    f.write(f"{user_name}: {score}/{len(questions)}\n")

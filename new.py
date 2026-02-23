import random

class Question:
    def _init_(self, question, options, answer, difficulty):
        self.question = question
        self.options = options
        self.answer = answer
        self.difficulty = difficulty

    def display(self):
        print("\n" + self.question)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    def check_answer(self, user_choice):
        try:
            return self.options[user_choice-1].lower() == self.answer.lower()
        except:
            return False



class QuizGame:
    def _init_(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def select_difficulty(self):
        print("\nSelect Difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter choice: ")

        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Default Easy selected.")
            return "easy"

    def start(self):
        difficulty = self.select_difficulty()

        filtered_questions = [q for q in self.questions if q.difficulty == difficulty]

        random.shuffle(filtered_questions)

        for question in filtered_questions:
            question.display()

            try:
                user_choice = int(input("Your answer (number): "))
            except:
                print("Invalid input!")
                continue

            if question.check_answer(user_choice):
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer: {question.answer}")

        print("\n===== QUIZ FINISHED =====")
        print(f"Your Score: {self.score}/{len(filtered_questions)}")


quiz = QuizGame()

quiz.add_question(Question(
    "Python ka creator kaun hai?",
    ["Elon Musk", "Guido van Rossum", "Mark Zuckerberg", "Bill Gates"],
    "Guido van Rossum",
    "easy"
))

quiz.add_question(Question(
    "List comprehension kya hota hai?",
    ["Loop shortcut", "Function", "Class", "Library"],
    "Loop shortcut",
    "medium"
))

quiz.add_question(Question(
    "Python me GIL ka matlab kya?",
    ["Global Interpreter Lock", "General Input Loop", "Graph Index Logic", "None"],
    "Global Interpreter Lock",
    "hard"
))


while True:
    quiz.start()

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
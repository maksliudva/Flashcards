
def print_menu():
    print('''
1. Add flashcards
2. Practice flashcards
3. Exit

    ''')

def print_flashcards_menu():
    print('''
1. Add a new flashcard
2. Exit
    ''')

def get_user_input(prompt):
    """Gets and validates user non-empty input from the user"""
    user_input = input(prompt).strip()

    while not user_input:
        print("Input cannot be empty.Please try again.")
        user_input = input(prompt).strip()

    return user_input

def add_or_update_flashcard(questions, question, answer):
    """Adds or updates flashcard in the dictionary"""
    if question in questions:
        print(f"The question {question} is already present.")
        update = input("Do you want to update the answer (y/n): ").strip()
        if update == "y":
            questions[question] = answer
            print(f"Updated flashcard: {question} -> '{answer}'.")
        else:
            print("No changes made.")
    else:
        questions[question] = answer
        print(f"Updated flashcard: {question} -> '{answer}'.")

def add_flashcards(questions):
    """Main function to add a flashcard."""
    question = get_user_input("Question: \n")
    answer = get_user_input("Answer: \n")
    add_or_update_flashcard(questions, question, answer)

def print_flashcard(question, answer):
    print(f"Question: {question}")
    print("Please press 'y' to see the answer or press 'n' to skip: ")
    user_input = input().strip()

    while not user_input or user_input not in ["y", "n"]:
        print("Input cannot be empty or be other than 'y' or 'n'.Please try again.")

    if user_input == "y":
        print(f"The answer is '{answer}'.\n")
    if user_input == "n":
        return False


def main():
    questions = {}

    while True:
        print_menu()
        choice = get_user_input("> ").strip()
        if choice not in ["1", "2", "3"]:
            print(f"{choice} is not a valid option. Please try again.")

        if choice == "1":

            while True:
                print_flashcards_menu()
                flashcard_choice = get_user_input("> ").strip()

                if flashcard_choice not in ["1", "2"]:
                    print(f"{flashcard_choice} is not a valid option. Please try again.")

                if flashcard_choice == "1":
                    add_flashcards(questions)
                if flashcard_choice == "2":
                    break

        if choice == "2":

            if not questions:
                print("No flashcards available.")
            else:
                for question, answer in questions.items():
                    print_flashcard(question, answer)
        if choice == "3":
            print("Bye!")
            break


if __name__ == '__main__':
    main()
# import time

# students = []
# def clear_terminal():
#     print("\033c", end="")

# school = int(input("Enter the number of students: "))
# time.sleep(2)
# clear_terminal()
# for _ in range(school): 
#   _ += 1
#   student_name = input(f"Enter The name of The {_} student: ")
#   time.sleep(1)
#   student_marks = int(input(f"Enter The marks of ''{student_name}'' : "))
#   students.append((student_name, student_marks))
#   clear_terminal()


# students.sort(key=lambda student: student[1], reverse=True)

# for student in students:
#   time.sleep(3)
# #   print(f"Name: {student[0]}, Marks: {student[1]}")
# import time

# choices = ["rock", "paper", "scissors"]

# def pseudo_random_choice():
#     current_time = int(time.time())  # Using the current time for randomness
#     return choices[current_time % len(choices)]

# def get_user_choice():
#     while True:
#         user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#         if user_choice in choices:
#             return user_choice
#         print("Invalid choice. Please try again.")

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         return "You win!"
#     else:
#         return "You lose!"

# def play_game():
#     user_score = 0
#     computer_score = 0
#     rounds = 5  # Number of rounds to play
    
#     for _ in range(rounds):
#         user_choice = get_user_choice()
#         computer_choice = pseudo_random_choice()
#         print(f"Computer chose: {computer_choice}")
#         result = determine_winner(user_choice, computer_choice)
#         print(result)
        
#         if result == "You win!":
#             user_score += 1
#         elif result == "You lose!":
#             computer_score += 1
        
#         print(f"Score -> You: {user_score}, Computer: {computer_score}")
#         print("-------------------")
        
#     if user_score > computer_score:
#         print("Congratulations! You won the game!")
#     elif user_score < computer_score:
#         print("Sorry, the computer won the game.")
#     else:
#         print("It's a tie!")

# if __name__ == "__main__":
#     play_game()


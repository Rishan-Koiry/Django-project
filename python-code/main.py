import sys

# import pyttsx3
# engine = pyttsx3.init()
# engine.say('''  The sky awakes in hues of pink,
# A gentle brush where morning's ink
# Dips low in shadows, soft and warm,
# Caressing earth in quiet charm.

# The wind, it stirs the trees with grace,
# A whispered touch, a sweet embrace,
# Each leaf dances, trembling light,
# As stars fade into the rising light.

# The world, it hums a tender song,
# Of moments passed and days along,
# In silence, we begin anew,
# With dreams as deep as skies of blue.

# So let the day unfold its wings,
# And carry us to brighter things,
# For every dawn, a chance to see,
# The beauty in simplicity.''')
# engine.runAndWait()




# fruits=[]
# for i in range(7):
#     f1=input("Enter the name of the fruit: ")
#     fruits.append(f1)
# print(fruits)
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
#   print(f"Name: {student[0]}, Marks: {student[1]}")
# i = 1

# while i < 51:
#     print(f"{i})Aditro Prnice")
#     i += 1
 
 

# or and describe the difference between them.
# if 5>6 and 2>9 and 3>8:
#     print("True")
# else:
#     print("False")    
# import sys
# import os
# sys.stdout.reconfigure(encoding='utf-8')
# os.system("")

# import random
# import time

# def clear_terminal():
#     print("\033c", end="")

# def get_fruit_hint(fruit):
#     hints = {
#         "apple": "🍏 This fruit keeps the doctor away!",
#         "banana": "🍌 Monkeys love this yellow fruit!",
#         "cherry": "🍒 A small red fruit often used in desserts!",
#         "date": "🌴 A sweet fruit popular in the Middle East!",
#         "elderberry": "🫐 A dark berry known for boosting immunity!",
#         "fig": "🍈 A soft fruit full of energy!",
#         "grape": "🍇 Used to make juice and wine!",
#         "honeydew": "🍈 A sweet green melon!",
#         "jackfruit": "🍈 The largest fruit with a strong aroma!",
#         "kiwi": "🥝 Brown and fuzzy outside, green inside!",
#         "lemon": "🍋 A sour fruit used in lemonade!",
#         "mango": "🥭 Known as the 'King of Fruits'!",
#         "nectarine": "🍑 Looks like a peach but has smooth skin!",
#         "orange": "🍊 A citrus fruit rich in Vitamin C!",
#         "papaya": "🍈 A tropical fruit with black seeds inside!",
#         "quince": "🍏 Often used in jams!",
#         "raspberry": "🍇 A red fruit with a sweet-tart taste!",
#         "strawberry": "🍓 A fruit with seeds on the outside!",
#         "tangerine": "🍊 A small, easy-to-peel orange-like fruit!",
#         "watermelon": "🍉 A juicy summer fruit with a green rind!"
#     }
#     return hints.get(fruit, "🍍 A delicious fruit!")

# def play_game():
#     clear_terminal()
#     print("🎉 Welcome to RK Fruit Guessing Game! 🎉")
#     time.sleep(1)
#     clear_terminal()

#     print("Your task is to guess the name of a fruit.")
#     time.sleep(1)
#     clear_terminal()
#     print("You have 10 lives. Each wrong guess costs 1 life.")
#     time.sleep(1)
#     clear_terminal()
#     print("Let’s begin With RK! 🍎🍌🍉")
#     time.sleep(1)
#     clear_terminal()

#     fruits = random.choice([
#         "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
#         "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine",
#         "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"
#     ])

#     lives = 10
#     guessed_letters = set()
#     fruit_letters = set(fruits)

#     while lives > 0:
#         guess = input("Guess a letter: ").lower()
#         if guess in guessed_letters:
#             print("⚠️ You already guessed that letter!")
#             continue

#         guessed_letters.add(guess)

#         if guess in fruit_letters:
#             print("✅ Correct guess!")
#         else:
#             lives -= 1
#             print(f"❌ Wrong guess! You have {lives} lives left.")
#             print(f"🔎 Hint: {get_fruit_hint(fruits)}")

#         current_progress = [letter if letter in guessed_letters else '_' for letter in fruits]
#         print("Current progress:", ' '.join(current_progress))

#         if set(current_progress) == fruit_letters:
#             print(f"🎉 Congratulations! You guessed the fruit: {fruits}!")
#             break
#     else:
#         print(f"😢 Sorry, you lost! The correct fruit was: {fruits}")

#     play_again = input("Play again? (y/n): ").lower()
#     if play_again == 'y':
     
#         play_game()
#     else:
#         print("👋 Goodbye! Thanks for playing RK Fruit Guessing Game!")

# play_game()




# import random
# com=random.randint(1,10)

# user=int(input("Enter the number between 1 to 10: "))
# if user==com:
#     print("You have guessed the correct number")
# else:
#     print("You have guessed the wrong number")
#     print(f"The correct number is {com}")



# for i in range(1,101):
#   print(i)
# import random
# import os
# import time
# import json

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def load_high_scores():
#     if os.path.exists("high_scores.json"):
#         with open("high_scores.json", "r") as file:
#             return json.load(file)
#     return {}

# def save_high_scores(high_scores):
#     with open("high_scores.json", "w") as file:
#         json.dump(high_scores, file)

# def display_high_scores(high_scores):
#     print("\nHigh Scores:")
#     for name, score in sorted(high_scores.items(), key=lambda x: x[1], reverse=True):
#         print(f"{name}: {score}")

# def memory_game():
#     clear_screen()
#     high_scores = load_high_scores()
#     print("Welcome to the Memory Game!")
#     player_name = input("Enter your name: ").strip()
#     difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()

#     if difficulty == "easy":
#         NUMBERS_TO_MEMORIZE = 5
#         MEMORIZATION_TIME = 10
#         GUESS_TIME_LIMIT = 30
#     elif difficulty == "medium":
#         NUMBERS_TO_MEMORIZE = 7
#         MEMORIZATION_TIME = 7
#         GUESS_TIME_LIMIT = 20
#     elif difficulty == "hard":
#         NUMBERS_TO_MEMORIZE = 10
#         MEMORIZATION_TIME = 5
#         GUESS_TIME_LIMIT = 15
#     else:
#         print("Invalid difficulty. Defaulting to medium.")
#         NUMBERS_TO_MEMORIZE = 7
#         MEMORIZATION_TIME = 7
#         GUESS_TIME_LIMIT = 20

#     random_numbers = random.sample(range(1, 101), NUMBERS_TO_MEMORIZE)
#     print(f"\nYou have {MEMORIZATION_TIME} seconds to memorize these {NUMBERS_TO_MEMORIZE} numbers:")
#     print(random_numbers)
#     time.sleep(MEMORIZATION_TIME)
#     clear_screen()

#     print(f"Time's up! You have {GUESS_TIME_LIMIT} seconds to enter the numbers.")
#     print("You can enter the numbers in any order. If you forget a number, just skip it!")
#     guessed_numbers = []
#     start_time = time.time()

#     while time.time() - start_time < GUESS_TIME_LIMIT:
#         try:
#             guess = input("Enter a number 1-100 (or 'done' to finish): ").strip().lower()
#             if guess == 'done':
#                 break
#             guess = int(guess)
#             if guess < 1 or guess > 100:
#                 print("Number must be between 1 and 100.")
#             else:
#                 guessed_numbers.append(guess)
#         except ValueError:
#             print("Invalid input! Enter a number or 'done' to finish.")

#     clear_screen()
#     correct_guesses = [num for num in guessed_numbers if num in random_numbers]
#     score = len(correct_guesses)
#     print("Game Over!")
#     print(f"The numbers were: {random_numbers}")
#     print(f"Your guesses: {guessed_numbers}")
#     print(f"Correct guesses: {correct_guesses}")
#     print(f"Your score: {score}/{NUMBERS_TO_MEMORIZE}")

#     if score == NUMBERS_TO_MEMORIZE:
#         print("Congratulations! You remembered all the numbers!")
#     else:
#         print("Better luck next time!")

#     high_scores[player_name] = max(high_scores.get(player_name, 0), score)
#     save_high_scores(high_scores)
#     clear_screen()
#     display_high_scores(high_scores)

# if __name__ == "__main__":
#     memory_game()




# print(4**5)
# name= ["Risen", "khan", "auditor", "prince",
#        "dishy", "khan", "auditor", "prince",        
#        "dishy", "khan", "auditor", "prince",
#        "dishy", "khan", "auditor", "prince",
#         "dishy", "khan", "auditor", "prince",]
# name1=input("Enter the name: ")
# if name1 in name:
#     print("The name is present")
 
 
#try:
#     number = int(input("Enter a number: "))
#     for i in range(1, 11):
#         print(f"{number} * {i} = {number * i}")
# except ValueError:
#     print("\n\033[38;5;1mPlease enter a valid number!\033[0m")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# def encode_secret_language(text):
#   vowels = "aeiou"
#   encoded_text = ""
#   for char in text:
#     if char.lower() in vowels:
#       encoded_text += char + "p" + char
#     else:
#       encoded_text += char
#   return encoded_text

# text = input("Enter the text: ")
# encoded_text = encode_secret_language(text)
# print("Encoded text:", encoded_text)


# NumberOfLetters = 0
# NumberOfDigits = 0
# NumberOfWords=0

# text = input("Enter a text of  numbers : ")
# for x in text:
#     x=x.lower()
#     if x >= 'a' and x <= 'z':
#          NumberOfLetters = NumberOfLetters + 1
   

#     elif x >= '0' and x <= '9':
#           NumberOfDigits = NumberOfDigits + 1
   

#     elif x == ' ':
#           NumberOfWords = NumberOfWords + 1

# print(NumberOfLetters)     
   
# print(NumberOfDigits) 
        
# print(NumberOfWords+1)     
# import random

# def start_game():
#     guess = random.randint(1, 100)
#     attempts = 0

#     print("Welcome to the Guessing Game!")
#     print("Try to guess the number between 1 and 100.")
    
#     while True:
#         try:
#             number = input("Enter the number (or type 'hint' for a hint, or 'exit' to quit): ").strip().lower()

#             if number == 'exit':
#                 print("Thanks for playing! Goodbye!")
#                 break
            
#             if number == 'hint':
#                 if '7' in str(guess):
#                     print("Hint: The number contains the digit 7, like a famous jersey number!")
#                 elif guess % 2 == 0:
#                     print("Hint: The number is even.")
#                 else:
#                     print("Hint: The number is odd.")
#                 continue

#             number = int(number)
#             attempts += 1

#             if number == guess:
#                 print(f"🎉 You have guessed the correct number {guess}!")
#                 print(f"You have guessed the number in {attempts} attempts.")
#                 play_again = input("Would you like to play again? (yes/no): ").strip().lower()
#                 if play_again == 'yes':
#                     start_game()
#                 else:
#                     print("Thanks for playing! Goodbye!")
#                     break
#             elif number > guess:
#                 print("📉 You have guessed a greater number. Try a smaller one.")
#             else:
#                 print("📈 You have guessed a smaller number. Try a larger one.")
#         except ValueError:
#             print("\033[91mPlease enter a valid number!\033[0m")

# start_game()


# import os

# def get_files(extension):
#     return sorted([f for f in os.listdir() if f.endswith(f".{extension}")])

# def rename_files(files, extension):
#     for i, file in enumerate(files, start=1):
#         new_name = f"{i}.{extension}"
#         os.rename(file, new_name) 
#         print(f"Renamed File Name -> {file} ->  New Renamed File Name {new_name}")

# ext = input("Enter file extension (e.g., png, gif,webp,jpg): ")
# files = get_files(ext)
# rename_files(files, ext)

# continue__="yes"
# import time
# while continue__=="yes":
#   try:
#     num = int(input("Enter the number: "))
#     for i in range(1, 11):
#       time.sleep(1)
#       print(f"{num} * {i} = {i * num}")
#     continue_=input("Do you want to continue? (yes/no): ").strip().lower()
#     if continue__ not in ["yes", "y"]:
#       print("Thanks for using the multiplication table!")
#     break

        

      
      
#   except ValueError:
#     print("Please enter a valid number")
#   except Exception as e:
#     print(f"An unexpect ed error occurred: {e}")
    




# import math
# print(math.sqrt(24))
# print(math.floor(4.5))






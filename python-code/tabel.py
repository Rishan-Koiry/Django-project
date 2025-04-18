import tkinter as tk
import random
from tkinter import messagebox
# import py33tsx3 
import random
import time
import pyttsx3
root = tk.Tk()
root.title("Car Game")
root.resizable(False, False)
root.config(bg="lightgray")

# Constants
WIDTH, HEIGHT = 600, 400
CAR_WIDTH, CAR_HEIGHT = 50, 100
SPEED = 20
ENEMY_CAR_WIDTH, ENEMY_CAR_HEIGHT = 50, 100
ENEMY_SPEED = 5
LEVEL_UP_SCORE = 10
NUM_ENEMY_CARS = 1

def reset_user_car():
    global user_car_x, user_car_y
    user_car_x = WIDTH // 2 - CAR_WIDTH // 2
    user_car_y = HEIGHT - CAR_HEIGHT - 20
    canvas.coords(user_car, user_car_x, user_car_y)

# Create canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

# Load images
user_car_image = tk.PhotoImage(file="user_car.png")
enemy_car_image = tk.PhotoImage(file="enemy_car.png")

# Draw user car
user_car_x, user_car_y = WIDTH // 2 - CAR_WIDTH // 2, HEIGHT - CAR_HEIGHT - 20
user_car = canvas.create_image(user_car_x, user_car_y, image=user_car_image)

# Enemy cars list
enemy_cars = []

def spawn_enemy():
    enemy_car_x = random.randint(0, WIDTH - ENEMY_CAR_WIDTH)
    enemy_car_y = random.randint(-HEIGHT, -ENEMY_CAR_HEIGHT)
    enemy_car = canvas.create_image(enemy_car_x, enemy_car_y, image=enemy_car_image)
    enemy_cars.append((enemy_car, enemy_car_x, enemy_car_y))

# Initial enemy spawn
for _ in range(NUM_ENEMY_CARS):
    spawn_enemy()

# Score and level
score, level = 0, 1
score_text = canvas.create_text(10, 10, anchor="nw", text=f"Score: {score}", font=("Arial", 16), fill="white")
level_text = canvas.create_text(10, 30, anchor="nw", text=f"Level: {level}", font=("Arial", 16), fill="white")

def move_left(event=None):
    global user_car_x
    if user_car_x - SPEED >= 0:
        user_car_x -= SPEED
        canvas.coords(user_car, user_car_x, user_car_y)

def move_right(event=None):
    global user_car_x
    if user_car_x + SPEED + CAR_WIDTH <= WIDTH:
        user_car_x += SPEED
        canvas.coords(user_car, user_car_x, user_car_y)

def check_collision():
    for enemy_car, enemy_car_x, enemy_car_y in enemy_cars:
        if (user_car_x < enemy_car_x + ENEMY_CAR_WIDTH and
            user_car_x + CAR_WIDTH > enemy_car_x and
            user_car_y < enemy_car_y + ENEMY_CAR_HEIGHT and
            user_car_y + CAR_HEIGHT > enemy_car_y):
            return True
    return False

def move_enemy_cars():
    global score, level, ENEMY_SPEED, NUM_ENEMY_CARS
    for i, (enemy_car, enemy_car_x, enemy_car_y) in enumerate(enemy_cars):
        enemy_car_y += ENEMY_SPEED
        if enemy_car_y > HEIGHT:
            enemy_car_y = random.randint(-HEIGHT, -ENEMY_CAR_HEIGHT)
            enemy_car_x = random.randint(0, WIDTH - ENEMY_CAR_WIDTH)
            score += 1
            if score % LEVEL_UP_SCORE == 0:
                level += 1
                ENEMY_SPEED += 1
                NUM_ENEMY_CARS  += 1
                if level > 1:  # After level 2, increase the number of enemy cars
                    NUM_ENEMY_CARS += 1
                    spawn_enemy()
                canvas.itemconfig(level_text, text=f"Level: {level}")
            canvas.itemconfig(score_text, text=f"Score: {score}")
        canvas.coords(enemy_car, enemy_car_x, enemy_car_y)
        enemy_cars[i] = (enemy_car, enemy_car_x, enemy_car_y)
    if check_collision():
        game_over()
    else:
        root.after(30, move_enemy_cars)

def game_over():
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", font=("Arial", 24), fill="red")
    messagebox.showinfo("Game Over", f"Game Over! Your final score is {score}")
    restart_button = tk.Button(root, text="Restart", command=restart_game)
    restart_button.pack()

def restart_game():
    global score, level, ENEMY_SPEED, NUM_ENEMY_CARS, enemy_cars
    score, level, ENEMY_SPEED = 0, 1, 5
    NUM_ENEMY_CARS = 1
    canvas.delete("all")
    enemy_cars.clear()
    for _ in range(NUM_ENEMY_CARS): 
        spawn_enemy()
    reset_user_car()
    move_enemy_cars()
    canvas.create_text(10, 10, anchor="nw", text=f"Score: {score}", font=("Arial", 16), fill="white")
    canvas.create_text(10, 30, anchor="nw", text=f"Level: {level}", font=("Arial", 16), fill="white")

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
move_enemy_cars()
root.mainloop()



# for i in range(1, 11):
#     result = f"{number} x {i} = {number * i}"
#     print(result)
#     engine.say(result)
# engine.runAndWait()
# engine = pyttsx3.init()
# engine.say("1301592834942972055182648307417315364538725075960067827915311484722452340966317215805106820959190833309704934346517741237438752456673499160125624414995891111204155079786496")
# engine.runAndWait()
# engine.say("Hello World")
# print(round(4.040448484))
# i=1
# while True:
#     i+=1
#     print(i)
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# print(f"Here is the sum of {num1} + {num2} : {(num1) + int(num2)}")
# gpa = float(input("Enter your GPA: "))
# gpa = round(gpa)
# print(f"Your GPA is {gpa}")


# for i in range(3):
#     print(i)





# 😎আচ্ছা, আমি সহজ করে বুঝিয়ে দিচ্ছি! 😊

# তুমি এমন একটা প্রোগ্রাম লিখবে যেখানে একজন ইউজারকে একটা নির্দিষ্ট সংখ্যা অনুমান করতে হবে।

# কিভাবে করবে?
# 1️⃣ একটা গোপন সংখ্যা ঠিক করো (যেমন ৫)।
# 2️⃣ ইউজারের কাছ থেকে একটা সংখ্যা ইনপুট নাও।
# 3️⃣ while loop ব্যবহার করো, যাতে ইউজার যতক্ষণ পর্যন্ত সঠিক সংখ্যা না বলে, ততক্ষণ প্রোগ্রাম চলতে থাকে।
# 4️⃣ if-else শর্ত ব্যবহার করো—

# যদি ইউজার কম বলে, তাহলে প্রিন্ট করো: "কম হয়ে গেছে! আবার চেষ্টা করো!"
# যদি ইউজার বেশি বলে, তাহলে প্রিন্ট করো: "বেশি হয়ে গেছে! আবার চেষ্টা করো!"
# যদি ইউজার ঠিক বলে, তাহলে প্রিন্ট করো: "সঠিক! তুমি পেয়ে গেছো!" এবং লুপ বন্ধ করো।
# এখন তুমি এটা নিজে কোড করার চেষ্টা করো! ✨ যদি কোথাও সমস্যা হয়, আমাকে বলো! 😃
# import random

# print("\033[1;34mWelcome to the number guessing game Aditro FF 😎!\033[0m")

# level = int(input("Guess a number between 1 to 100: "))
# attempts = int(input("Enter the number of attempts you want: "))
# print(f"\033[1;32mYou have {attempts} attempts to guess the number and you also chose to guess number between 1 to {level}\033[0m")

# hide_number = random.randint(1, level)
# flag = True

# while flag:
#   if attempts == 0:
#     print(f"\033[1;31mSorry, you have no attempts left! The number was {hide_number}\033[0m")
#     break
#   user_input = int(input("Enter a number: "))
#   if user_input < hide_number:
#     print("\033[1;33mToo low! Try again.\033[0m")
#     attempts -= 1
#     print(f"\033[1;32mRemaining Attempts: {attempts}\033[0m")
#   elif user_input > hide_number:
#     print("\033[1;33mToo high! Try again.\033[0m")
#     attempts -= 1
#     print(f"\033[1;32mRemaining Attempts: {attempts}\033[0m")
#   else:
#     print("\033[1;32mCorrect! You found it! 😱 🤯 🥳\033[0m")
#     print(f"\033[1;32mYour Remaining Attempts: {attempts}\033[0m")
#     flag = False













 



















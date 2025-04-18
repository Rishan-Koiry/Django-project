import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
os.system("")

import random
import time

def clear_terminal():
    print("\033c", end="")

def get_fruit_hint(fruit):
    hints = {
        "apple": "🍏 This fruit keeps the doctor away!",
        "banana": "🍌 Monkeys love this yellow fruit!",
        "cherry": "🍒 A small red fruit often used in desserts!",
        "date": "🌴 A sweet fruit popular in the Middle East!",
        "elderberry": "🫐 A dark berry known for boosting immunity!",
        "fig": "🍈 A soft fruit full of energy!",
        "grape": "🍇 Used to make juice and wine!",
        "honeydew": "🍈 A sweet green melon!",
        "jackfruit": "🍈 The largest fruit with a strong aroma!",
        "kiwi": "🥝 Brown and fuzzy outside, green inside!",
        "lemon": "🍋 A sour fruit used in lemonade!",
        "mango": "🥭 Known as the 'King of Fruits'!",
        "nectarine": "🍑 Looks like a peach but has smooth skin!",
        "orange": "🍊 A citrus fruit rich in Vitamin C!",
        "papaya": "🍈 A tropical fruit with black seeds inside!",
        "quince": "🍏 Often used in jams!",
        "raspberry": "🍇 A red fruit with a sweet-tart taste!",
        "strawberry": "🍓 A fruit with seeds on the outside!",
        "tangerine": "🍊 A small, easy-to-peel orange-like fruit!",
        "watermelon": "🍉 A juicy summer fruit with a green rind!"
    }
    return hints.get(fruit, "🍍 A delicious fruit!")

def play_game():
    clear_terminal()
    print("🎉 Welcome to RK Fruit Guessing Game! 🎉")
    time.sleep(5)
    clear_terminal()

    print("Your task is to guess the name of a fruit.")
    time.sleep(5)
    clear_terminal()
    print("You have 10 lives. Each wrong guess costs 1 life.")
    time.sleep(5)
    clear_terminal()
    print("Let’s begin With RK! 🍎🍌🍉")
    time.sleep(3)
    clear_terminal()

    fruits = random.choice([
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
        "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine",
        "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"
    ])

    lives = 10
    guessed_letters = set()
    fruit_letters = set(fruits)

    while lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in fruit_letters:
            print("✅ Correct guess!")
        else:
            lives -= 1
            print(f"❌ Wrong guess! You have {lives} lives left.")
            print(f"🔎 Hint: {get_fruit_hint(fruits)}")

        current_progress = [letter if letter in guessed_letters else '_' for letter in fruits]
        print("Current progress:", ' '.join(current_progress))

        if set(current_progress) == fruit_letters:
            print(f"🎉 Congratulations! You guessed the fruit: {fruits}!")
            break
    else:
        print(f"😢 Sorry, you lost! The correct fruit was: {fruits}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
     
        play_game()
    else:
        print("👋 Goodbye! Thanks for playing RK Fruit Guessing Game!")

play_game()

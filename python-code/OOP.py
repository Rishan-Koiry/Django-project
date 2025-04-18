# import tkinter as tk
# # import random


# class Calculator:
#   def __init__(self, root):
#     self.root = root
#     self.root.title("Calculator")
#     self.expression = ""
    
#     self.input_text = tk.StringVar()
#     self.input_frame = tk.Frame(self.root)
#     self.input_frame.pack()
    
#     self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
#     self.input_field.grid(row=0, column=0)
#     self.input_field.pack(ipady=10)
    
#     self.buttons_frame = tk.Frame(self.root)
#     self.buttons_frame.pack()
    
#     self.create_buttons()
    
#   def create_buttons(self):
#     buttons = [
#       '7', '8', '9', '/', 
#       '4', '5', '6', '*', 
#       '1', '2', '3', '-', 
#       'C', '0', '=', '+',
#       "" , "",  "",   '%'
#     ]
    
#     row = 0
#     col = 0
#     for button in buttons:
#       action = lambda x=button: self.click_event(x)
#       tk.Button(self.buttons_frame, text=button, width=10, height=3, command=action).grid(row=row, column=col)
#       col += 1
#       if col > 3:
#         col = 0
#         row += 1
  
#   def click_event(self, key):
#     if key == '=':
#       try:
#         result = str(eval(self.expression))
#         self.input_text.set(result)
#         self.expression = result
#       except:
#         self.input_text.set("Error")
#         self.expression = ""
#     elif key == 'C':
#       self.expression = ""
#       self.input_text.set("")
#     else:
#       self.expression += str(key)
#       self.input_text.set(self.expression)

# if __name__ == "__main__":
#   root = tk.Tk()
#   calculator = Calculator(root)
#   root.mainloop()
# class SnakeGame:
#   def __init__(self, root):
#     self.root = root
#     self.root.title("Snake Game")
#     self.root.resizable(False, False)
    
#     self.canvas = tk.Canvas(self.root, bg="black", height=400, width=400)
#     self.canvas.pack()
    
#     self.snake = [(20, 20), (20, 30), (20, 40)]
#     self.food = self.create_food()
#     self.direction = "Down"
    
#     self.root.bind("<KeyPress>", self.change_direction)
#     self.update_snake()
#     self.run_game()
  
#   def create_food(self):
#     x = random.randint(0, 19) * 20 
#     y = random.randint(0, 19) * 20
#     return (x, y)
  
#   def change_direction(self, event):
#     if event.keysym in ["Up", "Down", "Left", "Right"]:
#       self.direction = event.keysym
  
#   def update_snake(self):
#     self.canvas.delete("all")
#     for segment in self.snake:
#       self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")
#     self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")
  
#   def run_game(self):
#     head_x, head_y = self.snake[0]
#     if self.direction == "Up":
#       head_y -= 20
#     elif self.direction == "Down":
#       head_y += 20
#     elif self.direction == "Left":
#       head_x -= 20
#     elif self.direction == "Right":
#       head_x += 20
    
#     new_head = (head_x, head_y)
    
#     if new_head in self.snake or not (0 <= head_x < 400 and 0 <= head_y < 400):
#       self.game_over()
#       return
    
#     self.snake = [new_head] + self.snake[:-1]
    
#     if new_head == self.food:
#       self.snake.append(self.snake[-1])
#       self.food = self.create_food()
    
#     self.update_snake()
#     self.root.after(100, self.run_game)
  
#   def game_over(self):
#     self.canvas.create_text(200, 200, text="Game Over", fill="red", font=('Arial', 24))

# if __name__ == "__main__":
#   root = tk.Tk()
#   game = SnakeGame(root)
#   root.mainloop()


# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# print(f"here is your sum of {num1} + {num2} : {num1
# +num2}")


# print("Rishan Koiry")
# print("Hello World")

# class account:
#   def __init__(self, name, balance):
#     self.name = name
#     self.balance = balance

#   def deposit(self, amount):
#       if amount > 0:
#         self.balance += amount
#         return True
#       return False
  
#   def withdraw(self, amount):
#       if 0 < amount <= self.balance:
#         self.balance -= amount
#         return True
#       return False
  
#   def get_balance(self):
#       return self.balance
  
#   def __str__(self):
#       return f"Account holder: {self.name}, Balance: {self.balance}"
# __init__ = account("John", 100)
# # print(__init__)
# print(__init__.deposit(50))
# print(__init__.withdraw(10))
# print(__init__.get_balance())

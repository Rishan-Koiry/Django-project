# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time
# os.environ['PATH'] += ":/Users/rupok/Desktop/Python-Revise/chromedriver-mac-x64"
# driver = webdriver.Chrome()
# driver.get("https://rupok-koiry.vercel.app/")
# driver.implicitly_wait(10) 
# input_name = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "name"))
# )
# input_email = driver.find_element(By.ID, "email")
# input_number = driver.find_element(By.ID, "number")
# input_subject = driver.find_element(By.ID, "subject")
# input_message = driver.find_element(By.ID, "message")
# input_name.send_keys("Rishan Koiry")
# input_email.send_keys("rishankoiry@gmail.com")
# input_number.send_keys("01700000000")
# input_subject.send_keys("Test Subject")
# input_message.send_keys("hi how's going  ")
# button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-center.block.gradient-transition.rounded-md.bg-default.lg\\:text-base.text-sm.px-4.py-2.lg\\:px-6.lg\\:py-3.text-primary.shadow-default.flex.items-center.justify-center.gap-3.border-2.border-primary.font-medium.outline-none"))
# )
# button.click()
# WebDriverWait(driver, 20)
# time.sleep(100)  
# driver.quit()
# ✅ Step 1: Dictionary তৈরি করা



# import turtle

# # Screen setup
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Turtle Flower")

# # Create a turtle object
# flower = turtle.Turtle()
# flower.shape("turtle")
# flower.speed(10)

# # Function to draw a petal
# def draw_petal():
#     flower.color("yellow")
#     flower.circle(100, 60)  # Draw a part of the circle for a petal
#     flower.left(120)
#     flower.circle(100, 60)  # Draw another part of the circle for a petal
#     flower.left(120)

# # Draw flower
# def draw_flower():
#     for _ in range(6):  # Flower has 6 petals
#         draw_petal()
#         flower.left(60)  # Rotate by 60 degrees for the next petal

# # Draw the stem and leaves
# def draw_stem():
#     flower.color("green")
#     flower.right(90)
#     flower.forward(200)
#     flower.right(30)
#     flower.forward(50)
#     flower.backward(50)
#     flower.left(60)
#     flower.forward(50)
#     flower.backward(50)
#     flower.right(30)
#     flower.backward(200)

# # Set the turtle position for the flower
# flower.penup()````````````
# flower.goto(10, -100)
# flower.pendown()

# # Draw the flower
# draw_flower()

# # Draw the stem and leaves
# draw_stem()

# # Hide the turtle after drawing
# flower.hideturtle()

# # Finish
# screen.mainloop()




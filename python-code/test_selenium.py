from RK import webdriver
import os

# Add chromedriver directory to PATH
os.environ['PATH'] += ":/Users/rupok/Desktop/Python-Revise/chromedriver-mac-x64"

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com/")

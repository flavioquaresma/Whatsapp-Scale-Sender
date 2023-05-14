import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import quote
import pyautogui

# Path to your Excel file
excel_file = '/Users/flavioquaresma/Documents/Projects/Whatsapp Scale Sender/Database.xlsx'

# Load the Excel file using pandas
df = pd.read_excel(excel_file)

# Initialize the Chrome WebDriver (make sure you have Chrome and the corresponding WebDriver installed)
driver = webdriver.Chrome()

# Open Google Chrome and go to WhatsApp Web
driver.get('https://web.whatsapp.com')
time.sleep(10)

# Iterate over the rows of the DataFrame
for row in range(len(df)):
    # Get the URL from the respective column (assuming it is in column C)
    url = df.loc[row][2]

    # Open the provided URL
    driver.get(url)
    time.sleep(5)

    # Simulate pressing the "Return" key
    pyautogui.press('enter')
    time.sleep(5
               )


# Close the WebDriver
driver.quit()
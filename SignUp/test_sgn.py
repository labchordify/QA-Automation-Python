import time
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def setup():

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    """Fixture to initialize and teardown the WebDriver instance"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_sgn(setup):
    driver = setup
    driver.get('https://www.spotify.com/signup/')

    driver.save_screenshot("screenshots/sgnpage1.png")

    # Step 1: Fill out email and click Next
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys("griggs22624@9q1i.cse445.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"__next\"]/main/main/section/div/form/button").click()

    # Add a short sleep to ensure the next page is loaded
    driver.save_screenshot("screenshots/sgnpage2.png")
    time.sleep(2)

    # Step 2: Fill out password and click Next
    password_input = driver.find_element(By.ID, "new-password")
    password_input.send_keys("YourPassword123")
    time.sleep(3)
    
    driver.save_screenshot("screenshots/sgnpage2.png")
    driver.find_element(By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]").click()

    # Add another short sleep
    # driver.save_screenshot("screenshots/sgnpage3.png")
    time.sleep(2)

    # Step 3: Fill out name, date of birth, and gender and click Next
    name_input = driver.find_element(By.ID, "displayName")
    name_input.send_keys("Vimla Kumari")

    dob_year_input = driver.find_element(By.ID, "year")
    dob_year_input.send_keys("1990")

    dob_month_dropdown = driver.find_element(By.ID, "month")
    dob_month_dropdown.send_keys("January")

    dob_day_input = driver.find_element(By.ID, "day")
    dob_day_input.send_keys("1")

    driver.execute_script("window.scrollBy(0, 500);")
    
    gender_female_radio = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[2]/label/span[1]")
    if not gender_female_radio.is_selected():
        gender_female_radio.click()

    time.sleep(3)
    
    driver.save_screenshot("screenshots/sgnpage3.png")

    driver.find_element(By.XPATH, "//*[@id=\"__next\"]/main/main/section/div/form/div[2]/button").click()

   
    # Add a final short sleep
    time.sleep(2)
    driver.save_screenshot("screenshots/sgnpage4.png")
   

    # Assertion: Check if signup is successful
    # assert "confirmation" in driver.current_url

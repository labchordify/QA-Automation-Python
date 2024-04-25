import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def setup():

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    # Initialize ChromeDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_forgot_password(setup: WebDriver):
    driver = setup
    # Launch the browser and open Spotify website
    driver.get("https://www.spotify.com/en/login")

    # Click on the Login button
    # login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/button/span[1]/span")
    # login_button.click()
    driver.execute_script("window.scrollBy(0, 500);")
    driver.save_screenshot("screenshots/step1.png")
    # Click on the Forgot your password? link
    forgot_password_link = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[5]/a")
    forgot_password_link.click()

    # Enter email address
    email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/form/div/input")
    email_input.send_keys("example@gmail.com")

    driver.save_screenshot("screenshots/step2.png")

    time.sleep(10)
    # Click on the Send button
    send_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/form/button")
    send_button.click()

    # driver.save_screenshot("screenshots/step3.png")

    # Wait for a while to allow the email to be sent (you may adjust the time based on your email provider)
    time.sleep(10)

    # Check for the success message
    # success_message = driver.find_element(By.XPATH, "//div[contains(text(),'Email sent')]")
    # assert success_message.is_displayed(), "Email sent success message not displayed"

    # Additional assertions or verifications can be added here as needed

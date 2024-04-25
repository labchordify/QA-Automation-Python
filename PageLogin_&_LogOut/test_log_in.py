#Test Login and Logout Automation
#this code runs successfully
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()
    # Maximize the browser window
    driver.maximize_window()
    # Navigate to the website
    driver.get("https://accounts.spotify.com/en/login")
    yield driver
    # Close the browser session
    driver.quit()

def test_log_in(setup: WebDriver):
    # Open Spotify login page
    driver = setup
    
    # Wait for username input to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
    
    # Find username and password input elements
    username_input = driver.find_element(By.ID, "login-username")
    password_input = driver.find_element(By.ID, "login-password")
    
    # Enter username and password
    username_input.send_keys("xyz@gmai.com")
    password_input.send_keys("yourPassword123")
    
    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/button/span[1]/span")
    login_button.click()
    
    # Wait for account settings link to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "account-settings-link")))
    
    # Click on account settings link
    driver.find_element(By.ID, "account-settings-link").click()
    
    # Wait for profile dropdown to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/header/div/nav/ul/li[5]/button/div[2]/span")))
    
    # Click on the profile dropdown
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/header/div/nav/ul/li[5]/button/div[2]/span").click()
    
    # Wait for logout button to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/header/div/nav/ul/li[5]/div/ul/li[2]/a")))
    
    # Click on the "Log Out" button in the dropdown menu
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/header/div/nav/ul/li[5]/div/ul/li[2]/a").click()

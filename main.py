import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import shutil

# Constants
PATH = "/home/ams/Documents/chromedriver"
LIMIT = 100

options = Options()
options.binary_location = "/usr/lib/brave-bin/brave"
driver = webdriver.Chrome(options = options,service=Service(ChromeDriverManager().install()))
print("Starting....")

# Maximize the screen
driver.maximize_window()

# scrolls to the end of the search results
def scroll_to_bottom():
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

def make_new_dir(dir_name):
    cwd = os.getcwd()
    # print(cwd) 
    new_dir_path = os.path.join(cwd,dir_name)
    if os.path.exists(new_dir_path):
        shutil.rmtree(new_dir_path)
    os.mkdir(new_dir_path)
    print("Directory '% s' created" % dir_name)
    return new_dir_path


def get_images_from_google():
    # change the query here to whathever you want to search
    # you can use google search tricks here for more accurate results
    # use "" (double-quotes) to search for only the exact keyword
    query = '"mohanlal"'
    driver.get('https://images.google.com/')

    # sending query in the google image's search box
    search_box = driver.find_element(By.XPATH,'//*[@id="sbtc"]/div/div[2]/input')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    if '"' in query:
        new_dir_name = query.strip('"') 
        new_dir_path = make_new_dir(new_dir_name)
    else:
        new_dir_path = make_new_dir(query)
    
    scroll_to_bottom()
    

    for i in range(LIMIT):
        try:
            img = driver.find_element(By.XPATH,f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
            img.click()
            full_img =  driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
            time.sleep(2)
            # Enter the location of folder in which the images will be saved
            # Each new screenshot will automatically have its name updated
            full_img.screenshot(f"{new_dir_path}/{query}-{i}.png")
    
            # Just to avoid unwanted errors
            time.sleep(0.2)
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    get_images_from_google()
    driver.quit()

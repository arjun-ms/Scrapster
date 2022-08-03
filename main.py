
def scroll_to_bottom(nooftimes):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    html = driver.find_element(By.TAG_NAME,'html')
    
    for i in range(nooftimes):
        html.send_keys(Keys.END)
        time.sleep(2)
   

def make_new_dir(query):
    cwd = os.getcwd()
    print(cwd) 
    new_dir_path = os.path.join(cwd,query)
    if os.path.exists(new_dir_path):
        shutil.rmtree(new_dir_path)
    os.mkdir(new_dir_path)
    print("Directory '% s' created" % query)
    return new_dir_path


def get_images_from_google():
    
    NO_OF_TIMES = 2
    START_INDEX = 265
    
    query = '"mammootty"'
    driver.get('https://images.google.com/')

    search_box = driver.find_element(By.XPATH,'//*[@id="sbtc"]/div/div[2]/input')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    new_dir_name = query.strip('"') 
    new_dir_path = make_new_dir(new_dir_name)
    
    scroll_to_bottom(NO_OF_TIMES)
    
    # for loading whole page
    time.sleep(5)
    
    for i in range(START_INDEX,LIMIT):
        try:
            
            img = driver.find_element(By.XPATH,f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
            img.click()
            full_img =  driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
            time.sleep(2)
            # Enter the location of folder in which
            # the images will be saved
            full_img.screenshot(f"{new_dir_path}/{query}-{i}.png")
            # Each new screenshot will automatically
            # have its name updated
    
            # Just to avoid unwanted errors
            time.sleep(0.2)
            print(f"{query}-{i}.png downloaded")
        except:
            print("Cant find Xpath")
            # if we can't find the XPath of an image,
            # we skip to the next image
            continue
    
if __name__ == "__main__":
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
    
    PATH = "/home/ams/Documents/pyscraper/chromedriver"
    LIMIT = 10000

    options = Options()
    options.binary_location = "/usr/lib/brave-bin/brave"
    driver = webdriver.Chrome(options = options,service=Service(ChromeDriverManager().install()))
    print("Starting....")

    # Maximize the screen
    driver.maximize_window()

    get_images_from_google()
    driver.quit()

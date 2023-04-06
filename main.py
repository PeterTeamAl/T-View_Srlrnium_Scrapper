from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time


# url. TradingView
url = "https://ru.tradingview.com/chart/"

# options initializing
options = webdriver.ChromeOptions()

# initializing driver
driver = webdriver.Chrome(
    executable_path=r'D:\TradibgView_Selenium_Scrapper\chromedriver.exe',
    options=options
)


# Then we have 2 variants. We may just take a screenshot of all page or click a special screenshot button.

# 1st variant.
def make_screen():
    try:
        driver.get(url)
        print("I'm in!")
        time.sleep(3)
        td = str(datetime.date.today())
        driver.get_screenshot_as_file(f"media/{td}.png")
        # print(datetime.date.today())
        # print("Job's done, Sir!")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# 2nd variant
def get_picture():
    try:
        driver.get(url)
        time.sleep(5)
        screen_button = driver.find_element(By.ID, "header-toolbar-screenshot")
        screen_button.click()
        print("1 click")
        time.sleep(5)
        print("Try to find...")
        new_button = driver.find_elements(By.CLASS_NAME, 'item-RhC5uhZw')[3]
        print("Found")
        new_button.click()
        driver.maximize_window()
        print("2 click")
        time.sleep(5)
        td = str(datetime.date.today())
        driver.switch_to.window(driver.window_handles[1])
        driver.get_screenshot_as_file(f"media1/{td}.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



if __name__ == "__main__":
    # make_screen()
    # get_picture()
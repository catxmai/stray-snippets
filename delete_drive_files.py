from utils import *
from get_video_info import *
from google_controls import *

# Orinally in YouTubeAds repo


def click_show_more_button(driver):
    # button = driver.find_element(By.CSS_SELECTOR,
                                #  '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.ksBjEc.lKxP2d.LQeN7.oZrGf')
    button = driver.find_element(By.CSS_SELECTOR, "span.VfPpkd-vQzf8d[jsname='V67aGc']")
    jsclick(driver, button)

def click_select_showing_button(driver):
    # show_button = driver.find_element(By.CSS_SELECTOR,
    #                                   ".VfPpkd-MPu53c.VfPpkd-MPu53c-OWXEXe-dgl2Hf.VfPpkd-wZVHld-vqLbZd-oKdM2c-MPu53c.Ne8lhe.swXlm.az2ine")
    show_button = driver.find_element(By.CSS_SELECTOR, "input.VfPpkd-muHVFf-bMcfAe[type='checkbox']")
    jsclick(driver, show_button)

def click_delete_button(driver):
    delete_button = driver.find_element(By.CSS_SELECTOR,
                                        '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.LQeN7.EYdxJe')
    jsclick(driver, delete_button)

def click_understand_popup(driver):
    button = driver.find_element(
        By.CSS_SELECTOR,
        '.VfPpkd-MPu53c.VfPpkd-MPu53c-OWXEXe-dgl2Hf.Ne8lhe.swXlm.az2ine.VfPpkd-MPu53c-OWXEXe-mWPk3d > input')
    jsclick(driver, button)

def click_delete_popup(driver):
    delete_button = driver.find_element("xpath", '//span[text()="Permanently delete"]')
    jsclick(driver, delete_button)

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

def get_scroll_height(driver) -> int:
    return driver.execute_script("return document.documentElement.scrollHeight") 

def delete_on_page(driver):

    time.sleep(2)
    click_select_showing_button(driver)
    time.sleep(2)
    click_delete_button(driver)
    time.sleep(2)
    click_understand_popup(driver)
    time.sleep(2)
    click_delete_popup(driver)



if __name__ == "__main__":


    user = ""
    driver = create_driver(f"configs/config_{user}.json", headless=False)
    driver.get("https://one.google.com/storage/management/drive/large")
    driver_wait(driver, 5, (By.CSS_SELECTOR, '.VfPpkd-vQzf8d'))

    for _ in range(350):
        try:
            delete_on_page(driver)
            time.sleep(15)
        except NoSuchElementException:
            driver.get("https://one.google.com/storage/management/drive/large")
        



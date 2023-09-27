import os
import types
import typing
import time
import Booking.contant as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Chrome):

    def __init__(self,driver_path = r"C:/SeleniumDrivers/chromedriver-win32",teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self):
        self.get(const.BASE_URL)
        
        #wait for the element to be clickable
        try:
            # Wait for the button to be clickable
            ele = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="b2indexPage"]/div[17]/div/div/div/div[1]/div[1]/div/button')))
            ele.click()
        except Exception as e:
            print("Error:", e)


    def change_currency(self,currency):
        myEle = self.find_element("xpath",'//*[@id="b2indexPage"]/div[2]/div/header/nav[1]/div[2]/span[1]/button')
        myEle.click()

        try:
            ele = WebDriverWait(self,10).until(
                EC.element_to_be_clickable((By.XPATH,f"//div[text()='{currency}']")))
            ele.click()
        except Exception as e:
            print("Error",e)
        # time.sleep(3)
    
    def destination(self,dest):
        ele  = self.find_element("id",":re:")
        ele.clear()
        ele.send_keys(dest)
        time.sleep(3)

        place_select = self.find_element("xpath",'//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/ul/li[1]/div/div/div/div[1]')

        place_select.click()

    def checkDate(self,check_inDate_,check_outDate):

        check_in_date_ele = self.find_element(
            "css selector",
            f'span[data-date = "{check_inDate_}"]'
        )
        check_in_date_ele.click()

        check_out_date_ele = self.find_element(
            "css selector",
            f'span[data-date = "{check_outDate}"]'
            )
        check_out_date_ele.click()

        # time.sleep(3)

    def adult(self,count = 1):
        input_ele = self.find_element("css selector", 'button[data-testid="occupancy-config"]')
        input_ele.click()
        # time.sleep(3)

        # will decrement till 1
        decrement_ele = self.find_element("xpath",
                                              '//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]')
        while True:      
            decrement_ele.click()

            #To break the loop we need to check the value
            adultCount = self.find_element("id","group_adults")
            count_ele = adultCount.get_attribute("value")
            if int(count_ele) == 1:
                break
        
        increment_ele = self.find_element("xpath",'//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')

        for _ in range(count-1):
            increment_ele.click()

        # time.sleep(3)

    def searchEle(self):
        search_ele = self.find_element("css selector",'button[type = "submit"]')
        search_ele.click()

        

  
        


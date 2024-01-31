
from selenium.webdriver.common.by import By

class flight_booking_page:
    button_login_popup_close_xpath="//span[@role='presentation']"
    link_flight_xpath="//p[normalize-space()='Flights']"
    textbox_from_xpath='//div[@class="sc-12foipm-34 iHoHRr"]//div[@class="sc-12foipm-35 kdxZzw"]'
    textbox_from_send_xpath="//input[@type='text']"
    list_from_send_xpath="//ul[@id='autoSuggest-list']//li"
    textbox_to_xpath = "//div[@class='sc-12foipm-38 dAUhfz']"
    textbox_to_send_xpath = "//input[@type='text']"
    list_to_send_xpath = "//ul[@id='autoSuggest-list']//li"
    textbox_departure_click_xpath="(//div[@class='sc-12foipm-34 iHoHRr'])[3]"
    selectdate_xpath="//div[@aria-label='Thu Nov 23 2023']//p[@class='fsw__date'][normalize-space()='23']"
    button_done_xpath="//span[normalize-space()='Done']"
    button_searchFlights_xpath="//span[@class='sc-12foipm-85 fUaVPB']"

    def __init__(self,driver):
        self.driver=driver

    def clickLoginCloseWindow(self):
        self.driver.find_element(By.XPATH,self.button_login_popup_close_xpath).click()

    def clickFlightsOption(self):
        self.driver.find_element(By.XPATH, self.link_flight_xpath).click()

    def setFromDestination(self,fromDestination):
        self.driver.find_element(By.XPATH,self.textbox_from_xpath).click()
        # self.driver.find_element(By.XPATH,self.text_from_click_xpath).click
        # self.driver.find_element(By.XPATH,self.text_from_click_xpath).clear
        self.driver.find_element(By.XPATH,self.textbox_from_send_xpath).send_keys(fromDestination)
        list_from_elements = self.driver.find_elements(By.XPATH, self.list_from_send_xpath)
        for list in list_from_elements:
            print(list.text)
            if "Bengaluru" in list.text:
                list.click()
                break

    def setToDestination(self,toDestination):
        self.driver.find_element(By.XPATH, self.textbox_to_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_to_send_xpath).send_keys(toDestination)
        list_to_elements = self.driver.find_elements(By.XPATH, self.list_to_send_xpath)
        for li in list_to_elements:
            print(li.text)
            if "Dubai" in li.text:
                li.click()
                break

    def setDepartureDate(self):
        self.driver.find_element(By.XPATH,self.textbox_departure_click_xpath).click()
        self.driver.find_element(By.XPATH, self.selectdate_xpath).click()

    def clickButtonDone(self):
        self.driver.find_element(By.XPATH, self.button_done_xpath).click()

    def buttonSearchFlights(self):
        self.driver.find_element(By.XPATH, self.button_searchFlights_xpath).click()

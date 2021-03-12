from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
    # driver.find_elements_by_css_selector(".card-title a").click()
    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

    cardTitle = (By.CSS_SELECTOR, ".card-title a")  # ""  "
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")  #
    checkOut = (By.XPATH, "//button[@class='btn btn-success']") #(By.CSS_SELECTOR, "a[class*='btn-primary']")  # checkOutItems  "//button[@class='btn btn-primary]"

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click() # btn btn-success
        confirmPage = ConfirmPage(self.driver)
        return confirmPage  # This sets the object for the Confirmation Page

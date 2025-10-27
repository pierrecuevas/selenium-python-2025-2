from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbResultsPage(BasePage):
    MOVIE_LINK = (By.CLASS_NAME, "ipc-metadata-list-summary-item__t")

    def press_link(self):
        self.click(self.MOVIE_LINK)
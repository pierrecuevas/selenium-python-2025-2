from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class LastfmResultsPage(BasePage):
    ARTIST_LINK = (By.CLASS_NAME, "link-block-target")

    def press_link(self):
        self.click(self.ARTIST_LINK)
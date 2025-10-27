from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LastfmArtistPage(BasePage):
    LATEST_RELEASE = (By.CLASS_NAME, "artist-header-featured-items-item-date")


    def get_latest_release_date(self):
        return self.find_element(self.LATEST_RELEASE).text
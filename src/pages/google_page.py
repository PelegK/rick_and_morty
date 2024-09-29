from src.pages.base_page import BasePage


class Google_Page(BasePage):
    def click_images(self):
        self.click(self.selectors.GooglePage.images)

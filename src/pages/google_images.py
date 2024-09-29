from src.pages.base_page import BasePage


class Google_Images(BasePage):
    def click_images(self):
      self.click(self.selectors.GooglePage.images)
        
    def perform_search(self, text):
      self.clear_text(self.selectors.GoogleImages.search_bar)
      self.set_text(self.selectors.GoogleImages.search_bar,f'Rick and Morty {text}')
      self.click(self.selectors.GoogleImages.search_button)
      

from src.pages.base_page import BasePage
from datetime import datetime



class Image_Page(BasePage):
  def go_image_url(self,url):
        self.new_tab(url)
        
  def get_screenshot(self,chars_name,chars_id):
    image = self.get_element(self.selectors.ImagePage.image)
    date_format = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    screenshot_name = f"{chars_name}-{chars_id}-{date_format}.png"
    image.screenshot(screenshot_name)
  
  

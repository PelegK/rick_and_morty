from src.pages.base_page import BasePage
from datetime import datetime



class Results_Page(BasePage):
    def calculate_position(self, chars_id):
        id = str(chars_id)
        if len(id) == 3:
            id = int(id[0])+int(id[2])
        elif len(id) == 2:
            id = int(id[0])+int(id[1])
        else:
            id = int(id)
        return id
        
    def get_screenshot(self,chars_name,chars_id,id):
        images = self.get_elements(self.selectors.ResultsPage.images) 
        images[id].click()
        image = self.get_element(self.selectors.ResultsPage.selected_image)
        date_format = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        screenshot_name = f"{chars_name}-{chars_id}-{date_format}.png"
        image.screenshot(screenshot_name)
        
    
        

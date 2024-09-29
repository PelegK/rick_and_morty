from selenium.webdriver.common.by import By


class Selectors():
    class GooglePage():
        images = (By.CSS_SELECTOR,
                  '[data-pid="2"]')

    class GoogleImages():
        search_bar = (By.CSS_SELECTOR, '#APjFqb')
        search_button = (By.CSS_SELECTOR, 'button > div')

    class ResultsPage():
        images = (By.CSS_SELECTOR, '[jsname="qQjpJ"]')

        selected_image = (By.CSS_SELECTOR, 'img.sFlh5c.FyHeAf.iPVvYb')
        
    class ImagePage():
        image =  (By.CSS_SELECTOR, 'body > img')

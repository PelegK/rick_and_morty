from src.pages.google_page import Google_Page
from src.pages.google_images import Google_Images
from src.pages.results_page import Results_Page
from src.pages.image_page import Image_Page
from src.character import create_characters

characters = create_characters()
def go_to_images(browser):
    gp = Google_Page(browser)
    gp.click_images()
    
def first_char(browser):
    gi = Google_Images(browser)
    gi.perform_search(characters["Character1"]["name"])
    rp = Results_Page(browser)
    position = rp.calculate_position(characters["Character1"]["id"])
    rp.get_screenshot(characters["Character1"]["name"],characters["Character1"]["id"],position)

def second_char(browser):
    ip = Image_Page(browser)
    ip.go_image_url(characters["Character2"]["image"])
    ip.get_screenshot(characters["Character2"]["name"],characters["Character2"]["id"])
    ip.close_browser()
    
def test_compare_locations(browser):
    go_to_images(browser)
    first_char(browser)
    second_char(browser)
    char1_location = characters["Character1"]["location"]
    char2_location = characters["Character2"]["location"]
    assert char1_location == char2_location, f"{characters["Character1"]["name"]} from {char1_location} and {characters["Character2"]["name"]} from {char2_location}."
    print(f"Both characters are from {char1_location}.")
    
   
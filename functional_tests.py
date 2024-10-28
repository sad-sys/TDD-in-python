from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        'Johnson opens up a website to write a To Do list'
        'He goes to the homepage'
        self.browser.get("http://localhost:8000")

        'J notices the page and title holds the phrase "Add To-Do list" '
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test now')

        'He adds book to a text box' 
        'It shows up underneath immediately'

        'Checking if it saved the right item'

        'He revisits that URL to see if the item is still there'

        'He closes the browser'

if __name__ == "__main__":
    unittest.main(warnings="ignore")
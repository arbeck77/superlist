from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edit goes to the home page and accidently tries to submit
        # an empty list item. She hits Enter on the empty input box

        # the home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # she tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # she recieves a similar warning on the list page

        # and she can correct it by filling some tex in
        self.fail('write me!')


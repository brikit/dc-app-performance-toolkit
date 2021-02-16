import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.CLASS_NAME, "brikit-header-backdrop"))
            page.wait_until_visible((By.ID, "brikit-simple-toolbar-toggle")).click()
            page.wait_until_visible((By.ID, "brikit-simple-toolbar"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-content-stack"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-title-container"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-layer"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-content-column"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-content-block"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-labels-container"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-comments-container"))
            page.wait_until_visible((By.CLASS_NAME, "brikit-footer-container"))
        sub_measure()
    measure()

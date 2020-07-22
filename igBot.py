from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path="./utils/geckodriver")

    def login(self):
        driver = self.driver
        driver.get("https://instagram.com.br")
        time.sleep(3)

        username = driver.find_element_by_xpath(
            "//input[@name='username']")
        username.click()
        username.clear()
        username.send_keys(self.username)

        password = driver.find_element_by_xpath(
            "//input[@name='password']")
        password.click()
        password.clear()
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)

    def comment(self):
        driver = self.driver
        driver.get(
            "[post-url]")
        time.sleep(3)

        try:
            time.sleep(2)
            comentarios = ["❤️", "🚀", "👋🏽", "🙅🏽‍♂️", "😁", "👍🏽", "😇",
                           "🤓", "🦊", "🌻", "😊", "😻", "🤠", "🙌🏽", "😽", "🙀", "💪🏽"]
            for i in range(100):
                comment_input_area = driver.find_element_by_class_name(
                    'Ypffh')
                comment_input_area.click()
                time.sleep(random.randint(4, 6))
                comment_input_area = driver.find_element_by_class_name(
                    'Ypffh.focus-visible')
                comment_input_area.click()
                comment_input_area.send_keys(random.choice(comentarios))
                time.sleep(random.randint(4, 6))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Post')]").click()
                time.sleep(random.randint(3, 6))
                driver.refresh()

        except Exception as e:
            print(e)


Bot = InstagramBot('[username]', '[password]')
Bot.login()
time.sleep(3)
Bot.comment()

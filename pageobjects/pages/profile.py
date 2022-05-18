from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from retry import retry


class ProfilePage(Page):

    @property
    def btn_avatar(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=".button.profile-box__button")

    @property
    def btn_save(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=".button.profile-box__save-btn")

    @property
    def input_avatar(self):
        return self.driver.find_element(by=By.ID, value="avatarId")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="login")

    @property
    def input_email(self):
        return self.driver.find_element(by=By.ID, value="email")

    @property
    def input_new_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    @property
    def input_new_password_repeat(self):
        return self.driver.find_element(by=By.ID, value="passwordRepeat")

    @property
    def input_old_password(self):
        return self.driver.find_element(by=By.ID, value="oldPassword")

    @property
    def div_avatar_error(self):
        return self.driver.find_element(by=By.ID, value="avatar-validation-box")

    def open(self, *args, **kwargs):
        super().open("profile")

    @retry(StaleElementReferenceException)
    def upload_avatar(self, avatar_path):
        self.input_avatar.send_keys(avatar_path)

    def is_avatar_error_exists(self):
        try:
            self.driver.find_element(by=By.ID, value="avatar-validation-box")
        except NoSuchElementException:
            return False
        return True

    @retry(StaleElementReferenceException)
    def set_login_input(self, text):
        login = self.driver.find_element(by=By.ID, value="login")
        login.clear()
        login.send_keys(text)

    @retry(StaleElementReferenceException)
    def set_input_email(self, text):
        self.input_email.send_keys(text)

    @retry(StaleElementReferenceException)
    def set_input_new_password(self, text):
        self.input_new_password.send_keys(text)

    @retry(StaleElementReferenceException)
    def set_input_new_password_repeat(self, text):
        self.input_new_password_repeat.send_keys(text)

    @retry(StaleElementReferenceException)
    def set_old_password(self, text):
        self.input_old_password.send_keys(text)

    @retry(StaleElementReferenceException)
    def click_save_btn(self):
        self.btn_save.click()

    @property
    @retry(StaleElementReferenceException)
    def input_email_text(self):
        return self.input_email.get_attribute('value')

    @property
    @retry((StaleElementReferenceException, ValueError))
    def input_login_text(self):
        value = self.input_login.get_attribute('value')
        if len(value) == 0:
            raise ValueError
        return self.input_login.get_attribute('value')

    @retry(StaleElementReferenceException)
    def input_login_clear(self):
        self.input_login.clear()

    def change_login(self, new_login, password):
        self.set_login_input(new_login)
        self.set_old_password(password)
        self.click_save_btn()

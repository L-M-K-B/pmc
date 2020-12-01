import json
import random
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = 'sign_up_screen'

    def log_in_success(self, uname, pword):
        with open('users.json') as file:
            users = json.load(file)

        if users.get(uname)['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password"



class SignupScreen(Screen):

    def add_user(self, uname, pword):
        with open('users.json') as file:
            users = json.load(file)

        users[uname] = {
            'username': uname,
            'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open('users.json', 'w') as file:
            json.dump(users, file)

        self.manager.current = 'sign_up_screen_success'


class SignupScreenSuccess(Screen):
    def log_in(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class LoginScreenSuccess(Screen):
    def enlighten(self, feeling):
        try:
            quotes = open(f'{feeling.lower()}.txt').read().split("\n")
            self.ids.quote.text = random.choice(quotes)

        except FileNotFoundError:
            self.ids.quote.text = "There is not yet a quote for your feeling"

    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()

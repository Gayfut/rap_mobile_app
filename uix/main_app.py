from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.resources import resource_add_path

from settings import PATH_TO_IMAGES
from uix.main_screen import MainScreen
from uix.result_screen import ResultScreen


class MainApp(App):
    def build(self):
        resource_add_path(PATH_TO_IMAGES)

        screen_manager = ScreenManager()

        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(ResultScreen(name='result'))

        return screen_manager

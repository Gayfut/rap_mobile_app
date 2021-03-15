"""file for control main app specification"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.resources import resource_add_path

from settings import PATH_TO_IMAGES
from uix.main_screen import MainScreen
from uix.result_screen import ResultScreen
from uix.fail_screen import FailScreen


class MainApp(App):
    """control main app"""

    def build(self):
        """create and config main app"""
        resource_add_path(PATH_TO_IMAGES)

        screen_manager = ScreenManager()

        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(ResultScreen(name="result"))
        screen_manager.add_widget(FailScreen(name="fail"))

        return screen_manager

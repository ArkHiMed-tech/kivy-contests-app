from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (340, 620)

Builder.load_file('layout.kv')

class ListScreen(Screen):
    pass

class ContestishApp(App):
    def build(self):
        smanager = ScreenManager()
        smanager.add_widget(ListScreen(name='list'))
        smanager.current_screen = 'list'
        return smanager


if __name__ == '__main__':
    ContestishApp().run()
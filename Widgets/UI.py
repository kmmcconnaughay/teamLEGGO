from kivy.app import App
from kivy.garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.app import App
from os.path import sep, expanduser, dirname
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from glob import glob
import os
import shutil

class PngPls(Popup):

    def popup(self):
        text = "Please input a .png file."
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text=text, font_size=20))
        mybutton = Button(text="Ok!", size_hint=(1, .20), font_size=20)
        content.add_widget(mybutton)

        pngpopup = Popup(content=content,
                         title="C'mon",
                         auto_dismiss=False,
                         size_hint=(.7, .5))
        mybutton.bind(on_press=pngpopup.dismiss)
        pngpopup.open()


class SelectFile(App):
    def __init__(self, **kwargs):
        super(SelectFile, self).__init__(**kwargs)
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        self.browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])
        self.browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled)
    def build(self):
        return (self.browser)
    def _fbrowser_canceled(self, instance):
        self.browser.clear_widgets()
        self.stop()
        from learningWidgets import Leggo_Mosiaac, AppBody
        Leggo_Mosiaac().run()
    def _fbrowser_success(self, instance):
        self.selected_image = str(instance.selection)
        i = len(instance.selection)
        self.selected_image = self.selected_image[2:i-3]
        self.file_name = self.selected_image.rsplit('/', 1)[-1]
        n = len(self.file_name)
        if self.file_name[n-4:n] == ".png":
            cwd = os.getcwd()
            shutil.copy(self.selected_image, cwd + '/teamLEGGO.png')
            self.browser.clear_widgets()
            print('hey there I am quitting nicely')
            self.drawInputImage2()
            self.drawImage2()
            self.drawBackButton()
        else:
            pngpls = PngPls()
            return pngpls.popup()

    def drawInputImage2(self):
        self.browser.add_widget(Label(text= 'Here is your image!:', size_hint=(.1, .1),
                pos_hint= {'x':.15, 'y':.8}))
    def drawImage2(self):
        self.wimg = Image(source = 'teamLEGGO.png', size_hint=(.6, .6),
                pos_hint= {'x':.2, 'y':.2})
        self.browser.add_widget(self.wimg)
    def drawBackButton(self):
        self.back = Button(text = 'Back', size_hint=(.1, .05),
                pos_hint= {'x':.9, 'y':.0})
        self.browser.add_widget(self.back)
        self.back.bind(on_press = self.call)
    def call(self, instance):
        if instance.text == 'Back':
            self.browser.clear_widgets()
            from learningWidgets import Leggo_Mosiaac, AppBody
            Leggo_Mosiaac().run()

if __name__ == '__main__':
     SelectFile().run()

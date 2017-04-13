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
from kivy.uix.screenmanager import ScreenManager, Screen
from glob import glob
import os
import shutil


class InputFile(Screen):

    def __init__(self, **kwargs):
        super(InputFile, self).__init__(**kwargs)
        self.label1 = Label(text='What do you want to brick?')
        button1 = Button(text='Choose a file_name')
        button1.bind(on_press=SelectFile().run())
        self.text1 = TextInput(multiline=False)
        self.add_widget(self.label1)
        self.add_widget(button1)
        self.add_widget(self.text1)


class DisplayImg(App):
    def build(self):
        root = self.root
        curdir = dirname(SelectFile.file_name)
        for file_name in glob(join(curdir, 'images', '*')):
            try:
                picture = Picture(source-file_name, rotation=randint(-30, 30))
                root.add_widget(picture)
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % file_name)

    def on_pause(self):
        return True


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

    def build(self):
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])
        browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        SelectFile.stop()

    def _fbrowser_success(self, instance):
        self.selected_image = str(instance.selection)
        i = len(instance.selection)
        self.selected_image = self.selected_image[2:i-3]
        self.file_name = self.selected_image.rsplit('/', 1)[-1]
        n = len(self.file_name)
        if self.file_name[n-4:n] == ".png":
            cwd = os.getcwd()
            shutil.move(self.selected_image, cwd + self.file_name)
            return Image(source=self.file_name)
            self.stop()
        else:
            pngpls = PngPls()
            return pngpls.popup()


sm = ScreenManager()
sm.add_widget(InputFile(name='Input File'))

class MyApp(App):
    def build(self):
        #return InputFile()
        SelectFile().run()


if __name__ == '__main__':
    MyApp().run()

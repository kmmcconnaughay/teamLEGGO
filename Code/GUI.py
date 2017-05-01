from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.image import Image

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
from vector_analysis import vectorStuff
import urllib.request

input_mat_size = 100;
class AppBody(FloatLayout):

    def __init__(self, **kwargs):
        super(AppBody, self).__init__(**kwargs)
        self.drawPage1()

    def drawPage1(self):
        self.clear_widgets()
        self.size = (300, 300)
        self.animal = 'teamLEGGO_pix'
        self.drawInputImage()
        self.drawImputURL()
        self.drawSize()

    def drawInputImage(self):
        self.add_widget(Label(text= 'Input Your Image:', size_hint=(.1, .1),
                pos_hint= {'x':.15, 'y':.2}))
        self.button = Button(text = 'Your Files', size_hint=(.5, .1),
                pos_hint= {'x':.35, 'y':.2})
        self.add_widget(self.button)
        self.button.bind(on_press = self.callback)
    def drawImputURL(self):
        self.add_widget(Label(text='Or Input URL to an image', size_hint=(.1, .1),
                pos_hint= {'x':.15, 'y':.45}))
        self.urlIn = TextInput(multiline=True, size_hint=(.5, .1),
                pos_hint= {'x':.35, 'y':.45})
        self.urlIn.bind(focus=self.on_focus)
        self.add_widget(self.urlIn)
    def drawSize(self):
        self.add_widget(Label(text='Baseplate Size:', size_hint=(.1, .1),
                pos_hint= {'x':.45, 'y':.775}))
        self.drop1 = Button(text = '5"x5"', size_hint=(.2, .1),
                pos_hint= {'x':0, 'y':.7})
        self.add_widget(self.drop1)
        self.drop2 = Button(text = '6"x6"', size_hint=(.2, .1),
                pos_hint= {'x':.2, 'y':.7})
        self.add_widget(self.drop2)
        self.drop3 = Button(text = '5"x10"', size_hint=(.2, .1),
                pos_hint= {'x':.4, 'y':.7})
        self.add_widget(self.drop3)
        self.drop4 = Button(text = '10"x10"', size_hint=(.2, .1),
                pos_hint= {'x':.6, 'y':.7})
        self.add_widget(self.drop4)
        self.drop5 = Button(text = '15"x15"', size_hint=(.2, .1),
                pos_hint= {'x':.8, 'y':.7})
        self.add_widget(self.drop5)

        self.drop1.bind(on_press = self.callback)
        self.drop2.bind(on_press = self.callback)
        self.drop3.bind(on_press = self.callback)
        self.drop4.bind(on_press = self.callback)
        self.drop5.bind(on_press = self.callback)


    def callback(self, instance):
        if instance.text == '5"x5"':
            global input_mat_size
            input_mat_size = 16
            print(input_mat_size)
        if instance.text == '6"x6"':
            global input_mat_size
            input_mat_size = 19
            print(input_mat_size)
        if instance.text == '5"x10"':
            global input_mat_size
            input_mat_size = 16
            print(input_mat_size)
        if instance.text == '10"x10"':
            global input_mat_size
            input_mat_size = 32
            print(input_mat_size)
        if instance.text == '15"x15"':
            global input_mat_size
            input_mat_size = 48
            print(input_mat_size)
        if instance.text == 'LEGGO':
            self.clear_widgets()
            self.animal = 'tiger'
            self.drawInputImage2()
            self.drawImage2()
            self.drawBackButton()
        if instance.text == 'Your Files':
            self.clear_widgets()
            SelectFile().run()
    def on_focus(self, instance, value):
        if value:
            pass
        else:
            self.inputURL = instance.text
            cwd = os.getcwd()
            urllib.request.urlretrieve(instance.text, "URLimg.png")
            dir_path = os.path.dirname(os.path.realpath('URLimg.png'))
            shutil.copy(dir_path + 'URLimg.png', cwd + '/URLimg.png')

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
        from GUI import Leggo_Mosiaac, AppBody
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
            self.drawLabelImage()
            self.drawImage2()
            self.drawBackButton()
        else:
            pngpls = PngPls()
            return pngpls.popup()

    def drawLabelImage(self):
        self.browser.add_widget(Label(text= 'Here is your image!:', size_hint=(.1, .1),
                pos_hint= {'x':.15, 'y':.8}))
    def drawImage2(self):
        pixelationProgram = vectorStuff()
        pixelationProgram.input_mat_size = input_mat_size
        pixelationProgram.runPixel()
        self.wimg = Image(source = 'teamLEGGO_pix.png', size_hint=(.6, .6),
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
            Leggo_Mosiaac().run()



class Leggo_Mosiaac(App):

    def build(self):
        return AppBody()


if __name__ == '__main__':
    Leggo_Mosiaac().run()

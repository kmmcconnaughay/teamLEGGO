"""
The GUI for the LEGO Brick'd project. Allows users to select files that they want
to pixelate, pixelates the image, and displays it.

Authors: Ana Krishnan and Annie Kroo

"""

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

input_mat_size = 48;
class AppBody(FloatLayout):

    def __init__(self, **kwargs):
        '''
        Inherit Float Layout information and draw page 1
        '''
        super(AppBody, self).__init__(**kwargs)
        self.drawPage1()

    def drawPage1(self):
        '''
        Calls draw meathods for the initial GUI page. Additionally, this includes
        clears the widgets, defines a window that is 300 by 300 and draws button
        to push to get to the file browser, draws the text box input for URL
        and draws all of the buttons for selecting mat size.
        '''
        self.clear_widgets()
        self.size = (300, 300)
        self.drawInputImage()
        self.drawInputURL()
        self.drawSize()

    def drawInputImage(self):
        '''
        Adds button widget and binds it to callback with its instance set to
        'Your Files' with a label widget next to the button as instructions.
        '''
        self.add_widget(Label(text= '[b]Brick it![/b]', markup = True,
                              size_hint=(.1, .1), pos_hint= {'x':.45, 'y':.83}, font_size='60sp'))
        self.add_widget(Label(text= '[b]Input Your Image:[/b]', markup = True,
                              size_hint=(.1, .1), pos_hint= {'x':.24, 'y':.3}, font_size='20sp'))
        self.button = Button(text = 'Your Files', size_hint=(.5, .1),
                pos_hint= {'x':.45, 'y':.3})
        self.add_widget(self.button)
        self.button.bind(on_press = self.callback)
    def drawInputURL(self):
        '''
        Add text input that has a label next to it with instructions. Binds this
        to on_focus such that it calls on_focus when the box is either clicked on
        or clicked off of.
        '''
        self.add_widget(Label(text='[b]Or Input URL to an image:[/b]', markup = True,
                              size_hint=(.1, .1),pos_hint= {'x':.2, 'y':.475}, font_size='20sp'))
        self.add_widget(Label(text='(Paste URL and click outside of textbox)', size_hint=(.1, .1),
                pos_hint= {'x':.18, 'y':.425}))
        self.urlIn = TextInput(multiline=False, size_hint=(.5, .1),
                pos_hint= {'x':.45, 'y':.45})
        self.urlIn.bind(focus=self.on_focus)
        self.add_widget(self.urlIn)
    def drawSize(self):
        '''
        Buttons for each size of LEGO mat with instances as the sizes of the buttons
        bound to callbacks.
        '''
        self.add_widget(Label(text='[b]Baseplate Size:[/b]', markup = True,
                size_hint=(.1, .1), pos_hint= {'x':.45, 'y':.7}, font_size='20sp'))
        self.drop1 = Button(text = '[b]5"x5"[/b]', markup = True, size_hint=(.15, .1),
                pos_hint= {'x':0.025, 'y':.61})
        self.add_widget(self.drop1)
        self.drop2 = Button(text = '[b]6"x6"[/b]', markup = True, size_hint=(.15, .1),
                pos_hint= {'x':.225, 'y':.61})
        self.add_widget(self.drop2)
        self.drop3 = Button(text = '[b]5"x10"[/b]', markup = True, size_hint=(.15, .1),
                pos_hint= {'x':.425, 'y':.61})
        self.add_widget(self.drop3)
        self.drop4 = Button(text = '[b]10"x10"[/b]', markup = True, size_hint=(.15, .1),
                pos_hint= {'x':.625, 'y':.61})
        self.add_widget(self.drop4)
        self.drop5 = Button(text = '[b]15"x15"[/b]', markup = True, size_hint=(.15, .1),
                pos_hint= {'x':.825, 'y':.61})
        self.add_widget(self.drop5)

        self.drop1.bind(on_press = self.callback)
        self.drop2.bind(on_press = self.callback)
        self.drop3.bind(on_press = self.callback)
        self.drop4.bind(on_press = self.callback)
        self.drop5.bind(on_press = self.callback)


    def callback(self, instance):
        '''
        Actions for when any button on the initial page is clicked. Actions include
        changing global variable for mat size used for pixelation and opening
        the file browser.
        '''
        if instance.text == '[b]5"x5"[/b]':
            global input_mat_size
            input_mat_size = 16
            print(input_mat_size)
        if instance.text == '[b]6"x6"[/b]':
            global input_mat_size
            input_mat_size = 19
            print(input_mat_size)
        if instance.text == '[b]5"x10"[/b]':
            global input_mat_size
            input_mat_size = 16
            print(input_mat_size)
        if instance.text == '[b]10"x10"[/b]':
            global input_mat_size
            input_mat_size = 32
            print(input_mat_size)
        if instance.text == '[b]15"x15"[/b]':
            global input_mat_size
            input_mat_size = 48
            print(input_mat_size)
        if instance.text == 'Your Files':
            self.clear_widgets()
            SelectFile().run()
    def on_focus(self, instance, value):
        '''
        Called when the text box is selected or deselected. Depending on action,
        pulls image from the URL inputted by the user on deselect.
        '''
        if value:
            pass
        else:
            self.inputURL = instance.text
            n = len(self.inputURL)
            if self.inputURL[n-4:n] == ".png":
                cwd = os.getcwd()
                urllib.request.urlretrieve(instance.text, "teamLEGGO.png")
                self.clear_widgets()
                self.drawLabelImage()
                self.drawImage2()
            else:
                pngpls = PngPls()
                return pngpls.popup()

    def drawLabelImage(self):
        '''
        Displays label for selected image.
        '''
        self.add_widget(Label(text= 'Here is your image!:', size_hint=(.1, .1),
                pos_hint= {'x':.15, 'y':.8}))
    def drawImage2(self):
        '''
        Displays the pixelated image.
        '''
        pixelationProgram = vectorStuff()
        pixelationProgram.input_mat_size = input_mat_size
        pixelationProgram.runPixel()
        self.wimg = Image(source = 'teamLEGGO_pix.png', size_hint=(.6, .6),
                pos_hint= {'x':.2, 'y':.2})
        self.add_widget(self.wimg)
        bricksUsed, cost = pixelationProgram.get_price(pixelationProgram.lego_nums, pixelationProgram.input_mat_size)
        self.add_widget(Label(text= bricksUsed, size_hint=(.1, .1),
                pos_hint= {'x':.5, 'y':0}))
        self.add_widget(Label(text= cost, size_hint=(.1, .1),
                pos_hint= {'x':.5, 'y':.1}))
    def call(self, instance):
        '''
        Runs the Lego mosaic main interface again.
        '''
        if instance.text == 'Back':
            self.clear_widgets()
            Leggo_Mosiaac().run()


class PngPls(Popup):

    def popup(self):
        '''
        Creates a popup window if the user attempts to select an image to pixelate
        that is not a .png file.

        Checks to see whether the file is a .png or not each time a file is selected.
        '''
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
        '''
        Creates a browser that uses the Kivy Garden FileBrowser add-on to allow
        the user to select a .png file to pixelate.
        '''
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
        '''
        Builds file browser.
        '''
        return (self.browser)
    def _fbrowser_canceled(self, instance):
        '''
        Runs if the cancel button in the FileBrowser is pressed. Clears widgets
        in FileBroswer and runs the main program again, taking the user back to
        the initial screen.
        '''
        self.browser.clear_widgets()
        self.stop()
        from GUI import Leggo_Mosiaac, AppBody
        Leggo_Mosiaac().run()
    def _fbrowser_success(self, instance):
        '''
        Checks to see whether the selected image is a .png or not. Outputs a
        pop up if it is not.

        Copies selected image into the current working directory (aka the teamLEGGO
        folder). Displays the selected image and the pixelated image with a back
        button to take the user back to the initial interface.
        '''
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
        else:
            pngpls = PngPls()
            return pngpls.popup()

    def drawLabelImage(self):
        '''
        Displays label for selected image.
        '''
        self.browser.add_widget(Label(text= 'Here is your image!:', size_hint=(.1, .1),
                pos_hint= {'x':.15, 'y':.8}))
    def drawImage2(self):
        '''
        Displays the pixelated image.
        '''
        pixelationProgram = vectorStuff()
        pixelationProgram.input_mat_size = input_mat_size
        pixelationProgram.runPixel()
        self.wimg = Image(source = 'teamLEGGO_pix.png', size_hint=(.6, .6),
                pos_hint= {'x':.2, 'y':.2})
        self.browser.add_widget(self.wimg)
        bricksUsed, cost = pixelationProgram.get_price(pixelationProgram.lego_nums, pixelationProgram.input_mat_size)
        self.browser.add_widget(Label(text= bricksUsed, size_hint=(.1, .1),
                pos_hint= {'x':.5, 'y':0}))
        self.browser.add_widget(Label(text= cost, size_hint=(.1, .1),
                pos_hint= {'x':.5, 'y':.1}))
    def call(self, instance):
        '''
        Runs the Lego mosaic main interface again.
        '''
        if instance.text == 'Back':
            self.browser.clear_widgets()
            Leggo_Mosiaac().run()



class Leggo_Mosiaac(App):

    def build(self):
        return AppBody()


if __name__ == '__main__':
    Leggo_Mosiaac().run()

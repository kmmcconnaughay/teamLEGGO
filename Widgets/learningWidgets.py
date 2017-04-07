from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.image import Image


class AppBody(GridLayout):

    def __init__(self, **kwargs):
        super(AppBody, self).__init__(**kwargs)
        self.cols = 2
        self.animal = 'lion'
        self.add_widget(Label(text= 'Input Your Image'))
        self.button = Button(text = 'Your Files')
        self.add_widget(self.button)
        self.button.bind(on_press = self.callback)

        self.add_widget(Label(text='Or Input URL'))
        self.urlIn = TextInput(multiline=True)
        self.urlIn.bind(focus=self.on_focus)
        self.add_widget(self.urlIn)

        self.add_widget(Label(text='How big do you want your lego mosaic?'))
        self.sizeIn = TextInput(multiline=False)
        self.sizeIn.bind(focus=self.on_focus)
        self.add_widget(self.sizeIn)

        self.slide = Slider(min=-100, max=100, value=25)
        self.add_widget(self.slide)

        self.drop = Button(text = 'Mosaic Size')
        self.add_widget(self.drop)

        self.drop.bind(on_press = self.callback)
        self.wimg = Image(source = '%s.jpg'%self.animal, allow_stretch =True)
        self.add_widget(self.wimg)
        #dropdown = DropDown()
        # for index in range(10):
        #     btn = Button(text = 'Value %d' %index, size_hint_y=None, height=44)
        #     btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        #     dropdown.add_widget(btn)
        # mainbutton = Button(text='Size', size_hint=(None,None))
        # mainbutton.bind(on_release = dropdown.open)
        # dropdown.bind(on_select=lambda instance, x:setattr(mainbutton, 'text', x))
        # runTouchApp(mainbutton)
    def callback(self, instance):
        if instance.text == 'Mosaic Size' and self.animal == 'lion':
            self.remove_widget(self.wimg)
            self.animal = 'tiger'
            self.wimg = Image(source = '%s.jpg'%self.animal, allow_stretch =True)
            self.add_widget(self.wimg)
        elif instance.text == 'Mosaic Size' and self.animal == 'tiger':
            self.remove_widget(self.wimg)
            self.animal = 'bear'
            self.wimg = Image(source = '%s.jpg'%self.animal, allow_stretch =True)
            self.add_widget(self.wimg)
        elif instance.text == 'Mosaic Size' and self.animal == 'bear':
            self.remove_widget(self.wimg)
            self.animal = 'Oh My!'
            self.wimg = Label(text='OH MY!')
            self.add_widget(self.wimg)
        elif instance.text == 'Mosaic Size' and self.animal == 'Oh My!':
            self.remove_widget(self.wimg)
            self.animal = 'lion'
            self.wimg = Image(source = '%s.jpg'%self.animal, allow_stretch =True)
            self.add_widget(self.wimg)
        if instance.text == 'Mosaic Size':
            print(self.animal)
        if instance.text == 'Your Files':
            print('May I please access your files os?')

    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User defocused', instance)
            print (instance.text)


class Leggo_Mosiaac(App):

    def build(self):
        return AppBody()


if __name__ == '__main__':
    Leggo_Mosiaac().run()

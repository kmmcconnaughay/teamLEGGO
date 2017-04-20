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



class AppBody(FloatLayout):

    def __init__(self, **kwargs):
        super(AppBody, self).__init__(**kwargs)
        self.drawPage1()

    def drawPage1(self):
        self.clear_widgets()
        self.size = (300, 300)
        self.animal = 'teamLEGGO'
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
        self.add_widget(Label(text='Or Input URL', size_hint=(.1, .1),
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
            print('5x5')
        if instance.text == '6"x6"':
            print('6x6')
        if instance.text == '5"x10"':
            print('5x10')
        if instance.text == '10"x10"':
            print('10x10')
        if instance.text == '15"x15"':
            print('15x15')
        if instance.text == 'LEGGO':
            self.clear_widgets()
            self.animal = 'tiger'
            self.drawInputImage2()
            self.drawImage2()
            self.drawBackButton()
        if instance.text == 'Your Files':
            self.clear_widgets()
            from UI import SelectFile
            SelectFile().run()
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

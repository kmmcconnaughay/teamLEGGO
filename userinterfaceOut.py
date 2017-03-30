import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import json

class TestApp(App):
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
    def build_settings(self, settings):
        jsondata =[
            { "type": "title", "title": "Test application" },
            { "type": "options", "title": "My first key",
            "desc": "Description of my first key",
            "section": "section1",
            "key": "key1",
            "options": ["value1", "value2", "another value"] },

            { "type": "numeric",
            "title": "My second key",
            "desc": "Description of my second key",
            "section": "section1",
            "key": "key2" }]
        #jsondata2 = json.dumps()
        settings.add_json_panel('Test application',
            self.config, data= json.dumps(jsondata))

    def on_config_change(self, config, section, key, value):
        if config is self.config:
            token = (section, key)
            if token == ('section1', 'key1'):
                print('Our key1 has been changed to', value)
            elif token == ('section1', 'key2'):
                print('Our key2 has been changed to', value)
    def display_settings(self, settings):
        try:
            p = self.settings_popup
        except AttributeError:
            self.settings_popup = Popup(content=settings,
                                        title='Settings',
                                        size_hint=(0.8, 0.8))
            p = self.settings_popup
        if p.content is not settings:
            p.content = settings
    def build(self):
        config = self.config
        return Label(text='key1 is %s and key2 is %d' % (
            config.get('section1', 'key1'),
            config.getint('section1', 'key2')))

if __name__ == '__main__':
    TestApp().run()

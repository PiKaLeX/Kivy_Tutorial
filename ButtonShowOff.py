from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class Main(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def action(self):
        label = self.root.ids.txt
        label.text = "This text is displayed after pressing button"

    def build(self):
        return Builder.load_file("ButtonShowOff.kv")


Main().run()
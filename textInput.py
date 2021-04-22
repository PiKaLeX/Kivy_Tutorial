from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

kv = """
Screen:
    MDLabel:
        text: "Basic Authentication App"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        halign: "center"
        font_style: "H2"
    MDTextField:
        id: password_input
        hint_text: 'Enter you password'
        helper_text: 'Forgot your password?'
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "account-search"
        required: True
        on_text_validate:
            app.password_validator()
    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        halign: "center"
        on_press:
            app.password_validator()
    MDLabel:
        text: ""
        id: password_validator_result
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        halign: "center"
"""


class Main(MDApp):
    variable_in_class = ObjectProperty(None)
    dialog = None

    def build(self):
        return Builder.load_string(kv)

    def password_validator(self):
        input_text = self.root.ids.password_input.text
        if self.dialog is None:
            self.dialog = MDDialog(
                title='Password check',
                text="Sucess !",
                size_hint=(0.8, 1),
                buttons=[
                    MDFlatButton(text='Close', on_release=self.close_dialog),
                    MDFlatButton(text='More')
                    ]
                )

        result = None
        if input_text == "root":
            result = "Success"

            self.dialog.text = 'Success !'
            self.dialog.open()
        else:
            result = "Fail"
            self.dialog.text = 'Fail !'
            self.dialog.open()

        self.root.ids.password_validator_result.text = result

    def close_dialog(self, obj):
        self.dialog.dismiss()




Main().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_box_layout = BoxLayout(orientation='vertical')
        keypad_order = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]

        self.operators = ["/", "*", "+", "-"]
        self.is_last_was_operator = False
        self.last_button = ""
        self.solution = TextInput(
            readonly=True,
            font_size=55,
            halign='right',
            multiline=False
        )
        main_box_layout.add_widget(self.solution)

        for row in keypad_order:

            line_box_layout = BoxLayout()

            for label in row:
                btn = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                btn.bind(on_press=self.on_press_button)
                line_box_layout.add_widget(btn)

            main_box_layout.add_widget(line_box_layout)

        btn = Button(
            text="=",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        btn.bind(on_press=self.on_solution)
        main_box_layout.add_widget(btn)

        return main_box_layout

    def on_press_button(self, instance):
        button_text = instance.text
        current_text = self.solution.text

        print(f'You pressed the button ({button_text})')

        if button_text == "C":  # Clear the text
            self.solution.text = ""

        else:
            # Est-ce que on ajoute un operateur sur un champs vide? Si oui, on ignore.
            if current_text == "" and (button_text in self.operators):
                return
            # Est-ce que l'on ajoute un operateur après un autre opérateur? Si oui, on ignore
            if self.is_last_was_operator and (button_text in self.operators):
                return
            # Rendu ici, l'opération devrait être legit.
            self.solution.text += button_text

        self.last_button = button_text
        self.is_last_was_operator = button_text in self.operators


    def on_solution(self, instance):
        print(f'You pressed the button ({instance.text})')

        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Select an Investment Scheme")
        layout.add_widget(self.label)

        self.scheme1_button = Button(text="Scheme 1")
        self.scheme1_button.bind(on_press=self.open_scheme1)
        layout.add_widget(self.scheme1_button)

        self.scheme2_button = Button(text="Scheme 2")
        self.scheme2_button.bind(on_press=self.open_scheme2)
        layout.add_widget(self.scheme2_button)

        # Add more buttons for additional schemes as needed

        self.add_widget(layout)

    def open_scheme1(self, instance):
        self.manager.current = 'scheme1'

    def open_scheme2(self, instance):
        self.manager.current = 'scheme2'


class SchemeScreen(Screen):
    def __init__(self, scheme_name, calculate_interest_func, **kwargs):
        super().__init__(**kwargs)
        self.scheme_name = scheme_name
        self.calculate_interest_func = calculate_interest_func

        layout = BoxLayout(orientation='vertical')

        self.label = Label(text=f"Enter deposit amount for {self.scheme_name}:")
        layout.add_widget(self.label)

        self.input = TextInput(multiline=False)
        layout.add_widget(self.input)

        self.button = Button(text="Calculate Interest")
        self.button.bind(on_press=self.calculate_interest)
        layout.add_widget(self.button)

        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def calculate_interest(self, instance):
        try:
            amount = int(self.input.text)
            result = self.calculate_interest_func(amount)
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Please enter a valid number."


def calculate_interest_scheme1(amount):
    # Replace this with the actual calculation logic for scheme 1
    return f"Interest for scheme 1 with amount {amount}"

def calculate_interest_scheme2(amount):
    # Replace this with the actual calculation logic for scheme 2
    return f"Interest for scheme 2 with amount {amount}"

class InterestCalculatorApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainMenu(name='main'))

        sm.add_widget(SchemeScreen("Scheme 1", calculate_interest_scheme1, name='scheme1'))
        sm.add_widget(SchemeScreen("Scheme 2", calculate_interest_scheme2, name='scheme2'))

        return sm

if __name__ == "__main__":
    InterestCalculatorApp().run()

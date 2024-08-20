from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FamilySavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        self.amount_input = TextInput(hint_text='Enter deposit amount', input_filter='int', multiline=False)
        layout.add_widget(self.amount_input)

        calculate_btn = Button(text='Calculate Interest', size_hint_y=None, height=70)
        calculate_btn.bind(on_press=self.calculate_interest)
        layout.add_widget(calculate_btn)

        self.result_label = Label(size_hint_y=None, height=200)
        layout.add_widget(self.result_label)

        back_btn = Button(text='Back to Menu', size_hint_y=None, height=50)
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def calculate_interest(self, instance):
        try:
            amount = int(self.amount_input.text)
            result = self.calculate_family_saving_interest(amount)
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_family_saving_interest(self, amount):
        def calculate_interest_family(amount, rate):
            yearly = amount * rate
            monthly = yearly / 12
            rate_src = .05 if amount <= 500000 else .10
            tax = monthly * rate_src
            interest = monthly - tax
            return interest

    def go_back(self, instance):
        self.manager.current = 'interest_calculator_menu'

class InterestCalculatorMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        fs_btn = Button(text='Family Saving Certificate')
        fs_btn.bind(on_press=self.go_to_family_saving)
        layout.add_widget(fs_btn)

        fy_btn = Button(text='Five-Year BD Saving Certificate')
        fy_btn.bind(on_press=self.go_to_five_year_saving)
        layout.add_widget(fy_btn)

        pb_btn = Button(text='Three-Month Profit-Bearing Certificate')
        pb_btn.bind(on_press=self.go_to_profit_bearing)
        layout.add_widget(pb_btn)

        ps_btn = Button(text='Pensioner Saving Certificate')
        ps_btn.bind(on_press=self.go_to_pensioner_saving)
        layout.add_widget(ps_btn)
        self.add_widget(layout)

    def go_to_family_saving(self, instance):
        self.manager.current = 'family_saving'

    def go_to_five_year_saving(self, instance):
        self.manager.current = 'five_year_saving'

    def go_to_profit_bearing(self, instance):
        self.manager.current = 'profit_bearing'

    def go_to_pensioner_saving(self, instance):
        self.manager.current = 'pensioner_saving'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        welcome_label = Label(text="Welcome to Sanchay App!", font_size=24)
        layout.add_widget(welcome_label)

        ic_btn = Button(text='Interest Calculator', size_hint_y=None, height=70)
        ic_btn.bind(on_press=self.go_to_interest_calculator)
        layout.add_widget(ic_btn)

        ss_btn = Button(text='Saving Schemes', size_hint_y=None, height=70)
        layout.add_widget(ss_btn)

        loc_btn = Button(text='Locations', size_hint_y=None, height=70)
        layout.add_widget(loc_btn)

        self.add_widget(layout)

    def go_to_interest_calculator(self, instance):
        self.manager.current = 'interest_calculator_menu'

class SavingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(InterestCalculatorMenuScreen(name='interest_calculator_menu'))
        sm.add_widget(FamilySavingScreen(name='family_saving'))

        sm.add_widget(Screen(name='five_year_saving'))
        sm.add_widget(Screen(name='profit_bearing'))
        sm.add_widget(Screen(name='pensioner_saving'))
        return sm

if __name__ == '__main__':
    SavingsApp().run()

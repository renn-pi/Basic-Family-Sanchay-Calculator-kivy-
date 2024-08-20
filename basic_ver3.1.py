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
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.amount_input = TextInput(hint_text='Enter deposit amount', input_filter='int', multiline=False)
        layout.add_widget(self.amount_input)
        
        calculate_btn = Button(text='Calculate Interest')
        calculate_btn.bind(on_press=self.calculate_interest)
        layout.add_widget(calculate_btn)

        self.result_label = Label(size_hint_y=None, height=200, text_size=(300, None))
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

        first_half_interest = calculate_interest_family(1500000, .1152)
        second_half_interest = calculate_interest_family(1500000, .1050)

        if amount <= 500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_family(amount, rate)}"
        elif amount <= 1500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_family(amount, rate)}"
        elif amount <= 3000000:
            rate = .1050
            rest = amount - 1500000
            second_interest = calculate_interest_family(rest, rate)
            total_interest = first_half_interest + second_interest
            return (f"Receive interest on the first 1,500,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    f"Total interest per month: {total_interest}")
        elif amount <= 4500000:
            rate = .0950
            rest_over = amount - 3000000
            third_interest = calculate_interest_family(rest_over, rate)
            total_interest = first_half_interest + second_half_interest + third_interest
            return (f"Receive interest on the first 1,500,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 1,500,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_over} taka: {third_interest}\n"
                    f"Total interest per month: {total_interest}")
        else:
            return ("Individual deposit amount exceeded for this scheme (family saving certificate).\n"
                    "Please input any amount up to 4,500,000 taka for Family Savings Certificate and try again.")

    def go_back(self, instance):
        self.manager.current = 'menu'

class MenuScreen(Screen):
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

class SavingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FamilySavingScreen(name='family_saving'))
        sm.add_widget(Screen(name='five_year_saving'))  # Placeholder screen for Five-Year BD Saving Certificate
        sm.add_widget(Screen(name='profit_bearing'))  # Placeholder screen for Three-Month Profit-Bearing Certificate
        sm.add_widget(Screen(name='pensioner_saving'))  # Placeholder screen for Pensioner Saving Certificate
        return sm

if __name__ == '__main__':
    SavingsApp().run()

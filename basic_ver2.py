from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.add_widget(Label(text="BD Savings App", font_size='24sp', size_hint=(1, 0.2)))

        buttons = [
            ('Family Saving Certificate', 'family_saving'),
            ('Five-Year BD Saving Certificate', 'five_year_saving'),
            ('Three-Month Profit-Bearing Certificate', 'three_month_profit'),
            ('Pensioner Saving Certificate', 'pensioner_saving')
        ]

        for button_text, screen_name in buttons:
            btn = Button(text=button_text, size_hint=(1, None), height=50)
            btn.bind(on_press=self.switch_to_scheme(screen_name))
            layout.add_widget(btn)

        self.add_widget(layout)

    def switch_to_scheme(self, screen_name):
        def switch(instance):
            self.manager.current = screen_name
        return switch

class FamilySavingScreen(Screen):
    def __init__(self, **kwargs):
        super(FamilySavingScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.amount_input = TextInput(hint_text='Enter deposit amount', multiline=False, size_hint=(1, None), height=50)
        layout.add_widget(self.amount_input)

        self.result_label = Label(text='', size_hint=(1, None), height=200)
        layout.add_widget(self.result_label)

        calculate_button = Button(text='Calculate Interest', size_hint=(1, None), height=50)
        calculate_button.bind(on_press=self.calculate_interest)
        layout.add_widget(calculate_button)

        self.add_widget(layout)

    def calculate_interest(self, instance):
        try:
            amount = int(self.amount_input.text)
        except ValueError:
            self.result_label.text = "Invalid number. Please insert an integer number without any decimals, commas, etc."
            return

        def calculate_interest_family(amount, rate):
            yearly = amount * rate
            monthly = yearly / 12
            if amount <= 500000:
                rate_src = .05
            else:
                rate_src = .10
            tax = monthly * rate_src
            interest = monthly - tax
            return interest

        first_half_interest = calculate_interest_family(1500000, .1152)
        second_half_interest = calculate_interest_family(1500000, .1050)

        if amount <= 500000:
            rate = .1152
            result = calculate_interest_family(amount, rate)
            self.result_label.text = f"Receive interest per month: {result}"
        elif amount > 500000 and amount <= 1500000:
            rate = .1152
            result = calculate_interest_family(amount, rate)
            self.result_label.text = f"Receive interest per month: {result}"
        elif amount > 1500000 and amount <= 3000000:
            rate = .1050
            rest = amount - 1500000
            second_interest = calculate_interest_family(rest, rate)
            total_interest = first_half_interest + second_interest
            self.result_label.text = f"Receive interest on the first 15,00,000 taka: {first_half_interest}\nReceive interest on the rest {rest} taka: {second_interest}\nTotal interest per month: {total_interest}"
        elif amount > 3000000 and amount <= 4500000:
            rate = .0950
            rest_over = amount - 3000000
            third_interest = calculate_interest_family(rest_over, rate)
            total_interest = first_half_interest + second_half_interest + third_interest
            self.result_label.text = f"Receive interest on the first 15,00,000 taka: {first_half_interest}\nReceive interest on the second 15,00,000 taka: {second_half_interest}\nReceive interest on the rest {rest_over} taka: {third_interest}\nTotal interest per month: {total_interest}"
        else:
            self.result_label.text = "Individual deposit amount exceeded for this scheme (family saving certificate). Please input any amount up to 4500000 taka for Poribar Sanchaypatra and try again."

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FamilySavingScreen(name='family_saving'))
        # Placeholder screens for the other schemes
        sm.add_widget(Screen(name='five_year_saving'))
        sm.add_widget(Screen(name='three_month_profit'))
        sm.add_widget(Screen(name='pensioner_saving'))
        return sm

if __name__ == '__main__':
    MainApp().run()

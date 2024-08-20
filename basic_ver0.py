from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class InterestCalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Enter deposit amount:")
        self.layout.add_widget(self.label)

        self.input = TextInput(multiline=False)
        self.layout.add_widget(self.input)

        self.button = Button(text="Calculate")
        self.button.bind(on_press=self.calculate_interest)
        self.layout.add_widget(self.button)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_interest(self, instance):
        try:
            amount = int(self.input.text)
            result = self.calculate_interest_amount(amount)
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Please enter a valid number."

    def calculate_interest_amount(self, amount):
        rest = 0
        rest_1 = 0
        rate = 0

        def calculate_interest_small(amount, rate):
            yearly = amount * rate
            month_three = yearly / 12
            tax = month_three * .05
            interest = month_three - tax
            return interest

        def calculate_interest(amount, rate):
            yearly = amount * rate
            monthly = yearly / 12
            tax = monthly * .10
            interest = monthly - tax
            return interest

        first_half_interest = calculate_interest(1500000, .1152)
        second_half_interest = calculate_interest(1500000, .1050)

        if amount <= 500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_small(amount, rate)}"

        elif amount > 500000 and amount <= 1500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest(amount, rate)}"

        elif amount > 1500000 and amount <= 3000000:
            rate = .1050
            rest = amount - 1500000
            second_interest = calculate_interest(rest, rate)
            return f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n" \
                   f"Receive interest on the rest {rest} taka: {second_interest}\n" \
                   f"Total interest per month: {first_half_interest + second_interest}"

        elif amount > 3000000 and amount <= 4500000:
            rate = .0950
            rest_1 = amount - 3000000
            third_interest = calculate_interest(rest_1, rate)
            return f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n" \
                   f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n" \
                   f"Receive interest on the rest {rest_1} taka: {third_interest}\n" \
                   f"Total interest per month: {first_half_interest + second_half_interest + third_interest}"

        elif amount > 4500000:
            return "Individual deposit amount exceeded for this scheme.\nPlease input any amount up to 4500000 taka and try again."

if __name__ == "__main__":
    InterestCalculatorApp().run()

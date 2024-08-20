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

        calculate_btn = Button(text='Calculate Interest',size_hint_y=None, height=70) 
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



class FiveYearScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        self.amount_input = TextInput(hint_text='Enter deposit amount', input_filter='int', multiline=False)
        layout.add_widget(self.amount_input)

        

        calculate_btn = Button(text='Calculate Interest',size_hint_y=None, height=70) 
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
            result = self.calculate_five_year_interest(amount)
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_five_year_interest(self, amount):
        def calculate_interest_yearly(amount, rate):
            yearly_interest = amount * rate
            if amount <= 500000:
                rate_src = .05
            elif amount > 500000 :
                rate_src = .10
            tax = yearly_interest * rate_src
            interest = yearly_interest - tax
            return interest

        first_half_interest = calculate_interest_yearly(1500000, .1128)
        second_half_interest = calculate_interest_yearly(1500000, .1030)

        if amount <= 500000 :  
            rate = .1128
            return f"Receive interest per year: {calculate_interest_yearly(amount, rate)}"

        elif amount > 500000 and amount <= 1500000 :
            rate = .1128
            return f"Receive interest per year: {calculate_interest_yearly(amount,rate)}"

        elif amount > 1500000 and amount <= 3000000 :
            rate = .1030
            
        
            rest = amount - 1500000
            second_interest = calculate_interest_yearly(rest,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    f"Total interest every year: {first_half_interest + second_interest}\n")

        

        elif amount > 3000000 and amount <= 6000000:
            rate = .0930
            rest_1 = amount - 3000000
            third_interest = calculate_interest_yearly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                    f"Total interest every year: {first_half_interest + second_half_interest + third_interest}\n"
                    f"__________________________________________________________\n"
                    f" Note:Individual deposit limit exceeded.\n"
                    f"This calculated amount is only applicable for joint or company investments.\n")

           

        elif amount > 6000000 and amount <= 500000000:
            rate = .0930
            #return
            #for amount exceeding 60 lac
            rest_1 = amount - 3000000
            third_interest = calculate_interest_yearly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                    f"Total interest every year: {first_half_interest + second_half_interest + third_interest}\n"
                    f"_______________________________________________\n"
                    f"Note: Individual and Joint deposit amount exceeded for this scheme.\n"
                    f"This calculated amount may be applicable for companies.\n")
            
        else:
            return ("Investment amount exceeded for this scheme.\n"
                    "Please input any amount up to 3,000,000 taka for individual,\n"
                    "or up to 6,000,000 taka for joint investments,\n"
                    "or up to 50,000,000 taka for companies and try again.\n")



    def go_back(self, instance):  
        self.manager.current = 'menu'



class QuarterlySavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        self.amount_input = TextInput(hint_text='Enter deposit amount', input_filter='int', multiline=False)
        layout.add_widget(self.amount_input)

        calculate_btn = Button(text='Calculate Interest',size_hint_y=None, height=70) 
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
            result = self.calculate_quarterly_interest(amount) 
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_quarterly_interest(self, amount):
        def calculate_interest_quarterly(amount, rate):
            yearly = amount * rate
            monthly = yearly / 4
            if amount <= 500000:
                rate_src = .05
            elif amount > 500000 :
                rate_src = .10
            tax = monthly * rate_src
            interest = monthly - tax
            return interest

        first_half_interest = calculate_interest_quarterly (1500000,.1104)
        second_half_interest = calculate_interest_quarterly (1500000,.10)


        if amount <= 500000 :
            rate = .1104
            return f"Receive interest per month: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 500000 and amount <= 1500000 :
            rate = .1104
            return f"Receive interest per month: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 1500000 and amount <= 3000000 :
            rate = .10
            #return
            rest = amount - 1500000
            second_interest = calculate_interest_quarterly(rest,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    f"Total interest every three-month: {first_half_interest + second_interest}\n")

        elif amount > 3000000 and amount <= 6000000 :
                rate = .09
                rest_1 = amount - 3000000
                third_interest = calculate_interest_quarterly(rest_1,rate)
                return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                        f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                        f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                        f"Total interest every three-month: {first_half_interest + second_half_interest + third_interest}\n"
                        f"_______________________________________________\n"
                        f"Note:Individual deposit limit exceeded.\n"
                        f"This calculated amount is applicable for joint or company investments.\n")

        elif amount > 6000000 and amount <= 500000000: 
            rate = .09
            rest_1 = amount - 3000000
            third_interest = calculate_interest_quarterly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                    f"Total interest every three-month: {first_half_interest + second_half_interest + third_interest}\n"
                    f"_______________________________________________\n"
                    f"Note: Individual and Joint deposit amount exceeded for this scheme.\n"
                    f"This calculated amount may be applicable for companies.\n")

        else:
            return ("Investment amount exceeded for this scheme.\n"
                    "Please input any amount up to 3,000,000 taka for individual,\n"
                    "or up to 6,000,000 taka for joint investments,\n"
                    "or up to 50,000,000 taka for companies and try again.\n")

    def go_back(self, instance):  
        self.manager.current = 'menu'

class PensionerSavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        self.amount_input = TextInput(hint_text='Enter deposit amount', input_filter='int', multiline=False)
        layout.add_widget(self.amount_input)

        calculate_btn = Button(text='Calculate Interest',size_hint_y=None, height=70) 
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
            result = self.calculate_pensioner_interest(amount) 
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_pensioner_interest(self, amount):
        def calculate_interest_quarterly(amount, rate): 
            yearly = amount * rate
            three_months = yearly / 4
            if amount <= 500000:
                interest = three_months 
                return interest
            elif amount > 500000 :
                rate_src = .10
            tax = three_months * rate_src
            interest = three_months - tax
            return interest

        first_half_interest = calculate_interest_quarterly (1500000,.1176)
        second_half_interest = calculate_interest_quarterly (1500000,.1075)


        if amount <= 500000 :
            rate = .1176
            return f"Receive interest every three-month: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 500000 and amount <= 1500000 :
            rate = .1176
            return f"Receive interest every three-month: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 1500000 and amount <= 3000000 :
            rate = .1075
            #
            rest = amount - 1500000
            second_interest = calculate_interest_quarterly(rest,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    f"Total interest every three-month: {first_half_interest + second_interest}\n")

        elif amount > 3000000 and amount <= 5000000 :
            rate = .0975
            #
            rest_1 = amount - 3000000
            third_interest = calculate_interest_quarterly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                   f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                   f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                   f"Total interest every three-month: {first_half_interest + second_half_interest + third_interest}\n")

        elif amount > 5000000 :
            return ("Deposit limit exceeded.\n"
                   "Please input any amount up to 5000000 taka and try again.\n")


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
        
        sm.add_widget(FiveYearScreen(name='five_year_saving'))  
        sm.add_widget(QuarterlySavingScreen(name='profit_bearing'))  
        sm.add_widget(PensionerSavingScreen(name='pensioner_saving')) 
        return sm

if __name__ == '__main__':
    SavingsApp().run()

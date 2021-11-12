# *******************Progress!***************************
# Layout of the Calcuator is Completed
# Clear "C" button is Defined in the Calculator
# Numbers are Defined
# Symbols are Defined
# eval() operation is used
# 00 Button is Added
# Cancel Button "<" is Defined
# Decimal Points problem solved
# Equal sign "=" is Defined
# Positive Negative "+/-" is Defined
# Calculator App is completed and  Ready to Use
# *******************************************************
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("calc.kv")

class Window(Widget):
    Window.size = (300,400)
    def clear(self):
        self.ids.calc_input.text = ''


    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"
    

    def zero_zero(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}00"


    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[:-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
        if "-" in prior and "." not in num_list[:-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
        if "*" in prior and "." not in num_list[:-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
        if "/" in prior and "." not in num_list[:-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
    

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
    

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"


    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = f"{answer}"
        except:
            self.ids.calc_input.text = "Error"





class Calculator(App):
    def build(self):
        return Window()

if __name__ == "__main__":
    Calculator().run()
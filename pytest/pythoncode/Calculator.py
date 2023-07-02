class Calculator:
    def add(self, a, b):

        if a > 99 or a < -99 or b > 99 or b < -99:
            print("Please enter an integer or floating-point number within the range of [-99, 99]")
            return "Parameter value is out of range."

        return a + b

    def div(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("Please enter an integer or floating-point number within the range of [-99, 99]")
            return "Parameter value is out of range."

        return a / b
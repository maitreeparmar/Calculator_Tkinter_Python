# Required libraries
import tkinter as tk


class Calculator:
    def __init__(calc):
        calc.window = tk.Tk()
        calc.window.geometry("250x250")
        calc.window.resizable(0, 0)
        calc.window.title("Simple Calculator")
        calc.total_expression = ""
        calc.current_expression = ""
        calc.display_frame = calc.create_display_frame()
        calc.total_label, calc.label = calc.create_display_labels()

        calc.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        calc.operations = {"+": "+", "-": "-", "*": "\u00D7", "/": "\u00F7"}
        calc.buttons_frame = calc.create_buttons_frame()
        calc.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            calc.buttons_frame.rowconfigure(x, weight=1)
            calc.buttons_frame.columnconfigure(x, weight=1)

        calc.create_digit_buttons()
        calc.create_operator_buttons()
        calc.create_special_buttons()
        calc.bind_keys()

    def bind_keys(calc):
        calc.window.bind("<Return>", lambda event: calc.evaluate())
        for key in calc.digits:
            calc.window.bind(str(key), lambda event, digit=key: calc.add_to_expression(digit))
        for key in calc.operations:
            calc.window.bind(key, lambda event, operator=key: calc.append_operator(operator))

    def create_special_buttons(calc):
        calc.create_clear_button()
        calc.create_equals_button()

    def create_display_labels(calc):
        total_label = tk.Label(calc.display_frame, text=calc.total_expression, anchor=tk.E, padx=24)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(calc.display_frame, text=calc.current_expression, anchor=tk.E, padx=24)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(calc):
        frame = tk.Frame(calc.window, height=221)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(calc, value):
        calc.current_expression += str(value)
        calc.update_label()

    def create_digit_buttons(calc):
        for digit, grid_value in calc.digits.items():
            button = tk.Button(calc.buttons_frame, text=str(digit), borderwidth=0,
                               command=lambda x=digit: calc.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(calc, operator):
        calc.current_expression += operator
        calc.total_expression += calc.current_expression
        calc.current_expression = ""
        calc.update_total_label()
        calc.update_label()

    def create_operator_buttons(calc):
        i = 0
        for operator, symbol in calc.operations.items():
            button = tk.Button(calc.buttons_frame, text=symbol, borderwidth=0,
                               command=lambda x=operator: calc.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(calc):
        calc.current_expression = ""
        calc.total_expression = ""
        calc.update_label()
        calc.update_total_label()

    def create_clear_button(calc):
        button = tk.Button(calc.buttons_frame, text="C", borderwidth=0, command=calc.clear)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def evaluate(calc):
        calc.total_expression += calc.current_expression
        calc.update_total_label()
        try:
            calc.current_expression = str(eval(calc.total_expression))
            calc.total_expression = ""
        except Exception as e:
            calc.current_expression = "Error"
        finally:
            calc.update_label()

    def create_equals_button(calc):
        button = tk.Button(calc.buttons_frame, text="=", borderwidth=0, command=calc.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(calc):
        frame = tk.Frame(calc.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(calc):
        expression = calc.total_expression
        for operator, symbol in calc.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        calc.total_label.config(text=expression)

    def update_label(calc):
        calc.label.config(text=calc.current_expression[:11])

    def run(calc):
        calc.window.mainloop()


if __name__ == "__main__":
    calculate = Calculator()
    calculate.run()

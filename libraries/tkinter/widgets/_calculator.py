import tkinter.ttk as ttk
import tkinter as tk
from widgets.logic import C_logic


class Calculator_GUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.logic = C_logic
        self.results = []
        self.create_widgets()

    def create_widgets(self):
        self.entry_one = ttk.Entry(self)
        self.entry_one.grid(row=0, column=0, padx=5, pady=5)
        self.entry_two = ttk.Entry(self)
        self.entry_two.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(self, text="first number:").grid(row=0, column=0, sticky="n", padx=5)
        ttk.Label(self, text="first number:").grid(row=0, column=2, sticky="n", padx=5)

        ttk.Button(self, text="+", command=self.add).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self, text="-", command=self.substract).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self, text="*", command=self.multiply).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(self, text="/", command=self.divide).grid(row=1, column=3, padx=5, pady=5)

        self.result_var = tk.StringVar()
        self.result_conbobox = ttk.Combobox(self, textvariable=self.result_var, values=self.results, state="readonly")
        self.result_conbobox.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
        self.result_conbobox.set("Results...")

    def get_operands(self):
        try:
            _one = float(self.entry_one.get())
            _two = float(self.entry_two.get())
            return _one, _two
        except ValueError:
            return None, None
        
    def add_result(self, result):
        self.results.append(str(result))
        self.result_conbobox['values'] = self.results
        self.result_conbobox.set(str(result))

    def add(self):
        one, two = self.get_operands()
        if one is not None and two is not None:
            result = self.logic._sum(one, two)
            self.add_result(result)
        else:
            self.add_result("Error: Invalid entry")

    def substract(self):
        one, two = self.get_operands()
        if one is not None and two is not None:
            result = self.logic._substract(one, two)
            self.add_result(result)
        else:
            self.add_result("Error: Invalid entry")

    def multiply(self):
        one, two = self.get_operands()
        if one is not None and two is not None:
            result = self.logic._multiply(one, two)
            self.add_result(result)
        else:
            self.add_result("Error: Invalid entry")

    def divide(self):
        one, two = self.get_operands()
        if one is not None and two is not None:
            result = self.logic._divide(one, two)
            self.add_result(result)
        else:
            self.add_result("Error: Invalid entry")
    


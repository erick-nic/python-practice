import tkinter as tk
from widgets._calculator import Calculator_GUI

def main():
    root = tk.Tk()
    root.title("Basic calculator")
    Calculator_GUI(root).pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
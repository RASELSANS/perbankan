import tkinter as tk
from tkinter import messagebox

class BankCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Calculator")
        self.root.geometry("400x300")

        # Create frames
        self.frame_header = tk.Frame(self.root, bg="#333")
        self.frame_header.pack(fill="x")

        self.frame_menu = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_menu.pack(fill="x")

        self.frame_input = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_input.pack(fill="x")

        self.frame_result = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_result.pack(fill="x")

        # Create header
        self.label_header = tk.Label(self.frame_header, text="Bank Calculator", font=("Arial", 24), bg="#333", fg="#fff")
        self.label_header.pack(pady=10)

        # Create menu
        self.label_menu = tk.Label(self.frame_menu, text="Menu:", font=("Arial", 18), bg="#f0f0f0")
        self.label_menu.pack(pady=10)

        self.button_calculate = tk.Button(self.frame_menu, text="Calculate Interest", font=("Arial", 18), command=self.calculate_interest)
        self.button_calculate.pack(pady=10)

        self.button_exit = tk.Button(self.frame_menu, text="Exit", font=("Arial", 18), command=self.root.destroy)
        self.button_exit.pack(pady=10)

        # Create input fields
        self.label_principal = tk.Label(self.frame_input, text="Principal Amount:", font=("Arial", 18), bg="#f0f0f0")
        self.label_principal.pack(pady=10)

        self.entry_principal = tk.Entry(self.frame_input, font=("Arial", 18), width=20)
        self.entry_principal.pack(pady=10)

        self.label_rate = tk.Label(self.frame_input, text="Interest Rate (%):", font=("Arial", 18), bg="#f0f0f0")
        self.label_rate.pack(pady=10)

        self.entry_rate = tk.Entry(self.frame_input, font=("Arial", 18), width=20)
        self.entry_rate.pack(pady=10)

        self.label_time = tk.Label(self.frame_input, text="Time Period (years):", font=("Arial", 18), bg="#f0f0f0")
        self.label_time.pack(pady=10)

        self.entry_time = tk.Entry(self.frame_input, font=("Arial", 18), width=20)
        self.entry_time.pack(pady=10)

        self.label_interest_type = tk.Label(self.frame_input, text="Interest Type:", font=("Arial", 18), bg="#f0f0f0")
        self.label_interest_type.pack(pady=10)

        self.variable_interest_type = tk.StringVar()
        self.variable_interest_type.set("Bunga Tunggal")

        self.option_menu_interest_type = tk.OptionMenu(self.frame_input, self.variable_interest_type, "Bunga Tunggal", "Bunga Majemuk", "Anuitas")
        self.option_menu_interest_type.pack(pady=10)

        # Create result label
        self.label_result = tk.Label(self.frame_result, text="", font=("Arial", 18), bg="#f0f0f0")
        self.label_result.pack(pady=10)



    def calculate_interest(self):
        principal = float(self.entry_principal.get())
        rate = float(self.entry_rate.get()) / 100
        time = float(self.entry_time.get())
        interest_type = self.variable_interest_type.get()

        if interest_type == "Bunga Tunggal":
            interest = principal * rate * time
        elif interest_type == "Bunga Majemuk":
            interest = principal * (1 + rate) ** time
        elif interest_type == "Anuitas":
            interest = principal * ((1 + rate) ** time - 1) / rate

        result = f"Principal: Rp {principal:.2f}\nInterest Rate: {rate*100:.2f}%\nTime Period: {time:.2f} years\nInterest Type: {interest_type}\nInterest: Rp {interest:.2f}\nTotal Amount: Rp {principal + interest:.2f}"
        self.label_result.config(text=result)

root = tk.Tk()
app = BankCalculator(root)
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import requests

def convert_curr():
    from_currency = from_entry.get().upper()
    to_currency = to_entry.get().upper()
    amount_str = amount_entry.get()

    # Check if amount is numeric
    try:
        amount = float(amount_str)
    except ValueError:
        messagebox.showerror("Input Error", "Amount needs to be numeric.")
        return

    # API URL
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=4934b637a9d8ec71bf794ec02c3018e4"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

       
        if not data.get("success"):
            messagebox.showerror("API Error", data.get("error", {}).get("info", "Unknown error"))
            return

        rates = data["rates"]

       
        if from_currency not in rates or to_currency not in rates:
            messagebox.showerror("Currency Error", "Invalid currency code.")
            return

        from_rate = rates[from_currency]
        to_rate = rates[to_currency]

    
        result = amount * (to_rate / from_rate)
        result_label.config(
            text=f"{amount} {from_currency} = {result:.2f} {to_currency}", fg="white"
        )

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error or API error:", str(e))



#GUI setup

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.config(bg="#3b8beb") 

# Heading
tk.Label(
    root, text="Currency Converter", font=("Helvetica", 16, "bold"),
    bg="#3b8beb", fg="black"
).pack(pady=10)

# FROM
tk.Label(root, text="From Currency (e.g., USD)", bg="#3b8beb", fg="black").pack()
from_entry = tk.Entry(root, width=20)
from_entry.pack(pady=5)

# TO
tk.Label(root, text="To Currency (e.g., PKR)", bg="#3b8beb", fg="black").pack()
to_entry = tk.Entry(root, width=20)
to_entry.pack(pady=5)

# AMOUNT
tk.Label(root, text="Amount", bg="#3b8beb", fg="black").pack()
amount_entry = tk.Entry(root, width=20)
amount_entry.pack(pady=5)

# BUTTON
tk.Button(
    root, text="Convert", command=convert_curr,
    bg="#ffffff", fg="#080E15", font=("Helvetica", 10, "bold")
).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#3b8beb")
result_label.pack(pady=10)

root.mainloop()
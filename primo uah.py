import tkinter as tk

def convert_currency():
    try:
        amount = float(entry_amount.get())
        exchange_rate = float(3.17)

        if var_currency.get() == 1:  # UAH to USD
            converted_amount = amount / exchange_rate
            result_label.config(text=f"{amount} Primogems is equal to {converted_amount:.2f} UAH")
        elif var_currency.get() == 2:  # USD to UAH
            converted_amount = amount * exchange_rate
            result_label.config(text=f"{amount} UAH is equal to {converted_amount:.2f} Primogems")
        else:
            result_label.config(text="Invalid currency selection")
    except ValueError:
        result_label.config(text="Please enter valid numeric values")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create and place widgets
label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_currency = tk.Label(root, text="Currency:")
label_currency.grid(row=1, column=0, padx=10, pady=10, sticky="e")

var_currency = tk.IntVar()
radio_uah = tk.Radiobutton(root, text="Primogems to UAH", variable=var_currency, value=1)
radio_uah.grid(row=1, column=1, padx=10, pady=10, sticky="w")

radio_usd = tk.Radiobutton(root, text="UAH to Primogems", variable=var_currency, value=2)
radio_usd.grid(row=2, column=1, padx=10, pady=10, sticky="w")

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()

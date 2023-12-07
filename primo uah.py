import tkinter as tk

# mxdlaxh calculator Primos to multicurrency and UAH to pimos, enjoy)

def convert_currency():
    try:
        amount = float(entry_amount.get())
        exchange_rate_UAH = float(3.17)
        exchange_rate_PLN = float(16.59)
        exchange_rate_BYN = float(22.64)
        if var_currency.get() == 1:  
            converted_amount_UAH = amount / exchange_rate_UAH
            converted_amount_PLN = amount / exchange_rate_PLN
            converted_amount_BYN = amount / exchange_rate_BYN
            result_label.config(text=f"{amount} Primogems is equal to {converted_amount_UAH:.2f} UAH, {converted_amount_PLN:.2f} PLN, {converted_amount_BYN:.2f} BYN")
        elif var_currency.get() == 2:  
            converted_amount = amount * exchange_rate_UAH
            result_label.config(text=f"{amount} UAH is equal to {converted_amount:.2f} Primogems")
        else:
            result_label.config(text="Invalid currency selection")
    except ValueError:
        result_label.config(text="Please enter valid numeric values")
        
def create_gradient(canvas, width, height, colors):
    color_count = len(colors)
    color_step = 1 / (color_count - 1)
    for i in range(color_count - 1):
        start_x = 0
        start_y = int(i * height * color_step)
        end_x = width
        end_y = int((i + 1) * height * color_step)

        canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=colors[i], outline="")

def on_radio_change():
    selected_color = color_var.get()
    label.config(text=f"Selected Color: {selected_color}", fg=selected_color)


root = tk.Tk()
root.title("Currency Converter")
root.configure(bg="#f1cbff", padx=60, pady=40)
width, height = 600, 400
root.geometry(f"{width}x{height}")
font1 = ("Calibri",14)
root.grid_columnconfigure(0, weight=0)
root.grid_rowconfigure(0, weight=1)

gif_path = "primo4.gif"
original_image = tk.PhotoImage(file=gif_path)
resized_image = original_image.subsample(2, 2) 

label = tk.Label(root, image=resized_image)
label.grid(row=0, column=0, padx=10)

label_currency = tk.Label(root, text="Currency:", font=font1, bg='#f1cbff',fg='#662c2a' )
label_currency.grid(row=1, column=0, padx=10, pady=0,sticky="e" )

var_currency = tk.IntVar()
radio_uah = tk.Radiobutton(root, text="Primogems to UAH/PLN/BYN", font=font1, bg='#f1cbff',fg='#662c2a',variable=var_currency, value=1)
radio_uah.grid(row=1, column=1, padx=10, pady=15, sticky="w")

radio_usd = tk.Radiobutton(root, text="UAH to Primogems", font=font1, bg='#f1cbff',fg='#662c2a', variable=var_currency, value=2)
radio_usd.grid(row=2, column=1, padx=10, sticky="w")

label_amount = tk.Label(root,text="Amount:", font=font1, bg='#f1cbff',fg='#662c2a')
label_amount.grid(row=3, column=0, padx=10, pady=10,sticky="e")

entry_amount = tk.Entry(root,width=40,bg="#f5daff")
entry_amount.grid(row=3, column=1, padx=10, pady=10, )

convert_button = tk.Button(root, text="Convert", font=font1, bg='#f5daff',fg='#190b0a', command=convert_currency)
convert_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="",font=font1, bg='#f1cbff',fg='white')
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()

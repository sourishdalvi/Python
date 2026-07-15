import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root 
        self.root.title("Restaurant Management App")
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82
        frame = ttk.Frame(root)
        frame.pack(pady=20)
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}       
        self.menu_quantities = {}   
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            ).grid(row=i, column=0, padx=10, pady=5)
            e=ttk.Entry(frame,width=5)
            e.grid(row=i, column=0,pady=5)
            self.entries={}
        ttk.Combobox(
            frame,
            textvariable=self.currency,
            values=["USD", "INR"],
            state="readonly",
            width=10
            ) .grid(row=len(self.menu_items)+1,columnspan=1)
        ttk.Button(
            frame,
            text="Place Order",command=self.place_order) .grid(row=len(self.menu_items)+2, columnspan=3, pady=1)
    def place_order(self):
            rate=self.exchange_rate if self.currency.get() == "INR" else 1
            symbol = "₹" if self.currency.get() == "INR" else "$"
            total = 0
            summary = ""
            for item, entry in self.entries.items():
                quantity = entry.get()
                if quantity.isdigit() and int(quantity) > 0:
                    quantity = int(quantity)
                    cost=quantity * self.menu_items[item] * rate
                    total += cost
                    summary += f"{item}: {quantity} = {symbol}{cost}\n"
                else:
                    messagebox.showerror("Invalid Input","Order at least one item.")
root = tk.Tk()
root.geometry("600x400")
RestaurantOrderManagement(root)
root.mainloop()

from tkinter import *
from tkinter import ttk
import requests
class CurrencyConverterGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Amount input
        self.amount_label = ttk.Label(self, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # From currency dropdown
        self.from_label = ttk.Label(self, text="From:")
        self.from_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.from_currency = ttk.Combobox(self, values=self.get_currency_list())
        self.from_currency.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency.set("USD")

        # To currency dropdown
        self.to_label = ttk.Label(self, text="To:")
        self.to_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.to_currency = ttk.Combobox(self, values=self.get_currency_list())
        self.to_currency.grid(row=2, column=1, padx=10, pady=10)
        self.to_currency.set("EUR")

        # Convert button
        self.convert_button = ttk.Button(self, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Result label
        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def get_currency_list(self):
        # This method should return a list of currency codes
        # For simplicity, we'll return a small list. In a real application,
        # you might want to fetch this from an API or a more comprehensive source.
        return ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR"]

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                rate = data['rates'][to_curr]
                result = amount * rate
                self.result_label.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
            else:
                self.result_label.config(text="Error fetching exchange rates")
        except ValueError:
            self.result_label.config(text="Please enter a valid amount")
        except KeyError:
            self.result_label.config(text="Invalid currency selection")
        except requests.RequestException:
            self.result_label.config(text="Network error. Please check your connection.")


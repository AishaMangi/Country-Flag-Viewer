# "National Emblem Finder"
import requests
import pycountry
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox


def get_iso_code(country_name):
    try:
        country = pycountry.countries.search_fuzzy(country_name)[0]
        return country.alpha_2.lower()  # Convert country name to ISO Alpha-2 code
    except:
        return None


def get_flag():
    country_name = entry.get().strip()
    iso_code = get_iso_code(country_name)

    if iso_code:
        url = f"https://flagcdn.com/w320/{iso_code}.png"  # Fetch flag using ISO Alpha-2 code
        response = requests.get(url)

        if response.status_code == 200:
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img = ImageTk.PhotoImage(img)

            panel.config(image=img)
            panel.image = img
        else:
            messagebox.showerror("Error", "Flag not found! Please enter a valid country name.")
    else:
        messagebox.showerror("Error", "Invalid country name! Please enter a correct country.")


# GUI Setup
root = tk.Tk()
root.title("Country Flag Generator")

tk.Label(root, text="Enter Country Name:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Flag", command=get_flag).pack(pady=10)

panel = tk.Label(root)
panel.pack()

root.mainloop()
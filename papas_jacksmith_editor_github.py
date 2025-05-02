
# Papa's + Jacksmith Deluxe Save Editor GUI (GitHub Edition - Ticket, Stars, and Unlocks)

from pyamf.sol import SolReader, SolWriter
import tkinter as tk
from tkinter import filedialog, messagebox
import os, shutil

def modify_papas_sol(input_path, output_path, new_money, new_season, new_tickets, new_stars, new_stickers, unlock_minigames_flag, unlock_ingredients_flag):
    with open(input_path, "rb") as f:
        sol = SolReader(f).read()
    data = sol.body

    for key in data:
        if 'money' in key or 'medals' in key:
            data[key] = new_money
    for key in data:
        if 'month' in key or 'season' in key:
            data[key] = new_season
    for key in data:
        if 'toppingsrevealed' in key:
            data[key] = True
    for key in data:
        if 'alltickets' in key or 'tickets' in key:
            data[key] = new_tickets
            data[key] = 999

        for key in data:
        if 'stars' in key:
            data[key] = new_stars
        if 'stickers' in key:
            data[key] = new_stickers
        if 'minigamesunlocked' in key and unlock_minigames_flag:
            data[key] = True
        if ('ingredientsunlocked' in key or 'toppingsunlocked' in key) and unlock_ingredients_flag:
            data[key] = True

    with open(output_path, "wb") as f:
        SolWriter(f).write(sol)

def run_editor():
    game = selected_game.get()
    input_path = entry_input.get()
    output_path = entry_output.get()
    try:
        new_money = int(entry_money.get())
    except ValueError:
        messagebox.showerror("Error", "Money must be a number!")
        return
    new_season = entry_season.get()

    try:
        shutil.copy2(input_path, input_path + ".backup")
        if game in ["Papa's Pizzeria DX", "Papa's Freezeria DX"]:
            new_tickets = int(entry_tickets.get())
            new_stars = int(entry_stars.get())
            new_stickers = int(entry_stickers.get())
            minigames_flag = unlock_minigames.get()
            ingredients_flag = unlock_ingredients.get()
            modify_papas_sol(input_path, output_path, new_money, new_season, new_tickets, new_stars, new_stickers, minigames_flag, ingredients_flag)
            messagebox.showinfo("Success", f"{game} save modified! Backup created.")
        elif game == "Jacksmith":
            messagebox.showinfo("Coming Soon", "Jacksmith mod support is coming soon once save format is confirmed!")
        else:
            messagebox.showwarning("Unsupported", "This game is not supported yet.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("SOL files", "*.sol")])
    if path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, path)

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".sol", filetypes=[("SOL files", "*.sol")])
    if path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, path)

# Create GUI
app = tk.Tk()
app.title("Save Editor Toolkit")
app.geometry("480x240")
app.configure(bg="#1e1e1e")
app.attributes('-alpha', 0.92)  # Slight transparency

# Game selector
tk.Label(app, text="Select Game:", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="e")
selected_game = tk.StringVar(app)
selected_game.set("Papa's Pizzeria DX")
games = ["Papa's Pizzeria DX", "Papa's Freezeria DX", "Jacksmith"]
tk.OptionMenu(app, selected_game, *games).grid(row=0, column=1)

# Input/output
tk.Label(app, text="Input .sol File:", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="e")
entry_input = tk.Entry(app, width=40)
entry_input.grid(row=1, column=1)
tk.Button(app, text="Browse", command=browse_file).grid(row=1, column=2)

tk.Label(app, text="Output .sol File:", bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="e")
entry_output = tk.Entry(app, width=40)
entry_output.grid(row=2, column=1)
tk.Button(app, text="Save As", command=save_file).grid(row=2, column=2)

# Money + Season + Extras
tk.Label(app, text="Money Amount:", bg="#1e1e1e", fg="white").grid(row=3, column=0, sticky="e")
entry_money = tk.Entry(app)
entry_money.insert(0, "999999")
entry_money.grid(row=3, column=1)

tk.Label(app, text="Season (e.g. Winter):", bg="#1e1e1e", fg="white").grid(row=4, column=0, sticky="e")
entry_season = tk.Entry(app)
entry_season.insert(0, "Winter")
entry_season.grid(row=4, column=1)

# Extra Fields
tk.Label(app, text="Tickets (optional):", bg="#1e1e1e", fg="white").grid(row=5, column=0, sticky="e")
entry_tickets = tk.Entry(app)
entry_tickets.insert(0, "999")
entry_tickets.grid(row=5, column=1)

# More Extra Fields
tk.Label(app, text="Stars (optional):", bg="#1e1e1e", fg="white").grid(row=6, column=0, sticky="e")
entry_stars = tk.Entry(app)
entry_stars.insert(0, "100")
entry_stars.grid(row=6, column=1)

tk.Label(app, text="Stickers (optional):", bg="#1e1e1e", fg="white").grid(row=7, column=0, sticky="e")
entry_stickers = tk.Entry(app)
entry_stickers.insert(0, "50")
entry_stickers.grid(row=7, column=1)

tk.Label(app, text="Unlock All Minigames:", bg="#1e1e1e", fg="white").grid(row=8, column=0, sticky="e")
unlock_minigames = tk.BooleanVar(value=True)
tk.Checkbutton(app, variable=unlock_minigames, bg="#1e1e1e").grid(row=8, column=1, sticky="w")

tk.Label(app, text="Unlock All Ingredients:", bg="#1e1e1e", fg="white").grid(row=9, column=0, sticky="e")
unlock_ingredients = tk.BooleanVar(value=True)
tk.Checkbutton(app, variable=unlock_ingredients, bg="#1e1e1e").grid(row=9, column=1, sticky="w")

# Run
tk.Button(app, text="Apply Changes", command=run_editor).grid(row=5, column=1, pady=10)

app.mainloop()


import os
import shutil
import json
from pyamf.sol import SolReader, SolWriter
from datetime import datetime

def main():
    print("🎮 Welcome to Papa's Save Editor Toolkit! 💙🌈🐾")
    print("=" * 60)
    print("🔥 For Fans, By Fans | Flipline Studios Save Editor")
    print("🔧 Supports: JackSmith (PC/Steam), Freezeria DX, Pizzeria DX")
    print("=" * 60)
    
    choice = input("Select a game to edit:
1. JackSmith (PC/Steam)
2. Papa's Freezeria DX
3. Papa's Pizzeria DX

Enter your choice: ").strip()
    if choice == "1":
        edit_jacksmith()
    elif choice == "2":
        edit_papas('Freezeria')
    elif choice == "3":
        edit_papas('Pizzeria')
    else:
        print("❌ Invalid choice. Please restart.")

def edit_jacksmith():
    print("
🔧 JackSmith Save Editor 💰")
    file_path = input("Enter the path to your JackSmith save file (JSON): ").strip()
    file_path = auto_detect_file(file_path, '.json')

    if not os.path.exists(file_path):
        print("❌ File not found. Please check the path.")
        return

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        print("
💡 Real-Time Editing Mode (JackSmith) 💡")
        # Gold
        print(f"Current Gold: {data.get('gold', 'Unknown')}")
        new_gold = input("Enter new Gold value (or press Enter to keep current): ").strip()
        if new_gold and new_gold.isdigit():
            data['gold'] = int(new_gold)

        # Items
        print(f"Current Items: {data.get('items', 'Unknown')}")
        new_items = input("Enter new Items value (or press Enter to keep current): ").strip()
        if new_items and new_items.isdigit():
            data['items'] = int(new_items)

        # Unlocking Recipes
        unlock_craft = input("Unlock all craft recipes? (Y/N): ").strip().lower()
        if unlock_craft == "y":
            data['craft_recipes'] = "ALL_UNLOCKED"
            print("✅ All craft recipes unlocked.")

        unlock_papa = input("Unlock all Papa recipes? (Y/N): ").strip().lower()
        if unlock_papa == "y":
            data['papa_recipes'] = "ALL_UNLOCKED"
            print("✅ All Papa recipes unlocked.")

        print("
✅ Updated Values Preview:")
        print(json.dumps(data, indent=4))

        confirm = input("
💾 Save changes? (Y/N): ").strip().lower()
        if confirm == "y":
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print("✅ JackSmith save file has been successfully updated! 💙")
        else:
            print("❌ Changes discarded.")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

def edit_papas(game_name):
    print(f"
🔧 {game_name} Save Editor 💰")
    file_path = input(f"Enter the path to your {game_name} save file (.sol): ").strip()
    file_path = auto_detect_file(file_path, '.sol')

    if not os.path.exists(file_path):
        print("❌ File not found. Please check the path.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.{timestamp}.backup"
    shutil.copy(file_path, backup_path)
    print(f"✅ Backup created: {backup_path}")

    try:
        with open(file_path, "rb") as f:
            sol = SolReader(f).read()
        data = sol.body

        print("
💡 Real-Time Editing Mode (Freezeria/Pizzeria) 💡")
        # Money
        print(f"Current Money: {data.get('money', 'Unknown')}")
        new_money = input("Enter new Money value (or press Enter to keep current): ").strip()
        if new_money:
            data['money'] = float(new_money)

        # Stars
        print(f"Current Stars: {data.get('stars', 'Unknown')}")
        new_stars = input("Enter new Stars value (or press Enter to keep current): ").strip()
        if new_stars:
            data['stars'] = int(new_stars)

        # Tickets
        unlock_tickets = input("Unlock all tickets? (Y/N): ").strip().lower()
        if unlock_tickets == "y":
            data['tickets'] = 9999

        # Stickers
        unlock_stickers = input("Unlock all stickers? (Y/N): ").strip().lower()
        if unlock_stickers == "y":
            data['stickers'] = "ALL_UNLOCKED"

        # Minigames & Ingredients
        unlock_minigames = input("Unlock all minigames? (Y/N): ").strip().lower()
        unlock_ingredients = input("Unlock all ingredients? (Y/N): ").strip().lower()
        if unlock_minigames == "y":
            data['minigames'] = "ALL_UNLOCKED"
        if unlock_ingredients == "y":
            data['ingredients'] = "ALL_UNLOCKED"

        print("
✅ Updated Values Preview:")
        for key, value in data.items():
            print(f"{key}: {value}")

        confirm = input("
💾 Save changes? (Y/N): ").strip().lower()
        if confirm == "y":
            with open(file_path, "wb") as f:
                SolWriter(f).write(data)
            print(f"✅ {game_name} save file has been successfully updated! 💙")
        else:
            print("❌ Changes discarded.")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

def auto_detect_file(directory_or_file, extension):
    if os.path.isfile(directory_or_file):
        return directory_or_file
    elif os.path.isdir(directory_or_file):
        for file in os.listdir(directory_or_file):
            if file.endswith(extension):
                return os.path.join(directory_or_file, file)
    return directory_or_file

if __name__ == "__main__":
    main()

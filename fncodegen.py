import random
import string
import time
import pyautogui
import os

def generate_random_string(length=16):
    """Gen random shit"""
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def main():
    # Window title lmao [idk why did i code this program]"
    os.system('title Fortnite Code Gen')
    
    try:
        num_of_codes = int(input("How many codes? "))
    except ValueError:
        print("Please enter a valid number bro.")
        return
    
    for _ in range(num_of_codes):
        random_string = generate_random_string()
        print(f"Generated code: {random_string}")
        
        # Text selector
        pyautogui.hotkey('ctrl', 'a')
        
        # Type the code
        pyautogui.write(random_string)
        pyautogui.press('enter')  # Press enter
        
        # wait 5 sec
        time.sleep(5)

if __name__ == "__main__":
    main()

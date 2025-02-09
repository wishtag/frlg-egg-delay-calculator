import os
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    clear_screen()
    frames = input("Frames: ")
    frames_list = frames.split("\t")
    print(f"\nHeld Advance: {Fore.GREEN}{int(frames_list[0])-18}{Style.RESET_ALL}")
    print(f"\nPickup Advance: {Fore.GREEN}{int(frames_list[1])-3}{Style.RESET_ALL}")
    input()
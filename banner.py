#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import pyfiglet

# Optional: pip install pyfiglet if you want dynamic ASCII art
try:
    from pyfiglet import Figlet
    use_figlet = True
except ImportError:
    use_figlet = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()

    if use_figlet:
        f = Figlet(font='slant')
        print(f.renderText('WordStorm'))
    else:
        print(r"""
 __        __   _                                     
 \ \      / /__| | ___ ___  _ __ ___   ___     
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \     
   \ V  V /  __/ | (_| (_) | | | | | |  __/   
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|      
              """)
    
    print("⚡ WordStorm - Custom Password List Generator ⚡ \n")
    print("Author: Subigya")
    print("Generates ~10M unique passwords from base words you provide.\n")
    print("DISCLAIMER:")
    print("This tool is intended for **educational** and **authorized testing** purposes only.")
    print("Unauthorized usage against systems you do not own or have permission to test is illegal.")
    print("Use responsibly. You are solely responsible for your actions.")
    print("-------------------------------------------------------------\n")

    time.sleep(2)
show_banner()

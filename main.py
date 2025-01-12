#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A TO DO List program that is ran from the command line.
"""

import sys
from functions import *

def main():
    """
    Main entry point for the script.
    """
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            remove_task()

        elif choice == "3":
            show_tasks()

        elif choice == "4":
            sys.exit(0)

if __name__ == "__main__":
    main()

import sqlite3
from tkinter import *
from window import Window
from commands import *

if __name__ == '__main__':

    create_tables()
    #insert_workstations()

    root = Tk()
    app = Window(root)



import tkinter as tk

from Customer import Customer

if __name__ == "__main__":

    Cust1 = Customer("Андрей", "Деркач", "89283334455")
    Cust2 = Customer("Максим", "Баландин", "89283334555")

    print(Cust1)
    print(Cust2)
    print(Cust1 == Cust2)
    print(Cust1.short_info())
    print(Cust2.short_info())

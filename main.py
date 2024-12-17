import tkinter as tk

from Customer import Customer

if __name__ == "__main__":
    
    Cust1 = Customer("Андрей", "Деркач", "andrey.derkach@mail.ru")
    Cust2 = Customer("Максим", "Баландин", "max@mail.ru")
    
    print(Cust1)
    print(Cust2)
    print(Cust1.__eq__(Cust2))
    print(Cust1.short_info())
    print(Cust2.short_info())

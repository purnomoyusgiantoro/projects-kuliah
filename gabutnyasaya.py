import tkinter as tk 
from tkinter import messagebox

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

matematik = ""

def number(symbol):
    global matematik
    matematik += str(symbol)
    entry.delete(0, tk.END)
    entry.insert(tk.END, matematik)

def hapus():
    global matematik
    matematik = ""
    entry.delete(0, tk.END)

def hitung():
    global matematik
    try:
        result = eval(matematik)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        matematik = str(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        hapus()

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

window = tk.Tk()
lebar= 300
tinggi = 300
x = 300
y = 100
window.title("KALKULATOR")
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx = int((screenwidth/2)-(lebar/2))
newy = int((screenheight/2)-(tinggi/2)-100)
window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)
window.columnconfigure(5,weight=1)

window.rowconfigure(4,weight=1)
window.rowconfigure(5,weight=1)
window.rowconfigure(6,weight=1)
window.rowconfigure(7,weight=1)
window.rowconfigure(8,weight=1)
window.rowconfigure(9,weight=1)
window.rowconfigure(10,weight=1)
window.rowconfigure(11,weight=1)
window.rowconfigure(12,weight=1)


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


buttonBG = tk.Button(window,text=" ",command= hapus,bg="#000000",state='disabled')
buttonBG.grid(column=0, row=0, columnspan=6, rowspan=13, sticky="wens")


tk.Label(window, text="").grid(row=5, column=1, sticky='wens')
entry = tk.Entry(window,justify='right',font="30",bg="#000000",fg="#FFFFFF")
entry.grid(row=5, column=1, sticky='wens',columnspan=4)


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


buttonac = tk.Button(window,text="AC",command= hapus,bg="#E5E5EA",font="10")
buttonac.grid(column=1, row=7, sticky="wens")

buttonplusminus= tk.Button(window,text="+/-",bg="#E5E5EA",font="10")
buttonplusminus.grid(column=2, row=7, sticky="wens" )


buttonpersen = tk.Button(window,text="%",command=lambda: number ('*0.1'),bg="#E5E5EA",font="10")
buttonpersen.grid(column=3, row=7, sticky="wens" )

buttonbagi = tk.Button(window,text=":",command=lambda: number ('/'),bg="#FF9500",fg="#FFFFFF",font="10")
buttonbagi.grid(column=4, row=7, sticky="wens" )


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

button1 = tk.Button(window,text="1",command=lambda: number ('1'),bg="#333333",fg="#FFFFFF",font="10")
button1.grid(column=1, row=10, sticky="wens" )

button2= tk.Button(window,text="2",command=lambda: number ('2'),bg="#333333",fg="#FFFFFF",font="10")
button2.grid(column=2, row=10, sticky="wens" )

button3 = tk.Button(window,text="3",command=lambda: number ('3'),bg="#333333",fg="#FFFFFF",font="10")
button3.grid(column=3, row=10, sticky="wens" )

buttonplus = tk.Button(window,text="+",command=lambda: number ('+'),bg="#FF9500",fg="#FFFFFF",font="10")
buttonplus.grid(column=4, row=10, sticky="wens" )


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


button4 = tk.Button(window,text="4",command=lambda: number ('4'),bg="#333333",fg="#FFFFFF",font="10")
button4.grid(column=1, row=9, sticky="wens" )

button5 = tk.Button(window,text="5",command=lambda: number ('5'),bg="#333333",fg="#FFFFFF",font="10")
button5.grid(column=2, row=9, sticky="wens" )

button6 = tk.Button(window,text="6",command=lambda: number ('6'),bg="#333333",fg="#FFFFFF",font="10")
button6.grid(column=3, row=9, sticky="wens" )

buttonminus = tk.Button(window,text="-",command=lambda: number ('-'),bg="#FF9500",fg="#FFFFFF",font="10")
buttonminus.grid(column=4, row=9, sticky="wens" )


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

button7 = tk.Button(window,text="7",command=lambda: number ('7'),bg="#333333",fg="#FFFFFF",font="10")
button7.grid(column=1, row=8, sticky="wens" )

button8 = tk.Button(window,text="8",command=lambda: number ('8'),bg="#333333",fg="#FFFFFF",font="10")
button8.grid(column=2, row=8, sticky="wens" )

button9 = tk.Button(window,text="9",command=lambda: number ('9'),bg="#333333",fg="#FFFFFF",font="10")
button9.grid(column=3, row=8, sticky="wens" )

buttonx = tk.Button(window,text="x",command=lambda: number ('*'),bg="#FF9500",fg="#FFFFFF",font="10")
buttonx.grid(column=4, row=8, sticky="wens" )


#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

button0 = tk.Button(window,text="0",command=lambda: number ('0'),bg="#333333",fg="#FFFFFF",font="10")
button0.grid(column=1, row=11, sticky="wens", columnspan=2)

button0 = tk.Button(window,text=".",command=lambda: number ('.'),bg="#333333",fg="#FFFFFF",font="10")
button0.grid(column=3, row=11, sticky="wens" )

buttonresult = tk.Button(window,text="=",command= hitung ,bg="#FF9500",fg="#FFFFFF",font="10")
buttonresult.grid(column=4, row=11, sticky="wens" )




window.mainloop()




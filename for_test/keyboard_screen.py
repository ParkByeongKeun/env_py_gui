# https://www.youtube.com/watch?v=QHEYF3oquVk

from tkinter import *

root = Tk()
root.geometry('800x480')

e = Entry(root, width=200, border=7)
e.grid(row=0, column=0, columnspan=15, padx=20, pady=20)

def Button_click(alfabet):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(alfabet))

wave = Button(root, text='~`', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_1 = Button(root, text='1', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_2 = Button(root, text='2', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_3 = Button(root, text='3', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_4 = Button(root, text='4', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_5 = Button(root, text='5', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_6 = Button(root, text='6', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_7 = Button(root, text='7', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_8 = Button(root, text='8', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_9 = Button(root, text='9', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_0 = Button(root, text='0', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Minus = Button(root, text='-', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_is_equal= Button(root, text='=', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
Button_Backspace = Button(root, text='Backspace', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')


Tab_Button = Button(root, text='Tab  ', padx=55, pady=19, font=("Courier", 14), background='black', foreground='white')

Q = Button(root, text='Q', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('Q'), background='black', foreground='white')
W = Button(root, text='W', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('W'), background='black', foreground='white')
E = Button(root, text='E', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('E'), background='black', foreground='white')
R = Button(root, text='R', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('R'), background='black', foreground='white')
T = Button(root, text='T', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('T'), background='black', foreground='white')
Y = Button(root, text='Y', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('Y'), background='black', foreground='white')
U = Button(root, text='U', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('U'), background='black', foreground='white')
I = Button(root, text='I', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('I'), background='black', foreground='white')
O = Button(root, text='O', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('O'), background='black', foreground='white')
P = Button(root, text='P', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('P'), background='black', foreground='white')

right_bracket = Button(root, text='[', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click('['), background='black', foreground='white')

OR_line = Button(root, text='|', padx=88, pady=10, font=("Courier", 22),command=lambda: Button_click('|'), background='black', foreground='white')

left_bracket = Button(root, text=']', padx=20, pady=10, font=("Courier", 22),command=lambda: Button_click(']'), background='black', foreground='white')


Capslock = Button(root, text='Capslock', padx=34, pady=18, font=("Courier", 15), background='black', foreground='white')

A = Button(root, text='A', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
S = Button(root, text='S', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
D = Button(root, text='D', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
F = Button(root, text='F', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
G = Button(root, text='G', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
H = Button(root, text='H', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
J = Button(root, text='J', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
K = Button(root, text='K', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
L = Button(root, text='L', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')

colum = Button(root, text=';', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
coma_dot = Button(root, text='"', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')

Enter = Button(root, text='Enter', padx=71, pady=18, font=("Courier", 15), background='black', foreground='white')

Shift = Button(root, text='', padx=50, pady=18, font=("Courier", 15), background='black', foreground='white')
Shift2 = Button(root, text='Shift  ', padx=80, pady=18, font=("Courier", 15), background='black', foreground='white')


Z = Button(root, text='Z', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
X = Button(root, text='X', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
C = Button(root, text='C', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
V = Button(root, text='V', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
B = Button(root, text='B', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
N = Button(root, text='N', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
M = Button(root, text='M', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
coma = Button(root, text=',', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')
dot = Button(root, text='.', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')


Shift_2 = Button(root, text='Shift  ', padx=100, pady=18, font=("Courier", 15), background='black', foreground='white')
or_slash = Button(root, text='/', padx=20, pady=10, font=("Courier", 22), background='black', foreground='white')

Control = Button(root, text='Ctrl  ', padx=20, pady=8, font=("Courier", 24), background='black', foreground='white')

windows = Button(root, text='Win', padx=20, pady=12, font=("Courier", 22), background='black', foreground='white')

Alt = Button(root, text=' Alt', padx=20, pady=12, font=("Courier", 22), background='black', foreground='white')

Space = Button(root, text='        Space          ', padx=20, pady=12, font=("Courier", 22), background='black', foreground='white')

AltGr = Button(root, text='AltGr', padx=20, pady=12, font=("Courier", 22), background='black', foreground='white')

windows_2 = Button(root, text='Win ', padx=18, pady=12, font=("Courier", 22), background='black', foreground='white')

Ctrl_2 = Button(root, text='     Ctrl', padx=20, pady=12, font=("Courier", 22), background='black', foreground='white')


Fn = Button(root, text=' Fn ', padx=20, pady=12, font=("Courier", 22), background='black', foreground='white')



Button_1.grid(row=2, column=1)
Button_2.grid(row=2, column=2)
Button_3.grid(row=2, column=3)
Button_4.grid(row=2, column=4)
Button_5.grid(row=2, column=5)
Button_6.grid(row=2, column=6)
Button_7.grid(row=2, column=7)
Button_8.grid(row=2, column=8)
Button_9.grid(row=2, column=9)
Button_0.grid(row=2, column=10)
Minus.grid(row=2, column=11)
Button_is_equal.grid(row=2, column=12)
Button_Backspace.grid(row=2, column=13)

wave.grid(row=2, column=0)
Tab_Button.grid(row=3, column=0, columnspan=2)
#
Q.grid(row=3, column=1, columnspan=2)
W.grid(row=3, column=2, columnspan=2)
E.grid(row=3, column=3, columnspan=2)
R.grid(row=3, column=4, columnspan=2)
T.grid(row=3, column=5, columnspan=2)
Y.grid(row=3, column=6, columnspan=2)
U.grid(row=3, column=7, columnspan=2)
I.grid(row=3, column=8, columnspan=2)
O.grid(row=3, column=9, columnspan=2)
P.grid(row=3, column=10, columnspan=2)

right_bracket.grid(row=3, column=11, columnspan=2)
left_bracket.grid(row=3, column=10, columnspan=4)

OR_line.grid(row=3, column=13, columnspan=8)

Capslock.grid(row=4, columnspan=2)

A.grid(row=4, column=2)
S.grid(row=4, column=3)
D.grid(row=4, column=4)
F.grid(row=4, column=5)
G.grid(row=4, column=6)
H.grid(row=4, column=7)
J.grid(row=4, column=8)
K.grid(row=4, column=9)
L.grid(row=4, column=10)
colum.grid(row=4, column=11)
coma_dot.grid(row=4, column=12)
#
Enter.grid(row=4, column=13)


Shift.grid(row=5, column=0, columnspan=2)
Shift2.grid(row=5, column=0, columnspan=3)


Z.grid(row=5, column=2, columnspan=2)
X.grid(row=5, column=3, columnspan=2)
C.grid(row=5, column=4, columnspan=2)
V.grid(row=5, column=5, columnspan=2)
B.grid(row=5, column=6, columnspan=2)
N.grid(row=5, column=7, columnspan=2)
M.grid(row=5, column=8, columnspan=2)
coma.grid(row=5, column=9, columnspan=2)
dot.grid(row=5, column=10, columnspan=2)

Shift_2.grid(row=5, column=12, columnspan=2)
or_slash.grid(row=5, column=11, columnspan=2)

Control.grid(row=6, column=0, columnspan=2)

windows.grid(row=6, column=1, columnspan=2)

Alt.grid(row=6, column=1, columnspan=5)

Space.grid(row=6, column=1, columnspan=12)

AltGr.grid(row=6, column=5, columnspan=14)

windows_2.grid(row=6, column=8, columnspan=18)

Fn.grid(row=6, column=11, columnspan=22)

Ctrl_2.grid(row=6, column=13, columnspan=3)

root.mainloop()
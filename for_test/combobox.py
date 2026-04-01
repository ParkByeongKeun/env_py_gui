import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Dongpakka coding")
root.geometry("800x480")

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.current(0)
combobox.pack()
combobox.set('카드 결제일')   # 최초 목록 제목 설정

combobox1 = ttk.Combobox(root, width=60,height=20, values=values, state='readonly')
combobox1.pack()
combobox1.set('카드 결제일')   # 최초 목록 제목 설정

def btncmd():
  print(combobox.get())

btn = Button(root, text='주문', command=btncmd)

btn.pack()
root.mainloop()
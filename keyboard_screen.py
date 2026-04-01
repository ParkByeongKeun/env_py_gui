import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class KeyboardScreen(ttk.Frame):
    def __init__(self, parent, controller, my_entry, show_wifi_detail):
        super().__init__(parent)
        self.controller = controller
        self.capslock_state = False
        self.my_entry = my_entry
        self.show_wifi_detail = show_wifi_detail

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.columnconfigure(0, weight=1)

        self.pw_entry = Entry(self)
        self.pw_entry.grid(row=0, column=0,sticky='NEWS')

        keyboard_part = Frame(self, bg='red')
        keyboard_part.grid(row=1, column=0, sticky="NEWS")

        keyboard_part.rowconfigure(0, weight=3)
        keyboard_part.rowconfigure(1, weight=3)
        keyboard_part.rowconfigure(2, weight=3)
        keyboard_part.rowconfigure(3, weight=3)
        keyboard_part.rowconfigure(4, weight=2)
        keyboard_part.columnconfigure(0, weight=1)

        # ~ 1 2 3 4 5 6 7 8 9 0 - = backspace
        # ` ! @ # $ % ^ & * ( ) _ + backspace
        first_line_frame = Frame(keyboard_part, bg='black')
        first_line_frame.grid(row=0,column=0, sticky='NEWS')
        # q w e r t y u i o p [ ] \
        # Q W E R T Y U I O P { } |
        second_line_frame = Frame(keyboard_part, bg='green')
        second_line_frame.grid(row=1,column=0, sticky='NEWS')
        # capslock a s d f g h j k l ; ' enter
        # capslock A S D F G H J K L : " enter
        third_line_frame = Frame(keyboard_part, bg = 'yellow')
        third_line_frame.grid(row=2,column=0, sticky='NEWS')
        # shift z x c v b n m , . / shift
        # shift Z X C V B N M < > ? shift
        fourth_line_frame = Frame(keyboard_part, bg='blue')
        fourth_line_frame.grid(row=3,column=0, sticky='NEWS')
        # Back spacebar 입력
        fifth_line_frame = Frame(keyboard_part, bg='cyan')
        fifth_line_frame.grid(row=4,column=0, sticky='NEWS')

        # ~ 1 2 3 4 5 6 7 8 9 0 - = backspace
        # ` ! @ # $ % ^ & * ( ) _ + backspace
        first_line_frame.columnconfigure(0, weight=1)              # `             ~      
        first_line_frame.columnconfigure(1, weight=1)              # 1             !           
        first_line_frame.columnconfigure(2, weight=1)              # 2             @          
        first_line_frame.columnconfigure(3, weight=1)              # 3             #         
        first_line_frame.columnconfigure(4, weight=1)              # 4             $        
        first_line_frame.columnconfigure(5, weight=1)              # 5             %       
        first_line_frame.columnconfigure(6, weight=1)              # 6             ^      
        first_line_frame.columnconfigure(7, weight=1)              # 7             &     
        first_line_frame.columnconfigure(8, weight=1)              # 8             *    
        first_line_frame.columnconfigure(9, weight=1)              # 9             (   
        first_line_frame.columnconfigure(10, weight=1)             # 0             )  
        first_line_frame.columnconfigure(11, weight=1)             # -             _  
        first_line_frame.columnconfigure(12, weight=1)             # =             + 
        first_line_frame.columnconfigure(13, weight=2)             # backspace     backspace
        first_line_frame.rowconfigure(0, weight=1)

        # q w e r t y u i o p [ ] \
        # Q W E R T Y U I O P { } |
        second_line_frame.columnconfigure(0, weight=1)             # 공백
        second_line_frame.columnconfigure(1, weight=1)             # q            Q
        second_line_frame.columnconfigure(2, weight=1)             # w            W
        second_line_frame.columnconfigure(3, weight=1)             # e            E
        second_line_frame.columnconfigure(4, weight=1)             # r            R
        second_line_frame.columnconfigure(5, weight=1)             # t            T
        second_line_frame.columnconfigure(6, weight=1)             # y            Y
        second_line_frame.columnconfigure(7, weight=1)             # u            U
        second_line_frame.columnconfigure(8, weight=1)             # i            I
        second_line_frame.columnconfigure(9, weight=1)             # o            O
        second_line_frame.columnconfigure(10, weight=1)            # p            P
        second_line_frame.columnconfigure(11, weight=1)            # [            {
        second_line_frame.columnconfigure(12, weight=1)            # ]            }
        second_line_frame.columnconfigure(13, weight=2)            # \            |
        second_line_frame.rowconfigure(0, weight=1)
        

        # capslock a s d f g h j k l ; ' enter
        # capslock A S D F G H J K L : " enter
        third_line_frame.columnconfigure(0, weight=3)              # capslock      capsloc
        third_line_frame.columnconfigure(1, weight=2)              # a             A
        third_line_frame.columnconfigure(2, weight=2)              # s             S
        third_line_frame.columnconfigure(3, weight=2)              # d             D
        third_line_frame.columnconfigure(4, weight=2)              # f             F
        third_line_frame.columnconfigure(5, weight=2)              # g             G
        third_line_frame.columnconfigure(6, weight=2)              # h             H
        third_line_frame.columnconfigure(7, weight=2)              # j             J
        third_line_frame.columnconfigure(8, weight=2)              # k             K
        third_line_frame.columnconfigure(9, weight=2)              # l             L
        third_line_frame.columnconfigure(10, weight=2)             # ;             :
        third_line_frame.columnconfigure(11, weight=2)             # '             "
        third_line_frame.columnconfigure(12, weight=5)             # enter         enter
        third_line_frame.rowconfigure(0, weight=1)

        # shift z x c v b n m , . / shift
        # shift Z X C V B N M < > ? shift
        fourth_line_frame.columnconfigure(0, weight=2)
        fourth_line_frame.columnconfigure(1, weight=1)
        fourth_line_frame.columnconfigure(2, weight=1)
        fourth_line_frame.columnconfigure(3, weight=1)
        fourth_line_frame.columnconfigure(4, weight=1)
        fourth_line_frame.columnconfigure(5, weight=1)
        fourth_line_frame.columnconfigure(6, weight=1)
        fourth_line_frame.columnconfigure(7, weight=1)
        fourth_line_frame.columnconfigure(8, weight=1)
        fourth_line_frame.columnconfigure(9, weight=1)
        fourth_line_frame.columnconfigure(10, weight=1)
        fourth_line_frame.columnconfigure(11, weight=3)
        fourth_line_frame.rowconfigure(0, weight=1)


        # Back spacebar 입력
        fifth_line_frame.columnconfigure(0, weight=1)
        fifth_line_frame.columnconfigure(1, weight=5)
        fifth_line_frame.columnconfigure(2, weight=2)
        fifth_line_frame.rowconfigure(0, weight=1)

        

        # first_line_frame
        # self.Btn(first_line_frame, 0, 0, '~')
        # self.Btn(first_line_frame, 0, 1, '1')
        # self.Btn(first_line_frame, 0, 2, '2')
        # self.Btn(first_line_frame, 0, 3, '3')
        # self.Btn(first_line_frame, 0, 4, '4')
        # self.Btn(first_line_frame, 0, 5, '5')
        # self.Btn(first_line_frame, 0, 6, '6')
        # self.Btn(first_line_frame, 0, 7, '7')
        # self.Btn(first_line_frame, 0, 8, '8')
        # self.Btn(first_line_frame, 0, 9, '9')
        # self.Btn(first_line_frame, 0, 10, '0')
        # self.Btn(first_line_frame, 0, 11, '-')
        # self.Btn(first_line_frame, 0, 12, '=')
        # self.Btn(first_line_frame, 0, 13, '<-Del')

        self.Btn_wave = Button(first_line_frame, text='~', command=lambda: self.Btn_click('~'),font=('Arial', 10),bg='black', fg='white')
        self.Btn_wave.grid(row=0, column=0, sticky='NEWS')
        self.Btn_1 = Button(first_line_frame, text='1', command=lambda: self.Btn_click('1'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_1.grid(row=0, column=1, sticky='NEWS')
        self.Btn_2 = Button(first_line_frame, text='2', command=lambda: self.Btn_click('2'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_2.grid(row=0, column=2, sticky='NEWS')
        self.Btn_3 = Button(first_line_frame, text='3', command=lambda: self.Btn_click('3'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_3.grid(row=0, column=3, sticky='NEWS')
        self.Btn_4 = Button(first_line_frame, text='4', command=lambda: self.Btn_click('4'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_4.grid(row=0, column=4, sticky='NEWS')
        self.Btn_5 = Button(first_line_frame, text='5', command=lambda: self.Btn_click('5'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_5.grid(row=0, column=5, sticky='NEWS')
        self.Btn_6 = Button(first_line_frame, text='6', command=lambda: self.Btn_click('6'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_6.grid(row=0, column=6, sticky='NEWS')
        self.Btn_7 = Button(first_line_frame, text='7', command=lambda: self.Btn_click('7'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_7.grid(row=0, column=7, sticky='NEWS')
        self.Btn_8 = Button(first_line_frame, text='8', command=lambda: self.Btn_click('8'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_8.grid(row=0, column=8, sticky='NEWS')
        self.Btn_9 = Button(first_line_frame, text='9', command=lambda: self.Btn_click('9'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_9.grid(row=0, column=9, sticky='NEWS')
        self.Btn_0 = Button(first_line_frame, text='0', command=lambda: self.Btn_click('0'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_0.grid(row=0, column=10, sticky='NEWS')
        self.Btn_Minus = Button(first_line_frame, text='-', font=('Arial', 10), command=lambda: self.Btn_click('-'), bg='black', fg='white')
        self.Btn_Minus.grid(row=0, column=11, sticky='NEWS')
        self.Btn_equal= Button(first_line_frame, text='=', font=('Arial', 10), command=lambda: self.Btn_click('='), bg='black', fg='white')
        self.Btn_equal.grid(row=0, column=12, sticky='NEWS')
        self.Btn_Backspace = Button(first_line_frame, text='<-del', font=('Arial', 10), bg='black', fg='white', command=self.delete_one_word)
        self.Btn_Backspace.grid(row=0, column=13, sticky='NEWS')

        # second_line_frame
        
        # self.Btn(second_line_frame, 0, 0, '')
        # self.Btn(second_line_frame, 0, 1, 'q')
        # self.Btn(second_line_frame, 0, 2, 'w')
        # self.Btn(second_line_frame, 0, 3, 'e')
        # self.Btn(second_line_frame, 0, 4, 'r')
        # self.Btn(second_line_frame, 0, 5, 't')
        # self.Btn(second_line_frame, 0, 6, 'y')
        # self.Btn(second_line_frame, 0, 7, 'u')
        # self.Btn(second_line_frame, 0, 8, 'i')
        # self.Btn(second_line_frame, 0, 9, 'o')
        # self.Btn(second_line_frame, 0, 10, 'p')
        # self.Btn(second_line_frame, 0, 11, '[')
        # self.Btn(second_line_frame, 0, 12, ']')
        # self.Btn(second_line_frame, 0, 13, '\\')


        self.Btn_empty = Label(second_line_frame, text='', font=('Arial',10), bg='black', fg='white')
        self.Btn_empty.grid(row=0, column=0, sticky='NEWS')
        self.Btn_Q = Button(second_line_frame, text='q',command=lambda:self.Btn_click('q'), font=('Arial',10), bg='black', fg='white')
        self.Btn_Q.grid(row=0, column=1, sticky='NEWS')
        self.Btn_W = Button(second_line_frame, text='w',command=lambda:self.Btn_click('w'), font=('Arial',10), bg='black', fg='white')
        self.Btn_W.grid(row=0, column=2, sticky='NEWS')
        self.Btn_E = Button(second_line_frame, text='e',command=lambda:self.Btn_click('e'), font=('Arial',10), bg='black', fg='white')
        self.Btn_E.grid(row=0, column=3, sticky='NEWS')
        self.Btn_R = Button(second_line_frame, text='r',command=lambda:self.Btn_click('r'), font=('Arial',10), bg='black', fg='white')
        self.Btn_R.grid(row=0, column=4, sticky='NEWS')
        self.Btn_T = Button(second_line_frame, text='t',command=lambda:self.Btn_click('t'), font=('Arial',10), bg='black', fg='white')
        self.Btn_T.grid(row=0, column=5, sticky='NEWS')
        self.Btn_Y = Button(second_line_frame, text='y',command=lambda:self.Btn_click('y'), font=('Arial',10), bg='black', fg='white')
        self.Btn_Y.grid(row=0, column=6, sticky='NEWS')
        self.Btn_U = Button(second_line_frame, text='u',command=lambda:self.Btn_click('u'), font=('Arial',10), bg='black', fg='white')
        self.Btn_U.grid(row=0, column=7, sticky='NEWS')
        self.Btn_I = Button(second_line_frame, text='i',command=lambda:self.Btn_click('i'), font=('Arial',10), bg='black', fg='white')
        self.Btn_I.grid(row=0, column=8, sticky='NEWS')
        self.Btn_O = Button(second_line_frame, text='o',command=lambda:self.Btn_click('o'), font=('Arial',10), bg='black', fg='white')
        self.Btn_O.grid(row=0, column=9, sticky='NEWS')
        self.Btn_P = Button(second_line_frame, text='p',command=lambda:self.Btn_click('p'), font=('Arial',10), bg='black', fg='white')
        self.Btn_P.grid(row=0, column=10, sticky='NEWS')
        self.Btn_l_bra = Button(second_line_frame, text='[',command=lambda:self.Btn_click('['), font=('Arial', 10), bg='black', fg='white')
        self.Btn_l_bra.grid(row=0, column=11, sticky='NEWS')
        self.Btn_r_bra = Button(second_line_frame, text=']',command=lambda:self.Btn_click(']'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_r_bra.grid(row=0, column=12, sticky='NEWS')
        self.Btn_won = Button(second_line_frame, text='\\',command=lambda:self.Btn_click('\\'), font=('Arial',10), bg='black', fg='white')
        self.Btn_won.grid(row=0, column=13, sticky='NEWS')

        # third_line_frame
        # self.Btn(third_line_frame, 0, 0, 'capslock')
        # self.Btn(third_line_frame, 0, 1, 'a')
        # self.Btn(third_line_frame, 0, 2, 's')
        # self.Btn(third_line_frame, 0, 3, 'd')
        # self.Btn(third_line_frame, 0, 4, 'f')
        # self.Btn(third_line_frame, 0, 5, 'g')
        # self.Btn(third_line_frame, 0, 6, 'h')
        # self.Btn(third_line_frame, 0, 7, 'j')
        # self.Btn(third_line_frame, 0, 8, 'k')
        # self.Btn(third_line_frame, 0, 9, 'l')
        # self.Btn(third_line_frame, 0, 10, ';')
        # self.Btn(third_line_frame, 0, 11, "'")
        # self.Btn(third_line_frame, 0, 12, 'Enter')



        self.Btn_capslock = Button(third_line_frame, text='capslock', font=('Arial',10), bg='black', fg='white', command=self.toggle_capslock)
        self.Btn_capslock.grid(row=0, column=0, sticky='NEWS')
        self.Btn_A = Button(third_line_frame, text='a',command=lambda:self.Btn_click('a'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_A.grid(row=0, column=1, sticky='NEWS')
        self.Btn_S = Button(third_line_frame, text='s',command=lambda:self.Btn_click('s'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_S.grid(row=0, column=2, sticky='NEWS')
        self.Btn_D = Button(third_line_frame, text='d',command=lambda:self.Btn_click('d'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_D.grid(row=0, column=3, sticky='NEWS')
        self.Btn_F = Button(third_line_frame, text='f',command=lambda:self.Btn_click('f'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_F.grid(row=0, column=4, sticky='NEWS')
        self.Btn_G = Button(third_line_frame, text='g',command=lambda:self.Btn_click('g'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_G.grid(row=0, column=5, sticky='NEWS')
        self.Btn_H = Button(third_line_frame, text='h',command=lambda:self.Btn_click('h'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_H.grid(row=0, column=6, sticky='NEWS')
        self.Btn_J = Button(third_line_frame, text='j',command=lambda:self.Btn_click('j'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_J.grid(row=0, column=7, sticky='NEWS')
        self.Btn_K = Button(third_line_frame, text='k',command=lambda:self.Btn_click('k'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_K.grid(row=0, column=8, sticky='NEWS')
        self.Btn_L = Button(third_line_frame, text='l',command=lambda:self.Btn_click('l'), font=('Arial', 10), bg='black', fg='white')
        self.Btn_L.grid(row=0, column=9, sticky='NEWS')
        self.Btn_semi_col = Button(third_line_frame,text=';',command=lambda: self.Btn_click(';'), font=('Arial',10), bg='black', fg='white')
        self.Btn_semi_col.grid(row=0, column=10, sticky='NEWS')
        self.Btn_apo = Button(third_line_frame,text='\'',command=lambda: self.Btn_click("'"), font=('Arial',10), bg='black', fg='white')
        self.Btn_apo.grid(row=0, column=11, sticky='NEWS')
        self.Btn_enter = Button(third_line_frame, text='Enter', font=('Arial', 10), bg='black', fg='white', command=self.enter_func)
        self.Btn_enter.grid(row=0, column=12, sticky='NEWS')

        # fourth_line_frame
        # self.Btn(fourth_line_frame, 0, 0, 'shift')
        # self.Btn(fourth_line_frame, 0, 1, 'z')
        # self.Btn(fourth_line_frame, 0, 2, 'x')
        # self.Btn(fourth_line_frame, 0, 3, 'c')
        # self.Btn(fourth_line_frame, 0, 4, 'v')
        # self.Btn(fourth_line_frame, 0, 5, 'b')
        # self.Btn(fourth_line_frame, 0, 6, 'n')
        # self.Btn(fourth_line_frame, 0, 7, 'm')
        # self.Btn(fourth_line_frame, 0, 8, ',')
        # self.Btn(fourth_line_frame, 0, 9, '.')
        # self.Btn(fourth_line_frame, 0, 10, '/')
        # self.Btn(fourth_line_frame, 0, 11, 'shift')


        self.Btn_l_shift = Button(fourth_line_frame, text='shift', font=('Arial',10), bg='black', fg='white')
        self.Btn_l_shift.grid(row=0, column=0, sticky='NEWS')
        self.Btn_Z = Button(fourth_line_frame, text='z',command=lambda: self.Btn_click('z'), font=('Arial',10), bg='black', fg='white')
        self.Btn_Z.grid(row=0, column=1, sticky='NEWS')
        self.Btn_X = Button(fourth_line_frame, text='x',command=lambda: self.Btn_click('x'), font=('Arial',10), bg='black', fg='white')
        self.Btn_X.grid(row=0, column=2, sticky='NEWS')
        self.Btn_C = Button(fourth_line_frame, text='c',command=lambda: self.Btn_click('c'), font=('Arial',10), bg='black', fg='white')
        self.Btn_C.grid(row=0, column=3, sticky='NEWS')
        self.Btn_V = Button(fourth_line_frame, text='v',command=lambda: self.Btn_click('v'), font=('Arial',10), bg='black', fg='white')
        self.Btn_V.grid(row=0, column=4, sticky='NEWS')
        self.Btn_B = Button(fourth_line_frame, text='b',command=lambda: self.Btn_click('b'), font=('Arial',10), bg='black', fg='white')
        self.Btn_B.grid(row=0, column=5, sticky='NEWS')
        self.Btn_N = Button(fourth_line_frame, text='n',command=lambda: self.Btn_click('n'), font=('Arial',10), bg='black', fg='white')
        self.Btn_N.grid(row=0, column=6, sticky='NEWS')
        self.Btn_M = Button(fourth_line_frame, text='m',command=lambda: self.Btn_click('m'), font=('Arial',10), bg='black', fg='white')
        self.Btn_M.grid(row=0, column=7, sticky='NEWS')
        self.Btn_comma = Button(fourth_line_frame,text=',',command=lambda: self.Btn_click(','), font=('Arial',10), bg='black', fg='white')
        self.Btn_comma.grid(row=0, column=8, sticky='NEWS')
        self.Btn_period = Button(fourth_line_frame,text='.', command=lambda: self.Btn_click('.'), font=('Arial',10), bg='black', fg='white')
        self.Btn_period.grid(row=0, column=9, sticky='NEWS')
        self.Btn_slash = Button(fourth_line_frame,text='/', command=lambda: self.Btn_click('/'), font=('Arial',10), bg='black', fg='white')
        self.Btn_slash.grid(row=0, column=10, sticky='NEWS')
        self.Btn_r_shift = Button(fourth_line_frame, text='shift', font=('Arial',10), bg='black', fg='white')
        self.Btn_r_shift.grid(row=0, column=11, sticky='NEWS')


        # fifth_line_frame
        # self.Btn(fifth_line_frame, 0, 0, '')
        # self.Btn(fifth_line_frame, 0, 1, 'space bar')
        # self.Btn(fifth_line_frame, 0, 2, 'Connect')
        
        # self.Btn_fif_empty = Label(fifth_line_frame, bg='black')
        # self.Btn_fif_empty.grid(row=0, column=0, sticky='NEWS')
        self.Btn_back = Button(fifth_line_frame, text='Back', font=('Arial', 10), bg='black', fg='white',command=show_wifi_detail)
        self.Btn_back.grid(row=0, column=0, sticky='NEWS')
        self.Btn_spacebar = Button(fifth_line_frame, text='space bar', font=('Arial',10), bg='black', fg='white', command=self.spacebar_click)
        self.Btn_spacebar.grid(row=0, column=1, sticky='NEWS')
        self.Btn_connect = Button(fifth_line_frame, text='Connect', font=('Arial', 15), bg='black', fg='white', command= self.connect_func)
        self.Btn_connect.grid(row=0, column=2, sticky='NEWS')
    
    def Btn(self, frame, row, column, content):
        Button(frame, text=content, font=('Arial', 10), fg='white', bg='black', command=lambda: self.Btn_click(content)).grid(row=row, column=column, sticky='NEWS')
        # return Button(frame, text=content, font=('Arial', 10), fg='white', bg='black', command=lambda: self.Btn_click(content)).grid(row=row, column=column, sticky='NEWS')

    # def func_btn(self, frame, row, column):


    def toggle_capslock(self):
        if self.capslock_state:
            self.capslock_state = False
            self.Btn_wave.config(text='~', command=lambda:self.Btn_click('~'))
            self.Btn_1.config(text='1', command=lambda:self.Btn_click('1'))
            self.Btn_2.config(text='2', command=lambda:self.Btn_click('2'))
            self.Btn_3.config(text='3', command=lambda:self.Btn_click('3'))
            self.Btn_4.config(text='4', command=lambda:self.Btn_click('4'))
            self.Btn_5.config(text='5', command=lambda:self.Btn_click('5'))
            self.Btn_6.config(text='6', command=lambda:self.Btn_click('6'))
            self.Btn_7.config(text='7', command=lambda:self.Btn_click('7'))
            self.Btn_8.config(text='8', command=lambda:self.Btn_click('8'))
            self.Btn_9.config(text='9', command=lambda:self.Btn_click('9'))
            self.Btn_0.config(text='0', command=lambda:self.Btn_click('0'))
            self.Btn_Minus.config(text='-', command=lambda:self.Btn_click('-'))
            self.Btn_equal.config(text='=', command=lambda:self.Btn_click('='))
            self.Btn_Backspace.config(text='<-del')
            self.Btn_empty.config(text='')
            self.Btn_Q.config(text='q', command=lambda: self.Btn_click('q'))
            self.Btn_W.config(text='w', command=lambda: self.Btn_click('w'))
            self.Btn_E.config(text='e', command=lambda: self.Btn_click('e'))
            self.Btn_R.config(text='r', command=lambda: self.Btn_click('r'))
            self.Btn_T.config(text='t', command=lambda: self.Btn_click('t'))
            self.Btn_Y.config(text='y', command=lambda: self.Btn_click('y'))
            self.Btn_U.config(text='u', command=lambda: self.Btn_click('u'))
            self.Btn_I.config(text='i', command=lambda: self.Btn_click('i'))
            self.Btn_O.config(text='o', command=lambda: self.Btn_click('o'))
            self.Btn_P.config(text='p', command=lambda: self.Btn_click('p'))
            self.Btn_l_bra.config(text='[', command=lambda: self.Btn_click('['))
            self.Btn_r_bra.config(text=']', command=lambda: self.Btn_click(']'))
            self.Btn_won.config(text='\\', command=lambda: self.Btn_click('\\'))
            self.Btn_capslock.config(text='capslock')
            self.Btn_A.config(text='a',command=lambda:self.Btn_click('a'))
            self.Btn_S.config(text='s',command=lambda:self.Btn_click('s'))
            self.Btn_D.config(text='d',command=lambda:self.Btn_click('d'))
            self.Btn_F.config(text='f',command=lambda:self.Btn_click('f'))
            self.Btn_G.config(text='g',command=lambda:self.Btn_click('g'))
            self.Btn_H.config(text='h',command=lambda:self.Btn_click('h'))
            self.Btn_J.config(text='j',command=lambda:self.Btn_click('j'))
            self.Btn_K.config(text='k',command=lambda:self.Btn_click('k'))
            self.Btn_L.config(text='l',command=lambda:self.Btn_click('l'))
            self.Btn_semi_col.config(text=';',command=lambda:self.Btn_click(';'))
            self.Btn_apo.config(text="'",command=lambda:self.Btn_click("'"))
            self.Btn_enter.config(text='Enter')
            self.Btn_l_shift.config(text='shift')
            self.Btn_Z.config(text='z',command=lambda:self.Btn_click('z'))
            self.Btn_X.config(text='x',command=lambda:self.Btn_click('x'))
            self.Btn_C.config(text='c',command=lambda:self.Btn_click('c'))
            self.Btn_V.config(text='v',command=lambda:self.Btn_click('v'))
            self.Btn_B.config(text='b',command=lambda:self.Btn_click('b'))
            self.Btn_N.config(text='n',command=lambda:self.Btn_click('n'))
            self.Btn_M.config(text='m',command=lambda:self.Btn_click('m'))
            self.Btn_comma.config(text=',',command=lambda:self.Btn_click(','))
            self.Btn_period.config(text='.',command=lambda:self.Btn_click('.'))
            self.Btn_slash.config(text='/',command=lambda:self.Btn_click('/'))
            self.Btn_r_shift.config(text='shift')
            self.Btn_fif_empty.config(text='')
            self.Btn_spacebar.config(text='space bar')
            self.Btn_connect.config(text='Connect')

        else:
            self.capslock_state = True
            self.Btn_wave.config(text='`', command=lambda:self.Btn_click('`'))
            self.Btn_1.config(text='!', command=lambda:self.Btn_click('!'))
            self.Btn_2.config(text='@', command=lambda:self.Btn_click('@'))
            self.Btn_3.config(text='#', command=lambda:self.Btn_click('#'))
            self.Btn_4.config(text='$', command=lambda:self.Btn_click('$'))
            self.Btn_5.config(text='%', command=lambda:self.Btn_click('%'))
            self.Btn_6.config(text='^', command=lambda:self.Btn_click('^'))
            self.Btn_7.config(text='&', command=lambda:self.Btn_click('&'))
            self.Btn_8.config(text='*', command=lambda:self.Btn_click('*'))
            self.Btn_9.config(text='(', command=lambda:self.Btn_click('('))
            self.Btn_0.config(text=')', command=lambda:self.Btn_click(')'))
            self.Btn_Minus.config(text='_', command=lambda:self.Btn_click('_'))
            self.Btn_equal.config(text='+', command=lambda:self.Btn_click('+'))
            self.Btn_Backspace.config(text='<-del')
            self.Btn_empty.config(text='')
            self.Btn_Q.config(text='Q', command=lambda:self.Btn_click('Q'))
            self.Btn_W.config(text='W', command=lambda:self.Btn_click('W'))
            self.Btn_E.config(text='E', command=lambda:self.Btn_click('E'))
            self.Btn_R.config(text='R', command=lambda:self.Btn_click('R'))
            self.Btn_T.config(text='T', command=lambda:self.Btn_click('T'))
            self.Btn_Y.config(text='Y', command=lambda:self.Btn_click('Y'))
            self.Btn_U.config(text='U', command=lambda:self.Btn_click('U'))
            self.Btn_I.config(text='I', command=lambda:self.Btn_click('I'))
            self.Btn_O.config(text='O', command=lambda:self.Btn_click('O'))
            self.Btn_P.config(text='P', command=lambda:self.Btn_click('P'))
            self.Btn_l_bra.config(text='{', command=lambda:self.Btn_click('{'))
            self.Btn_r_bra.config(text='}', command=lambda:self.Btn_click('}'))
            self.Btn_won.config(text='|', command=lambda:self.Btn_click('|'))
            self.Btn_capslock.config(text='capslock')
            self.Btn_A.config(text='A', command=lambda:self.Btn_click('A'))
            self.Btn_S.config(text='S', command=lambda:self.Btn_click('S'))
            self.Btn_D.config(text='D', command=lambda:self.Btn_click('D'))
            self.Btn_F.config(text='F', command=lambda:self.Btn_click('F'))
            self.Btn_G.config(text='G', command=lambda:self.Btn_click('G'))
            self.Btn_H.config(text='H', command=lambda:self.Btn_click('H'))
            self.Btn_J.config(text='J', command=lambda:self.Btn_click('J'))
            self.Btn_K.config(text='K', command=lambda:self.Btn_click('K'))
            self.Btn_L.config(text='L', command=lambda:self.Btn_click('L'))
            self.Btn_semi_col.config(text=':', command=lambda:self.Btn_click(':'))
            self.Btn_apo.config(text='"', command=lambda:self.Btn_click('"'))
            self.Btn_enter.config(text='Enter')
            self.Btn_l_shift.config(text='shift')
            self.Btn_Z.config(text='Z', command=lambda:self.Btn_click('Z'))
            self.Btn_X.config(text='X', command=lambda:self.Btn_click('X'))
            self.Btn_C.config(text='C', command=lambda:self.Btn_click('C'))
            self.Btn_V.config(text='V', command=lambda:self.Btn_click('V'))
            self.Btn_B.config(text='B', command=lambda:self.Btn_click('B'))
            self.Btn_N.config(text='N', command=lambda:self.Btn_click('N'))
            self.Btn_M.config(text='M', command=lambda:self.Btn_click('M'))
            self.Btn_comma.config(text='<', command=lambda:self.Btn_click('<'))
            self.Btn_period.config(text='>', command=lambda:self.Btn_click('>'))
            self.Btn_slash.config(text='?', command=lambda:self.Btn_click('?'))
            self.Btn_r_shift.config(text='shift')
            self.Btn_fif_empty.config(text='')
            self.Btn_spacebar.config(text='space bar')
            self.Btn_connect.config(text='Connect')

    # def shift_func(self):
    #     self.

    def delete_one_word(self):
        current = self.pw_entry.get()
        self.pw_entry.delete(0, END)
        self.pw_entry.insert(0, str(current)[0:-1])

    def spacebar_click(self):
        current = self.pw_entry.get()
        self.pw_entry.delete(0, END)
        self.pw_entry.insert(0, str(current)+str(' '))

    def Btn_click(self, alphabet):
        current = self.pw_entry.get()
        self.pw_entry.delete(0, END)
        self.pw_entry.insert(0, str(current)+str(alphabet))

    def enter_func(self):
        self.controller.wifi_pw = self.pw_entry.get()
        # print(self.controller.wifi_pw)
        self.my_entry.delete(0, END)
        self.my_entry.insert(0, str(self.pw_entry.get()))
        self.show_wifi_detail()

    def connect_func(self):
        self.controller.wifi_pw = self.pw_entry.get()
        # print(self.controller.wifi_pw)
        self.my_entry.delete(0, END)
        self.my_entry.insert(0, str(self.pw_entry.get()))
        self.show_wifi_detail()
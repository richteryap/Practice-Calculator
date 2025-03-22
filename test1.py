import tkinter as tk

root = tk.Tk()
root.title('Calculus-Powered Graphing App')
root.geometry('350x250')

appLayout = tk.Frame(root)
appLayout.pack()

bottonFrame = tk.Frame(appLayout)
bottonFrame.grid()

# number bottons
botton7 = tk.Button(bottonFrame, text='7', command=lambda: print('7'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton7.grid(row=0, column=0, padx=1, pady=1)

botton8 = tk.Button(bottonFrame, text='8', command=lambda: print('8'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton8.grid(row=0, column=1, padx=1, pady=1)

botton9 = tk.Button(bottonFrame, text='9', command=lambda: print('9'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton9.grid(row=0, column=2, padx=1, pady=1)

botton4 = tk.Button(bottonFrame, text='4', command=lambda: print('4'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton4.grid(row=1, column=0, padx=1, pady=1)

botton5 = tk.Button(bottonFrame, text='5', command=lambda: print('5'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton5.grid(row=1, column=1, padx=1, pady=1)

botton6 = tk.Button(bottonFrame, text='6', command=lambda: print('6'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton6.grid(row=1, column=2, padx=1, pady=1)

botton1 = tk.Button(bottonFrame, text='1', command=lambda: print('1'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton1.grid(row=2, column=0, padx=1, pady=1)

botton2 = tk.Button(bottonFrame, text='2', command=lambda: print('2'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton2.grid(row=2, column=1, padx=1, pady=1)

botton3 = tk.Button(bottonFrame, text='3', command=lambda: print('3'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton3.grid(row=2, column=2, padx=1, pady=1)

botton0 = tk.Button(bottonFrame, text='0', command=lambda: print('0'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
botton0.grid(row=3, column=0, padx=1, pady=1)

bottonDot = tk.Button(bottonFrame, text='.', command=lambda: print('.'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
bottonDot.grid(row=3, column=1, padx=1, pady=1)

bottonEqual = tk.Button(bottonFrame, text='=', command=lambda: print('='), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
bottonEqual.grid(row=3, column=2, padx=1, pady=1)

# operator bottons
bottonAdd = tk.Button(bottonFrame, text='+', command=lambda: print('+'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
bottonAdd.grid(row=3, column=3, padx=1, pady=1)

bottonSub = tk.Button(bottonFrame, text='-', command=lambda: print('-'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
bottonSub.grid(row=2, column=3, padx=1, pady=1)

bottonMul = tk.Button(bottonFrame, text='*', command=lambda: print('*'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
bottonMul.grid(row=1, column=3, padx=1, pady=1)

bottonDiv = tk.Button(bottonFrame, text='/', command=lambda: print('/'), font = ('Courier New', 15), cursor = 'hand2', bd=1,
                                 relief = 'flat', overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black', width=5)
bottonDiv.grid(row=0, column=3, padx=1, pady=1)

root.mainloop()
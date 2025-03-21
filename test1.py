import tkinter as tk

root = tk.Tk()
root.title('Calculus-Powered Graphing App')
root.geometry('350x250')

bottonFrame = tk.Frame(root)
bottonFrame.pack()

botton1 = tk.Button(bottonFrame, text='Click Me!', command=lambda: print('Hello World!'))
botton1.grid(row=0, column=0)

botton2 = tk.Button(bottonFrame, text='Click Me!', command=lambda: print('Hello World!'))
botton2.grid(row=1, column=0)

botton3 = tk.Button(bottonFrame, text='Click Me!', command=lambda: print('Hello World!'))
botton3.grid(row=0, column=1)

root.mainloop()
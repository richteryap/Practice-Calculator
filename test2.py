import tkinter as tk

root = tk.Tk()
root.title('Calculus-Powered Graphing App')
root.geometry('625x265')

appLayout = tk.Frame(root)
appLayout.pack()

# Screen
screen = tk.Entry(appLayout, font=('Courier New', 15), bg='white', fg='black', width=50, bd=5, relief='flat', justify='right')
screen.grid(row=0, column=0, columnspan=2, pady=5)

# Buttons layout
buttonFrameTop0=tk.Frame(appLayout, bg='white')
buttonFrameTop0.grid(row=1, column=0, pady=5)

buttonFunctions = tk.Button(buttonFrameTop0, text='functions', command=lambda: print('functions'),
                            font = ('Courier New', 15), cursor = 'hand2', bd=1, relief = 'flat',
                            overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black',
                            width=11)
buttonFunctions.grid(row=0, column=0, sticky='e')

buttonFrameTop1=tk.Frame(appLayout, bg='white')
buttonFrameTop1.grid(row=1, column=1, pady=5)

buttonTop2 = [
    ['AC', '<==', '==>', 'C']
]

for r, row in enumerate(buttonTop2):
    for c, char in enumerate(row):
        tk.Button(
            buttonFrameTop1, text=char, command=lambda ch=char: print(ch),
            font=('Courier New', 15), cursor='hand2', bd=1,
            relief='flat', overrelief='flat', justify='center',
            bg='gainsboro', fg='black', width=5
        ).grid(row=r, column=c, padx=1, pady=1)

# Button1 Layout
buttonFrame1 = tk.Frame(appLayout, bg='white')
buttonFrame1.grid(row=2, column=1, padx=5, pady=2)

buttons1 = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for r, row in enumerate(buttons1):
    for c, char in enumerate(row):
        tk.Button(
            buttonFrame1, text=char, command=lambda ch=char: print(ch),
            font=('Courier New', 15), cursor='hand2', bd=1,
            relief='flat', overrelief='flat', justify='center',
            bg='gainsboro', fg='black', width=5
        ).grid(row=r, column=c, padx=1, pady=1)

# Button2 layout
buttonFrame2 = tk.Frame(appLayout, bg='white')
buttonFrame2.grid(row=2, column=0, padx=5, pady=2)

buttons2 = [
    ['x', 'y', 'a^2', 'a^b'],
    ['(', ')', '<', '>'],
    ['log', 'e', '<=', '>='],
    ['ln', ',', 'sqrt', 'pi']
]

for r, row in enumerate(buttons2):
    for c, char in enumerate(row):
        tk.Button(
            buttonFrame2, text=char, command=lambda ch=char: print(ch),
            font=('Courier New', 15), cursor='hand2', bd=1,
            relief='flat', overrelief='flat', justify='center',
            bg='gainsboro', fg='black', width=5
        ).grid(row=r, column=c, padx=1, pady=1)

root.mainloop()
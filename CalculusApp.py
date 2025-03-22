import tkinter as tk

root = tk.Tk()
root.title('Calculus-Powered Graphing App')
root.geometry('625x265')

appLayout = tk.Frame(root)
appLayout.pack()


# Screen
screen = tk.Entry(appLayout, font=('Courier New', 15), bg='white', fg='black',
                  width=50, bd=5, relief='flat', justify='right')
screen.grid(row=0, column=0, columnspan=2, pady=5)


# Button Format
def create_button(parent, text, row, col):
    tk.Button(
        parent, text=text, command=lambda: print(text),
        font=('Courier New', 15), cursor='hand2', bd=1,
        relief='flat', overrelief='flat', justify='center',
        bg='gainsboro', fg='black', width=5
    ).grid(row=row, column=col, padx=1, pady=1)


# Top Buttons
buttonFrameTopLeft=tk.Frame(appLayout, bg='white')
buttonFrameTopLeft.grid(row=1, column=0, pady=5)

buttonFunctions = tk.Button(buttonFrameTopLeft, text='functions', command=lambda: print('functions'),
                            font = ('Courier New', 15), cursor = 'hand2', bd=1, relief = 'flat',
                            overrelief = 'flat', justify = 'center', bg='gainsboro', fg='black',
                            width=11)
buttonFunctions.grid(row=0, column=0, sticky='e')

buttonFrameTopRight=tk.Frame(appLayout, bg='white')
buttonFrameTopRight.grid(row=1, column=1, pady=5)

top_buttons = ['AC', '<==', '==>', 'C']

for c, char in enumerate(top_buttons):
    create_button(buttonFrameTopRight, char, 0, c)


# Button Functions
buttonFrameLeft = tk.Frame(appLayout, bg='white')
buttonFrameLeft.grid(row=2, column=0, padx=5, pady=2)

left_buttons = [
    ['x', 'y', 'a^2', 'a^b'],
    ['(', ')', '<', '>'],
    ['log', 'e', '<=', '>='],
    ['ln', ',', 'sqrt', 'pi']
]

for r, row in enumerate(left_buttons):
    for c, char in enumerate(row):
        create_button(buttonFrameLeft, char, r, c)


# Button Numbers
buttonFrameRight = tk.Frame(appLayout, bg='white')
buttonFrameRight.grid(row=2, column=1, padx=5, pady=2)

right_buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for r, row in enumerate(right_buttons):
    for c, char in enumerate(row):
        create_button(buttonFrameRight, char, r, c)

root.mainloop()

import tkinter as tk
import math
import sympy as sp

root = tk.Tk()
root.title('Calculus-Powered Graphing App')
root.geometry('625x265')

appLayout = tk.Frame(root)
appLayout.pack()

screen = tk.Entry(appLayout, font=('Courier New', 15), bg='white', fg='black',
                  width=50, bd=5, relief='flat', justify='right')
screen.grid(row=0, column=0, columnspan=2, pady=5)

real_expression = ""

def on_button_click(text):
    global real_expression

    if text == 'AC':
        screen.delete(0, tk.END)
        real_expression = ""
    elif text == 'C':
        if real_expression == "Error":
            screen.delete(0, tk.END)
            real_expression = ""
            return
        screen.delete(len(screen.get()) - 1, tk.END)
        real_expression = real_expression[:-1]
    elif text == '◄':
        current_pos = screen.index(tk.INSERT)
        if current_pos > 0:
            screen.icursor(current_pos - 1)
    elif text == '►':
        current_pos = screen.index(tk.INSERT)
        if current_pos < len(screen.get()):
            screen.icursor(current_pos + 1)
    elif text == '=':
        open_parens = real_expression.count('(')
        close_parens = real_expression.count(')')

        if not real_expression:
            return
        if open_parens > close_parens:
            real_expression += ')' * (open_parens - close_parens)
        try:
            result = sp.sympify(real_expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
            real_expression = str(result)
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
            real_expression = "Error"
    elif text == 'a^2':
        screen.insert(tk.END, '^2')
        real_expression += '**2'
    elif text == 'a^b':
        screen.insert(tk.END, '^')
        real_expression += '**'
    elif text == '==':
        screen.insert(tk.END, '=')
        real_expression += '=='
    elif text == 'π':
        screen.insert(tk.END, 'π')
        real_expression += 'math.pi'
    elif text == '√x':
        screen.insert(tk.END, '√(')
        real_expression += 'math.sqrt('
    elif text == 'ⁿ√x':
        screen.insert(tk.END, 'ⁿ√(')
        real_expression += '**(1/'
    elif text == 'n!':
        screen.insert(tk.END, '!')
    
        i = len(real_expression) - 1
        while i >= 0 and real_expression[i].isdigit():
            i -= 1
    
        if i < len(real_expression) - 1:
            num = real_expression[i + 1:]
            real_expression = real_expression[:i + 1] + f'math.factorial({num})'
        else:
            real_expression += 'math.factorial('
    elif text == '|x|':
        screen.insert(tk.END, 'abs(')
        real_expression += 'math.fabs('
    elif text == '%':
        screen.insert(tk.END, '%')
        real_expression += '/100'
    elif text == '10^':
        screen.insert(tk.END, '10^(')
        real_expression += '10**('
    elif text == 'e':
        screen.insert(tk.END, 'e')
        real_expression += 'math.e'
    elif text == 'ln':
        screen.insert(tk.END, 'ln(')
        real_expression += 'math.log('
    elif text == 'log':
        screen.insert(tk.END, 'log(')
        real_expression += 'math.log10('
    elif text == 'mod':
        screen.insert(tk.END, 'mod')
        real_expression += '%'
    else:
        screen.insert(tk.END, text)
        real_expression += text

def create_button(parent, text, row, col):
    if text == '⬅':
        command = move_cursor_left
    elif text == '➡':
        command = move_cursor_right
    else:
        command = lambda: on_button_click(text)

    tk.Button(
        parent, text=text, command=command,
        font=('Courier New', 15), cursor='hand2', bd=1,
        relief='flat', overrelief='flat', justify='center',
        bg='gainsboro', fg='black', width=5
    ).grid(row=row, column=col, padx=1, pady=1)


buttonLayouts = {
    'Functions': [
        ['x', 'y', 'a^2', 'a^b'],
        ['(', ')', '<', '>'],
        ['{', '}', '<=', '>='],
        ['[', ']', ',', '==']
    ],
    'Calculus': [
        ['(', ')', 'a^2', 'a^b'],  
        ['√x', 'ⁿ√x', '10^', 'e'],  
        ['log', 'ln', 'π', 'mod'],  
        ['n!', '|x|', '%', ',']
    ],
    'Trigonometry': [
        ['sin', 'cos', 'tan', '('],
        ['sec', 'csc', 'cot', ')'],
        ['asin', 'acos', 'atan', 'x'],
        ['asec', 'acsc', 'acot', 'y']
    ],
}

def update_left_buttons(category):
    buttonFunctions.config(text=category)

    for widget in buttonFrameLeft.winfo_children():
        widget.destroy()

    layout = buttonLayouts.get(category, buttonLayouts['Functions'])

    for r, row in enumerate(layout):
        for c, char in enumerate(row):
            create_button(buttonFrameLeft, char, r, c)

buttonFrameTopLeft = tk.Frame(appLayout)
buttonFrameTopLeft.grid(row=1, column=0, pady=5)

buttonFrameTopLeftLeft = tk.Frame(buttonFrameTopLeft, bg='white')
buttonFrameTopLeftLeft.grid(row=0, column=0, padx=5)

buttonFunctions = tk.Menubutton(buttonFrameTopLeftLeft, text='Functions', font=('Courier New', 15), cursor='hand2',
                                bd=1, relief='flat', justify='center', bg='gainsboro', fg='black', width=12)
buttonFunctions.menu = tk.Menu(buttonFunctions, tearoff=0)
buttonFunctions["menu"] = buttonFunctions.menu
buttonFunctions.grid(row=0, column=0)

buttonFunctions.menu.add_command(label='FUNCTIONS', font=('Courier New', 13), command=lambda: update_left_buttons("Functions"))
buttonFunctions.menu.add_command(label='CALCULUS', font=('Courier New', 13), command=lambda: update_left_buttons("Calculus"))
buttonFunctions.menu.add_command(label='TRIGONOMETRY', font=('Courier New', 13), command=lambda: update_left_buttons("Trigonometry"))

buttonFrameTopLeftRight = tk.Frame(buttonFrameTopLeft, bg='white')
buttonFrameTopLeftRight.grid(row=0, column=1, padx=5)

buttonDerive = tk.Button(buttonFrameTopLeftRight, text='DERIVATION', command=lambda: print('Derive'),
                        font=('Courier New', 15), cursor='hand2', bd=1, relief='flat',
                        overrelief='flat', justify='center', bg='gainsboro', fg='black', width=10)
buttonDerive.grid(row=0, column=0)

buttonFrameLeft = tk.Frame(appLayout, bg='white')
buttonFrameLeft.grid(row=2, column=0, padx=5, pady=2)

update_left_buttons('Functions')

buttonFrameTopRight = tk.Frame(appLayout, bg='white')
buttonFrameTopRight.grid(row=1, column=1, pady=5)

top_buttons = ['AC', '◄', '►', 'C']

for c, char in enumerate(top_buttons):
    create_button(buttonFrameTopRight, char, 0, c)

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

def move_cursor_left(event=None):
    screen.icursor(screen.index(tk.INSERT) - 1)

def move_cursor_right(event=None):
    screen.icursor(screen.index(tk.INSERT) + 1)

def on_key_press(event):
    key = event.char
    if key in '0123456789+-*/().':
        screen.insert(tk.END, key)
    elif key == '\r':
        on_button_click('=')
    elif key == '\x08':
        on_button_click('C')

root.bind('<Left>', move_cursor_left)

root.bind('<Right>', move_cursor_right)

root.bind('<Key>', on_key_press)

root.mainloop()
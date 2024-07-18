import tkinter as tk
from tkinter import messagebox

def Metric():
    global metric
    root.withdraw()
    metric = tk.Tk()
    metric.title("METRIC")
    metric.geometry('350x280')

    def calculate_metric():
        h = eval(metric_entry_height.get())
        w = eval(metric_entry_weight.get())
        bmi = w/((h*h)*0.0001)
        bmistatus(bmi)

    metric_label = tk.Label(metric, text = 'METRIC', font = ('Courier New', 20))
    metric_label.pack(pady = 15)

    metric_info = tk.Label(metric, text = 'Input Info:', font = ('Courier New', 17))
    metric_info.pack()

    metric_info_frame = tk.Frame(metric)
    metric_info_frame.pack()

    metric_info_weight = tk.Label(metric_info_frame, text = 'WEIGHT(kg)', font = ('Courier New', 15))
    metric_info_weight.grid(row = 0, column = 0, pady = 1)

    metric_info_height = tk.Label(metric_info_frame, text = 'HEIGHT(cm)', font = ('Courier New', 15))
    metric_info_height.grid(row = 0, column = 1, pady = 1)

    metric_entry_weight = tk.Entry(metric_info_frame)
    metric_entry_weight.grid(row = 1, column = 0)

    metric_entry_height = tk.Entry(metric_info_frame)
    metric_entry_height.grid(row = 1, column = 1)

    calculate_button = tk.Button(metric, text = 'CALCULATE', font = ('Courier New', 20), cursor = 'hand2',
                                 relief = 'flat', overrelief = 'flat', justify = 'center',
                                 command = calculate_metric)
    calculate_button.pack(pady = 18)

    back_button = tk.Button(metric, text = 'BACK', font = ('Courier New', 8), cursor = 'hand2', relief = 'flat',
                            overrelief = 'flat', justify = 'center', command = destroym)
    back_button.pack()

def English():
    global english
    root.withdraw()
    english = tk.Tk()

    english.title("ENGLISH")
    english.geometry('350x280')

    def calculate_english():
        h = english_entry_height.get().split()
        w = eval(english_entry_weight.get())
        if len(h) != 2:
            messagebox.showinfo(title = 'Invalid Input', message = 'Please use this format: e.g. 5 6')
        else:
            ft = eval(h[0])
            inch = eval(h[1])
            all_inches = (ft*12)+inch
            bmi = (w/pow(all_inches, 2))*703
            bmistatus(bmi)

    english_label = tk.Label(english, text = 'ENGLISH', font = ('Courier New', 20))
    english_label.pack(pady = 15)

    english_info = tk.Label(english, text = 'Input Info:', font = ('Courier New', 17))
    english_info.pack()

    english_info_frame = tk.Frame(english)
    english_info_frame.pack()

    english_info_weight = tk.Label(english_info_frame, text = 'WEIGHT(lbs)', font = ('Courier New', 15))
    english_info_weight.grid(row = 0, column = 0, pady = 1)

    english_info_height = tk.Label(english_info_frame, text = 'HEIGHT(ft 5 6)', font = ('Courier New', 15))
    english_info_height.grid(row = 0, column = 1, pady = 1)

    english_entry_weight = tk.Entry(english_info_frame)
    english_entry_weight.grid(row = 1, column = 0)

    english_entry_height = tk.Entry(english_info_frame)
    english_entry_height.grid(row = 1, column = 1)

    calculate_button = tk.Button(english, text = 'CALCULATE', font = ('Courier New', 20), cursor = 'hand2',
                                 relief = 'flat', overrelief = 'flat', justify = 'center',
                                 command = calculate_english)
    calculate_button.pack(pady = 18)

    back_button = tk.Button(english, text = 'BACK', font = ('Courier New', 8), cursor = 'hand2', relief = 'flat',
                            overrelief = 'flat', justify = 'center', command = destroye)
    back_button.pack()

def bmistatus(bmi):
    global BMI
    BMI = tk.Tk()
    BMI.title('RESULT')
    BMI.geometry('350x150')

    if bmi < 18.5:
        status = "Underweight."
    elif 18.5 <= bmi < 24.9:
        status = "Normal Weight."
    elif 24.9 <= bmi < 29.9:
        status = "Overweight."
    elif bmi >= 30:
        status = "Obese."

    label_result = tk.Label(BMI, text = f"Your bmi is {bmi:.2f} and you are {status}",
                            font = ('Courier New', 15), wraplength = 300)
    label_result.pack(pady = 40)


def choose_convert():
    global converts
    root.withdraw()
    converts = tk.Tk()
    converts.title('CONVERTION')
    converts.geometry('400x120')

    choice_frame = tk.Frame(converts)
    choice_frame.pack()

    chooseconversion = tk.Label(choice_frame, text = 'Choose Conversion:', font = ('Courier New', 15), height = 2)
    chooseconversion.grid(row = 0, column = 0, columnspan = 2, pady = 5)

    button_conversion1 = tk.Button(choice_frame, text = 'Metric to Engilsh', font = ('Courier New', 10), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = choose_units1)
    button_conversion1.grid(row = 1, column = 0, padx = 15)

    button_conversion2 = tk.Button(choice_frame, text = 'English to Metric', font = ('Courier New', 10), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = choose_units2)
    button_conversion2.grid(row = 1, column = 1, padx = 15)

    backbutton = tk.Button(choice_frame, text = 'BACK', font = ('Courier New', 8), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = converthome)
    backbutton.grid(row = 2, column = 0, columnspan = 2)

def choose_units1():
    global choiceunits1
    converts.withdraw()
    choiceunits1 = tk.Tk()
    choiceunits1.title("METRIC TO ENGLISH")
    choiceunits1.geometry('400x120')

    units1_frame = tk.Frame(choiceunits1)
    units1_frame.pack(pady = 20)

    w_units = tk.Button(units1_frame, text = 'WEIGHT', font = ('Courier New', 20), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = kg_to_lbs)
    w_units.grid(row = 0, column = 0, padx = 15)

    h_units = tk.Button(units1_frame, text = 'HEIGHT', font = ('Courier New', 20), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = cm_to_ft)
    h_units.grid(row = 0, column = 1, padx = 15)

def choose_units2():
    global choiceunits2
    converts.withdraw()
    choiceunits2 = tk.Tk()
    choiceunits2.title('ENGLISH TO METRIC')
    choiceunits2.geometry('400x120')

    units2_frame = tk.Frame(choiceunits2)
    units2_frame.pack(pady = 20)

    w_units = tk.Button(units2_frame, text = 'WEIGHT', font = ('Courier New', 20), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = lbs_to_kg)
    w_units.grid(row = 0, column = 0, padx = 15)

    h_units = tk.Button(units2_frame, text = 'HEIGHT', font = ('Courier New', 20), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = ft_to_cm)
    h_units.grid(row = 0, column = 1, padx = 15)

def kg_to_lbs():
    global kglbs
    choiceunits1.withdraw()
    kglbs = tk.Tk()
    kglbs.title('HEIGHT')
    kglbs.geometry('400x150')

    def answerkglbs():
        a = eval(entrykg.get())
        aa = round(a * 2.20462)
        aaa = tk.Label(answerframe, text = f'{aa}lbs', font = ('Courier New', 15))
        aaa.grid(row = 0, column = 0)
        
    convertframe = tk.Frame(kglbs)
    convertframe.pack()

    labellabel = tk.Label(convertframe, text = 'KILOGRAMS', font = ('Courier New', 15), height = 2)
    labellabel.grid(row = 0, column = 0, padx = 10)

    labelto = tk.Label(convertframe, text = ' to ', font = ('Courier New', 15), height = 2)
    labelto.grid(row = 0, column = 1)

    labelanswer = tk.Label(convertframe, text = ' POUNDS ', font = ('Courier New', 15), height = 2)
    labelanswer.grid(row = 0, column = 2, padx = 10)

    entrykg = tk.Entry(convertframe)
    entrykg.grid(row = 1, column = 0)

    equalsign = tk.Label(convertframe, text = '=', font = ('Courier New', 15))
    equalsign.grid(row = 1, column = 1)

    answerbutton = tk.Button(convertframe, text = 'CONVERT', font = ('Courier New', 15), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = answerkglbs)
    answerbutton.grid(row = 2, column = 0, columnspan = 3)

    backbutton = tk.Button(convertframe, text = '   BACK   ', font = ('Courier New', 8), cursor = 'hand2',
                            relief = 'flat', overrelief = 'flat', command = backconvert1)
    backbutton.grid(row = 3, column = 0, columnspan = 3)

    answerframe = tk.LabelFrame(convertframe)
    answerframe.grid(row = 1, column = 2)

def cm_to_ft():
    global cmft
    choiceunits1.withdraw()
    cmft = tk.Tk()
    cmft.title('HEIGHT')
    cmft.geometry('400x150')

    def answercmft():
        a = eval(entrycm.get())
        aa = round(a / 2.54)
        ft = (aa // 12)
        inc = (aa % 12)
        if inc == 0:
            aaa = tk.Label(answerframe, text = f'{ft}ft', font = ('Courier New', 15))
            aaa.grid(row = 0, column = 0)
        else:
            aaa = tk.Label(answerframe, text = f'{ft}ft {inc}inc', font = ('Courier New', 15))
            aaa.pack(expand = 'yes', fill = 'both')

    convertframe = tk.Frame(cmft)
    convertframe.pack()

    labellabel = tk.Label(convertframe, text = 'CENTIMETERS', font = ('Courier New', 15), height = 2)
    labellabel.grid(row = 0, column = 0, padx = 10)

    labelto = tk.Label(convertframe, text = ' to ', font = ('Courier New', 15), height = 2)
    labelto.grid(row = 0, column = 1)

    labelanswer = tk.Label(convertframe, text = '  FEET   ', font = ('Courier New', 15), height = 2)
    labelanswer.grid(row = 0, column = 2, padx = 10)

    entrycm = tk.Entry(convertframe)
    entrycm.grid(row = 1, column = 0)

    equalsign = tk.Label(convertframe, text = '=', font = ('Courier New', 15))
    equalsign.grid(row = 1, column = 1)

    answerbutton = tk.Button(convertframe, text = 'CONVERT', font = ('Courier New', 15), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = answercmft)
    answerbutton.grid(row = 2, column = 0, columnspan = 3)

    backbutton = tk.Button(convertframe, text = '   BACK   ', font = ('Courier New', 8), cursor = 'hand2',
                               relief = 'flat', overrelief = 'flat', command = backconvert2)
    backbutton.grid(row = 3, column = 0, columnspan = 3)

    answerframe = tk.LabelFrame(convertframe)
    answerframe.grid(row = 1, column = 2)

def lbs_to_kg():
    global lbskg
    choiceunits2.withdraw()
    lbskg = tk.Tk()
    lbskg.title('WEIGHT')
    lbskg.geometry('400x150')

    def answerlbskg():
        a = eval(entrylbs.get())
        aa = round(a * 0.453592)
        aaa = tk.Label(answerframe, text = f'{aa}kg', font = ('Courier New', 15))
        aaa.grid(row = 0, column = 0)

    convertframe = tk.Frame(lbskg)
    convertframe.pack()

    labellabel = tk.Label(convertframe, text = ' POUNDS ', font = ('Courier New', 15), height = 2)
    labellabel.grid(row = 0, column = 0, padx = 10)

    labelto = tk.Label(convertframe, text = ' to ', font = ('Courier New', 15), height = 2)
    labelto.grid(row = 0, column = 1)

    labelanswer = tk.Label(convertframe, text = 'KILOGRAMS', font = ('Courier New', 15), height = 2)
    labelanswer.grid(row = 0, column = 2, padx = 10)

    entrylbs = tk.Entry(convertframe)
    entrylbs.grid(row = 1, column = 0)

    equalsign = tk.Label(convertframe, text = '=', font = ('Courier New', 15))
    equalsign.grid(row = 1, column = 1)

    answerbutton = tk.Button(convertframe, text = 'CONVERT', font = ('Courier New', 15), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = answerlbskg)
    answerbutton.grid(row = 2, column = 0, columnspan = 3)

    backbutton = tk.Button(convertframe, text = '   BACK   ', font = ('Courier New', 8), cursor = 'hand2',
                               relief = 'flat', overrelief = 'flat', command = backconvert3)
    backbutton.grid(row = 3, column = 0, columnspan = 3)

    answerframe = tk.LabelFrame(convertframe)
    answerframe.grid(row = 1, column = 2)

def ft_to_cm():
    global ftcm
    choiceunits2.withdraw()
    ftcm = tk.Tk()
    ftcm.title('HEIGHT')
    ftcm.geometry('400x150')

    def answerftcm():
        a = entryft.get().split()
        if len(a) != 2:
            messagebox.showinfo(title = 'INVALID INPUT', message = 'Use this format: e.g. 5 6')
            ft_to_cm()
        aa1 = eval(a[0])
        aa2 = eval(a[1])
        ft = (aa1 * 12)
        inc = (ft + aa2)
        aa = round(inc * 2.54)
        aaa = tk.Label(answerframe, text = f'{aa}cm', font = ('Courier New', 15))
        aaa.grid(row = 0, column = 0)

    convertframe = tk.Frame(ftcm)
    convertframe.pack()

    labellabel = tk.Label(convertframe, text = '  FEET   ', font = ('Courier New', 15), height = 2)
    labellabel.grid(row = 0, column = 0, padx = 10)

    labelto = tk.Label(convertframe, text = ' to ', font = ('Courier New', 15), height = 2)
    labelto.grid(row = 0, column = 1)

    labelanswer = tk.Label(convertframe, text = 'CENTIMETER', font = ('Courier New', 15), height = 2)
    labelanswer.grid(row = 0, column = 2, padx = 10)

    entryft = tk.Entry(convertframe)
    entryft.grid(row = 1, column = 0)

    equalsign = tk.Label(convertframe, text = '=', font = ('Courier New', 15))
    equalsign.grid(row = 1, column = 1)

    answerbutton = tk.Button(convertframe, text = 'CONVERT', font = ('Courier New', 15), cursor = 'hand2',
                                   relief = 'flat', overrelief = 'flat', command = answerftcm)
    answerbutton.grid(row = 2, column = 0, columnspan = 3)

    backbutton = tk.Button(convertframe, text = '   BACK   ', font = ('Courier New', 8), cursor = 'hand2',
                               relief = 'flat', overrelief = 'flat', command = backconvert4)
    backbutton.grid(row = 3, column = 0, columnspan = 3)

    answerframe = tk.LabelFrame(convertframe)
    answerframe.grid(row = 1, column = 2)

def destroym():
    root.update()
    root.deiconify()
    metric.destroy()
    BMI.destroy()

def destroye():
    root.update()
    root.deiconify()
    english.destroy()
    BMI.destroy()

def backconvert1():
    converts.update()
    converts.deiconify()
    kglbs.destroy()

def backconvert2():
    converts.update()
    converts.deiconify()
    cmft.destroy()

def backconvert3():
    converts.update()
    converts.deiconify()
    lbskg.destroy()

def backconvert4():
    converts.update()
    converts.deiconify()
    ftcm.destroy()

def converthome():
    root.update()
    root.deiconify()
    converts.destroy()

def exitroot():
    root.destroy()

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('350x250')

title_label = tk.Label(root, text = "BMI CALCULATOR", font = ('Courier New', 20), justify = 'center', height = 2)
title_label.pack(padx = 20, pady = 5)

button_frame = tk.Frame(root)
button_frame.pack(fill = 'y',  padx=20)

choice_label = tk.Label(button_frame, text = 'Choose System:', font = ('Courier New', 18), justify = 'center')
choice_label.grid(row = 0, column = 0, columnspan = 2)

button1 = tk.Button(button_frame, text = 'Metric', font = ('Courier New', 18), justify = 'left', cursor = 'hand2',
                    relief = 'flat', overrelief = 'flat', command = Metric)
button1.grid(row = 1, column = 0, padx = 10)

button2 = tk.Button(button_frame, text = 'English', font = ('Courier New', 18), justify = 'center', cursor = 'hand2', 
                    relief = 'flat', overrelief = 'flat', command = English)
button2.grid(row = 1, column = 1, padx = 10)

other_frame = tk.Frame(root)
other_frame.pack(pady = 5)

convert_button = tk.Button(other_frame, text = 'CONVERT UNITS', font = ('Courier New', 10), cursor = 'hand2', relief = 'flat',
                           overrelief = 'flat', justify = 'center', command = choose_convert)
convert_button.pack(side = 'top')

exit_button = tk.Button(other_frame, text = 'EXIT', font = ('Courier New', 8), cursor = 'hand2', relief = 'flat',
                        overrelief = 'flat', justify = 'center', command = exitroot)
exit_button.pack(side = 'top')

root.mainloop()
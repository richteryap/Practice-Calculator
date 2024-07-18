import tkinter as tk
from tkinter import Label, LabelFrame, Entry, ttk, Button
from datetime import datetime, timedelta


def calculate_water_bill():
    # Function to calculate the water bill based on user inputs

    min_charges = {
        'Residential': {'1/2"': 218.40, '3/4"': 349.40, '1"': 497.00, '1 1/2"': 1747.20,
                        '2"': 4368.00, '3"': 7862.40, '4"': 15724.80, '10"': 60278.40},
        'Government': {'1/2"': 218.40, '3/4"': 349.40, '1"': 497.00, '1 1/2"': 1747.20,
                       '2"': 4368.00, '3"': 7862.40, '4"': 15724.80, '10"': 60278.40},
        'Commercial': {'1/2"': 436.80, '3/4"': 698.80, '1"': 1397.70, '1 1/2"': 3494.40,
                       '2"': 8736.00, '3"': 15724.80, '4"': 31449.60, '10"': 120556.80},
        'Industrial': {'1/2"': 436.80, '3/4"': 698.80, '1"': 1397.70, '1 1/2"': 3494.40,
                       '2"': 8736.00, '3"': 15724.80, '4"': 31449.60, '10"': 120556.80}
    }

    # Get user inputs
    present_reading = float(presentEntry.get())
    previous_reading = float(previousEntry.get())
    meter_consumption = present_reading - previous_reading
    name = nameEntry.get()
    address = addressEntry.get()
    account_number = account_number_entry.get()
    meter_number = meter_number_entry.get()

    # Get customer type input
    customer_type = classificationEntry.get().title().strip()

    # Get meter size input
    meter_size = metersizeEntry.get()

    # Calculate minimum charges
    min_charge = min_charges[customer_type][meter_size]

    # Initialize commodity charge to 0
    commodity_charge = 0

    # Check if commodity charges apply
    if meter_consumption > 10:
        if 11 <= meter_consumption <= 20:
            commodity_charge = (meter_consumption - 10) * 30.55
        elif 21 <= meter_consumption <= 30:
            commodity_charge = 10 * 30.55 + (meter_consumption - 20) * 31.85
        elif 31 <= meter_consumption <= 40:
            commodity_charge = 10 * 30.55 + 10 * 31.85 + (meter_consumption - 30) * 33.65
        else:
            commodity_charge = 10 * 30.55 + 10 * 31.85 + 10 * 33.65 + (meter_consumption - 40) * 36.00

    # Get the current date
    current_date = datetime.now()

    # Assume the billing cycle (20 days sa CDO Water District)
    billing_cycle_days = 20

    # Calculate the bill date
    bill_date = current_date.strftime("%m-%d-%Y")

    # Calculate the due date by adding the billing cycle to the current date
    due_date = (current_date + timedelta(days=billing_cycle_days)).strftime("%m-%d-%Y")

    # Identify what period is the statement of account
    period_date = current_date.strftime("%B %Y")

    # Calculate total water bill
    total_bill = min_charge + commodity_charge

    # Add 12% VAT
    vat_rate = 0.12
    vat_amount = total_bill * vat_rate

    # Calculate total amount including VAT
    total_amount_with_vat = total_bill + vat_amount

    # Add 10% if amount is not paid after Due Date
    penalty_rate = 0.10
    penalty_amount = total_amount_with_vat * penalty_rate

    # Calculate the amount after Due Date
    total_penalty_amount = total_amount_with_vat + penalty_amount

    # Define the size for the result window
    result_window_width = 719
    result_window_height = 405

    # Display the result in a new window
    result_window = tk.Toplevel(root)
    result_window.title('Water Bill Receipt')

    # Calculate the center position for the result window
    result_window_center_x = int(screen_width / 2 - result_window_width / 2)
    result_window_center_y = int(screen_height / 2 - result_window_height / 2)

    result_window.geometry(
        f'{result_window_width}x{result_window_height}+{result_window_center_x}+{result_window_center_y}')

    title_label1 = Label(result_window, text=f"{'=' * 65}",
                         font=('Courier New', 14, 'bold'), justify='center')
    title_label1.grid(row=0, column=0)

    # Create a separate label for "CS1B WATER DISTRICT"
    title_label = Label(result_window, text=f"CS1B WATER DISTRICT", font=('Courier New', 14, 'bold'))
    title_label.grid(row=1, column=0)

    title_label1 = Label(result_window, text=f"Bldg. 9 USTP CDO Campus, Lapasan, Cagayan de Oro City"
                                             f"\n{'-' * 89}", font=('Courier New', 10, 'bold'))
    title_label1.grid(row=2, column=0)

    # Create the receipt label
    receipt_label1 = Label(result_window, text=f"Statement of Account"
                                               f"\nFor the month of {period_date}", font=('Courier New', 10),
                           justify='center')
    receipt_label1.grid(row=3, column=0)

    test_frame = LabelFrame(result_window)
    test_frame.grid(row=4, column=0, padx=4, pady=5, sticky='ew')

    r2 = Label(test_frame, text=f"Name: {name}"
                                f"\nAddress: {address}"
                                f"\nCustomer Type: {customer_type}"
                                f"\nMeter Size: {meter_size}"
                                f"\nBill Date: {bill_date}", font=('Courier New', 10), justify='left', relief='flat')
    r2.grid(row=0, column=0, padx=20, pady=5, sticky='w')  # Align to the left

    r3 = Label(test_frame, text=f"Account Number: {account_number}"
                                f"\nMeter Number: {meter_number}"
                                f"\nPresent Reading: {present_reading}"
                                f"\nPrevious Reading: {previous_reading}"
                                f"\nDue Date: {due_date}", font=('Courier New', 10), justify='right')
    r3.grid(row=0, column=1, padx=20, pady=5, sticky='e')  # Align to the right

    # Configure column weights
    test_frame.grid_columnconfigure(0, weight=1)
    test_frame.grid_columnconfigure(1, weight=1)

    receipt_label = Label(result_window, text=f"Meter Consumption: {meter_consumption} m³"
                                              f"\nMinimum Charge: ₱{min_charge:,.2f}"
                                              f"\nCommodity Charge: ₱{commodity_charge:,.2f}"
                                              f"\nTotal: ₱{total_bill:,.2f}"
                                              f"\nAdd VAT (12%): ₱{vat_amount:,.2f}"
                                              f"\n{'-' * 89}",
                          font=('Courier New', 10), justify='center')
    receipt_label.grid(row=5, column=0)

    footer_label = Label(result_window, text=f"Total Water Bill: ₱{total_amount_with_vat:,.2f}"
                                             f"\nAmount after Due Date: ₱{total_penalty_amount:,.2f}",
                         font=('Courier New', 10, 'bold'), justify='center')
    footer_label.grid(row=6, column=0)

    footer_label1 = Label(result_window, text=f"{'=' * 65}",
                          font=('Courier New', 14, 'bold'), justify='center')
    footer_label1.grid(row=7, column=0)


# GUI code
root = tk.Tk()
root.title('Water Bill')
root.iconbitmap('water_drops_icon_161227.ico')

# Main title
headingLabel = Label(root, text='CS1B WATER DISTRICT', font=('serif', 20, 'bold'),
                     bg="DodgerBlue2", fg='snow', bd=9, relief='groove')
headingLabel.grid(row=0, column=0, columnspan=2, padx=4, pady=5, sticky='ew')

# Description label with a smaller font size
descriptionLabel = Label(root, text='Bldg. 9 USTP CDO Campus, Lapasan, Cagayan de Oro City',
                         font=('serif', 10, 'bold'), bg="DodgerBlue2", fg='snow', bd=9, relief='groove')
descriptionLabel.grid(row=1, column=0, columnspan=2, padx=5, sticky='ew')

# User Information
user_info_frame = LabelFrame(root, text='USER INFORMATION', font=('serif', 11, 'bold'),
                             bg="DodgerBlue2", fg='snow', bd=9)
user_info_frame.grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky='ew')

nameLabel = Label(user_info_frame, text='    Name:    ', font=('serif', 11, 'bold'),
                  bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
nameLabel.grid(row=0, column=0, padx=5, pady=5)

nameEntry = Entry(user_info_frame, font=('arial', 8), width=35)
nameEntry.grid(row=0, column=1, padx=10, pady=5)

account_number_label = Label(user_info_frame, text='  Account Number:  ', font=('serif', 11, 'bold'),
                             bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
account_number_label.grid(row=0, column=2, padx=5, pady=5)

account_number_entry = Entry(user_info_frame, font=('arial', 8), width=25)
account_number_entry.grid(row=0, column=3, padx=10)

addressLabel = Label(user_info_frame, text='  Address:  ', font=('serif', 11, 'bold'),
                     bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
addressLabel.grid(row=1, column=0, padx=5, pady=5)

addressEntry = Entry(user_info_frame, font=('arial', 8), width=35)
addressEntry.grid(row=1, column=1, padx=16)

meter_number_label = Label(user_info_frame, text='    Meter Number:    ', font=('serif', 11, 'bold'),
                           bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
meter_number_label.grid(row=1, column=2, padx=5)

meter_number_entry = Entry(user_info_frame, font=('arial', 8), width=25)
meter_number_entry.grid(row=1, column=3, padx=10)

# Customer Details

customer_details_frame = LabelFrame(root, text='CUSTOMER DETAILS', font=('serif', 11, 'bold'),
                                    bg="DodgerBlue2", fg='snow', bd=9)
customer_details_frame.grid(row=3, column=0, padx=4)

classificationLabel = Label(customer_details_frame, text='   Classification:   ', font=('serif', 11, 'bold'),
                            bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
classificationLabel.grid(row=0, column=0, padx=4, pady=5)

classification_choices = ['Residential', 'Commercial', 'Government', 'Industrial']
classificationEntry = ttk.Combobox(customer_details_frame, values=classification_choices, font=('arial', 8),
                                   state='readonly')
classificationEntry.grid(row=0, column=1, padx=9, pady=9)

metersizeLabel = Label(customer_details_frame, text='     Meter Size:      ', font=('serif', 11, 'bold'),
                       bg="DodgerBlue2",
                       fg='snow', bd=4, relief='groove')
metersizeLabel.grid(row=1, column=0, padx=7, pady=10)

metersize_choices = ['1/2"', '3/4"', '1"', '1 1/2"', '2"', '3"', '4"', '10"']
metersizeEntry = ttk.Combobox(customer_details_frame, values=metersize_choices, font=('arial', 8), state='readonly')
metersizeEntry.grid(row=1, column=1, padx=5, pady=10)

# Meter Consumption

meter_consumption_frame = LabelFrame(root, text='METER CONSUMPTION', font=('serif', 11, 'bold'),
                                     bg="DodgerBlue2", fg='snow', bd=9)
meter_consumption_frame.grid(row=3, column=1, padx=3)

presentLabel = Label(meter_consumption_frame, text='   Enter Present Reading:   ', font=('serif', 11, 'bold'),
                     bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
presentLabel.grid(row=0, column=0, padx=5, pady=5)

presentEntry = Entry(meter_consumption_frame, font=('arial', 8), width=18)
presentEntry.grid(row=0, column=1, padx=10, pady=5)

previousLabel = Label(meter_consumption_frame, text='  Enter Previous Reading:  ', font=('serif', 11, 'bold'),
                      bg="DodgerBlue2", fg='snow', bd=4, relief='groove')
previousLabel.grid(row=1, column=0, padx=5, pady=10)

previousEntry = Entry(meter_consumption_frame, font=('arial', 8), width=18)
previousEntry.grid(row=1, column=1, padx=10, pady=5)

# Calculate button

button_frame = LabelFrame(root)
button_frame.grid(row=4, column=0, columnspan=2, padx=3, pady=5, sticky='ew')

calculate_button = Button(button_frame, text='CALCULATE', font=('serif', 12, 'bold'),
                          bg="DodgerBlue2", fg='snow', bd=10, relief='groove')
calculate_button.pack(fill='x')

# Result

result_label = Label(root, text='', font=('Courier New', 11))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=9)

window_width = 704
window_height = 391

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

calculate_button.config(command=calculate_water_bill)

root.mainloop()

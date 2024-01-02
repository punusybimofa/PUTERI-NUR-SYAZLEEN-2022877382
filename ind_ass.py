import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar


# Constants
NUM_TABLES = 10
table_status = [False] * NUM_TABLES  # False represents an available table
user_info = []

def reserve_table():
    # Collect user information
        name = name_entry.get()
        phone_number = phone_entry.get()
        num_adults = int(adults_entry.get())
        num_kids = int(kids_entry.get())
        num_elders = int(elders_entry.get())
        time_reserve = time_var.get()
        date_reserve = cal.get_date()

    # Calculate total cost
        total_cost = (num_adults * 60.00) + (num_kids * 30.00) + (num_elders * 40.00)

        # Display reservation information
        reservation_info = (
            f"Name: {name}\n"
            f"Phone Number: {phone_number}\n"
            f"Adults: {num_adults}\n"
            f"Kids: {num_kids}\n"
            f"Elders/OKU: {num_elders}\n"
            f"Total Cost: RM {total_cost:.2f}"
        )

        messagebox.showinfo("Success", reservation_info)

        # Update table status and user information
        user_info.append({
            'name': name,
            'phone_number': phone_number,
            'num_adults': num_adults,
            'num_kids': num_kids,
            'num_elders': num_elders,
            'total_cost': total_cost,
            'time_reserve': time_reserve,
            'date_reserve': date_reserve
        })

        #To print specific value in a dictionary ( list )
        #print(user_info[0]['name'])
        #print(user_info[0])

        #----------------------TESTING---------------
        
        # Connect to your MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="reserva_buffet"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        # Inserting data into a table
        #sql = "INSERT INTO `customer_details` (NAME, PHONE_NUM, NUM_ADULT, NUM_KIDS, NUM_ELDER, TIME, DATE, TOTAL_COST) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #val = (name_entry.get(), phone_entry.get(), adults_entry.get(), kids_entry.get(), elders_entry.get(), time_var.set(), cal(), total_cost())
        sql = "INSERT INTO `customer_details` (NAME, PHONE_NUM, NUM_ADULT, NUM_KIDS, NUM_ELDER, TIME, DATE, TOTAL_COST) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user_info[0]['name'], user_info[0]['phone_number'], user_info[0]['num_adults'], user_info[0]['num_kids'], user_info[0]['num_elders'], user_info[0]['time_reserve'], user_info[0]['date_reserve'], user_info[0]['total_cost'])
        try:
            cursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

        clear_user_info()

# ''' -> Comment for Multiple Line
'''     
def update_table_listbox():
    table_listbox.delete(0, tk.END)
    for i, status in enumerate(table_status):
        if status:
            table_listbox.insert(tk.END, f"Table {i + 1} (Reserved)")
        else:
            table_listbox.insert(tk.END, f"Table {i + 1} (Available)")
'''

def clear_user_info():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    adults_entry.delete(0, tk.END)
    kids_entry.delete(0, tk.END)
    elders_entry.delete(0, tk.END)
    time_var.set("Select Your Time")  # Default value before your selection
    date.config(text = "No Date Selected")
    user_info.clear()

# GUI setup
root = tk.Tk()
root.title("DUCKY BUFFET")
root.geometry ('600x680')

label= tk.Label(root,text= "DUCKY BUFFET",font=("Cambria", 20, "italic"), bg= "light goldenrod", 
                fg="dark goldenrod3", bd=8, relief="groove")
label.pack(ipadx=800)


# User Information Entry Widgets
name_label = tk.Label(root, text="Name:", fg="salmon4",bd=5, relief="ridge", bg="light goldenrod", padx=245)
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack ( ipadx=200)  


phone_label = tk.Label(root, text="Phone Number:", fg="salmon4",bd=5, relief="ridge", bg="light goldenrod", padx=220 )
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack(ipadx=200)

adults_label = tk.Label(root, text="Number of Adults:", fg="salmon4", bd=5, relief="ridge", bg="light goldenrod", padx=215)
adults_label.pack()
adults_entry = tk.Entry(root)
adults_entry.pack(ipadx=200)

kids_label = tk.Label(root, text="Number of Kids:", fg="salmon4", bd=5, relief="ridge", bg="light goldenrod", padx=220 )
kids_label.pack()
kids_entry = tk.Entry(root)
kids_entry.pack(ipadx=200)

elders_label = tk.Label(root, text="Number of Elders/OKU:", fg="salmon4",  bd=5, relief="ridge", bg="light goldenrod", padx=200)
elders_label.pack()
elders_entry = tk.Entry(root)
elders_entry.pack(ipadx=200)

time_label = tk.Label(root, text="Time:", fg="salmon4",  bd=5, relief="ridge", bg="light goldenrod", padx=50)
time_label.pack()

# Trip Type Dropdown

# Create the list of options 
time_list = ["4PM", "5PM", "6PM", "7PM", "8PM", "9PM"] 

time_var = tk.StringVar(root)
time_var.set("Select Your Time")  # Default value before your selection
time_dropdown = tk.OptionMenu(root, time_var, *time_list)

time_dropdown.pack(pady=10, ipadx=50)
 
date_label = tk.Label(root, text="Date:",fg="salmon4", bd=5, relief="ridge", bg="light goldenrod", padx=50)
date_label.pack()
 

# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = 2023, month = 1,
               day = 22)
 
cal.pack(pady = 5)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
tk.Button(root, text = "Get Date",
       command = grad_date).pack(pady = 3)
 
date = tk.Label(root, text = "")
date.pack(pady =1)

# Table Listbox
# table_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=NUM_TABLES)
# table_listbox.pack(pady=10, ipadx=10)

# Reserve Button
reserve_button = tk.Button(root, text="Reserve Table", command=reserve_table)
reserve_button.pack(pady=5, ipadx=5)

# Update Table Listbox
# update_table_listbox()

# Run the main loop
root.mainloop()

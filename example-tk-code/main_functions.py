# main_functions.py
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from aaswconnect import *
#from connect import *
from functions import *
import tkinter.messagebox as mb


# Function to populate the table with data from the database
def populate_table():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()

        # Replace 'your_table_name' with the actual table name
        query = "SELECT * FROM `teamb`"
        cursor.execute(query)
        data = cursor.fetchall()

        # Clear existing rows in the table (if any)
        for row in table.get_children():
            table.delete(row)

        # Insert fetched data into the table
        for row in data:
            table.insert("", "end", values=row)

        cursor.close()
        conn.close()

def delete_data_wrapper():
    selected_item = table.selection()[0]
    delete_data(table, selected_item)


def search_database_wrapper():
    criterion = selected_criterion.get()
    value = search_value.get()
    search_database_by_criterion(table, criterion, value)

def edit_data_wrapper():
    criterion = selected_criterion.get()
    selected_item = table.selection()[0]
    edit_data(table,selected_item,app)

def add_data_wrapper():
    add_record()


def update_button_states():
    selected_items = table.selection()

    if len(selected_items) == 1:
        edit_button.config(state=tk.NORMAL)
        delete_button.config(state=tk.NORMAL)
    elif len(selected_items) > 1:
        edit_button.config(state=tk.DISABLED)
        delete_button.config(state=tk.NORMAL)
    else:  # No items are selected
        edit_button.config(state=tk.DISABLED)
        delete_button.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.resizable(False, False)
app.title("Database Table Viewer")
app.geometry("1280x806")  # Width x Height

image = Image.open("images/background.jpg")
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the background to fit the app

# Frame for top controls (search bar, drop-down, and button)
top_frame = ttk.Frame(app)
top_frame.pack(pady=10, padx=10, fill=tk.X)  # Add some padding around the frame

# Drop-down menu for search criterion
search_criteria = ["CRN", "Subject", "Time", "Days"]
selected_criterion = tk.StringVar()
criterion_dropdown = ttk.Combobox(top_frame, textvariable=selected_criterion, values=search_criteria)
criterion_dropdown.grid(row=0, column=0, padx=5, pady=5)

# Entry for the search value
search_value = tk.StringVar()
search_entry = ttk.Entry(top_frame, textvariable=search_value)
search_entry.grid(row=0, column=1, padx=5, pady=5)

# Search button
search_button = ttk.Button(top_frame, text="Search", command=search_database_wrapper)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Create a frame to contain the table and scrollbars
frame = ttk.Frame(app)
frame.place(relx=0.5, rely=0.5, width=800, height=350, anchor="center")

# Scrollbars
scrollbarx = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
scrollbary = tk.Scrollbar(frame, orient=tk.VERTICAL)

# Create a Treeview widget (table)
table = ttk.Treeview(frame, columns=tuple("ColumnName" + str(i) for i in range(1, 20)), show="headings")

# Configure the table's scroll commands
table.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

# Bind the scrollbars to the table view
scrollbarx.config(command=table.xview)
scrollbary.config(command=table.yview)

# Using pack to manage geometry of widgets inside the frame
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Main application window already created as 'app'

# Creating the operations frame
operations_frame = ttk.Frame(app)
operations_frame.pack(pady=10, padx=10)  # Adjust as needed

# Add Record Button
add_button = ttk.Button(operations_frame, text="Add", command=add_data_wrapper)
add_button.grid(row=0, column=0, padx=5, pady=5)

# Delete Record Button
delete_button = ttk.Button(operations_frame, text="Delete", command=delete_data_wrapper)
delete_button.grid(row=0, column=1, padx=5, pady=5)

# Edit Record Button
edit_button = ttk.Button(operations_frame, text="Edit", command=edit_data_wrapper)
edit_button.grid(row=0, column=2, padx=5, pady=5)

# Bind the function to the Treeview's selection change event
table.bind("<<TreeviewSelect>>", lambda e: update_button_states())

# Initialize the button states
update_button_states()

# Define column headings 
column_names = ["Code", "TAMUK", "Subject", "Course", "CRN", "", "Building", "Room", "Days", "Time",
                "Duration", "Semester", "Year", "Room Type", "Enrollments", "Exceed Funds", "SCH Exceed Funds", "LLE Affected", "ULE Affected"]

for i, column_name in enumerate(column_names):
    table.heading("ColumnName" + str(i + 1), text=column_name)

# Define column widths
for i in range(1, 20):
    table.column("ColumnName" + str(i), width=100)

# Insert the table into the frame
table.pack(fill="both", expand=True)

# Create a "Refresh" button to populate the table
refresh_button = ttk.Button(app, text="Refresh", command=populate_table)
refresh_button.pack(pady=20)

# Initial population of the table
populate_table()

app.mainloop()

# main_functions.py
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from aaswconnect import *
import tkinter.messagebox as mb


def search_database_by_criterion(table, criterion, value):
    data = fetch_data_by_criterion(criterion, value)  # this function needs to be defined in your handler
    
    for row in table.get_children():
        table.delete(row)

    # Insert fetched data into the table (if data is not None)
    if data:
        for record in data:
            table.insert("", "end", values=record)



# Edit function
def edit_data(table, selected_item, app):
    # Extract the data from the selected item
    uid = table.item(selected_item)['values']

    # Create a connection to the database
    conn = connect_to_database()

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define the SQL query to select data based on the 'CRN' column
    select_query = "SELECT * FROM teamb WHERE CRN = %s"

    try:
        # Execute the select query with the provided 'CRN' value
        cursor.execute(select_query, (uid[4],))
        result = cursor.fetchone()  # Get the record

        if result:
            # Create an editing window
            edit_window = tk.Toplevel()
            edit_window.title("Edit Data")

            # Create entry fields to edit data
            entry_labels = ["Code", "TAMUK", "Subject", "Course", "CRN",'', "Building", "Room", "Days", "Time",
                "Duration", "Semester", "Year", "Room Type", "Enrollments", "Exceed Funds", "SCH Exceed Funds", "LLE Affected", "ULE Affected"]
            entry_values = [tk.StringVar(value=result[0]), tk.StringVar(value=result[1]),
                tk.StringVar(value=result[2]), tk.StringVar(value=result[3]), tk.StringVar(value=result[4]),tk.StringVar(value=result[5]), tk.StringVar(value=result[6]),
                tk.StringVar(value=result[7]), tk.StringVar(value=result[8]), tk.StringVar(value=result[9]), tk.StringVar(value=result[10]),
                tk.StringVar(value=result[11]), tk.StringVar(value=result[12]),
                tk.StringVar(value=result[13]), tk.StringVar(value=result[14]), tk.StringVar(value=result[15]), tk.StringVar(value=result[16]),
                tk.StringVar(value=result[17]), tk.StringVar(value=result[18])]
            # Determine the number of rows and columns for the grid layout
            num_rows = len(entry_labels)
            num_columns = 4  # Four columns able to change the forms number of columns

            # Calculate the maximum width of labels in each row
            max_label_widths = [0] * num_rows
            for i, label_text in enumerate(entry_labels):
                label = tk.Label(edit_window, text=label_text)
                label.update_idletasks()  # Update to get the actual width
                label_width = label.winfo_width()
                max_label_widths[i % num_rows] = max(max_label_widths[i % num_rows], label_width)

            for i, label_text in enumerate(entry_labels):
                # FORMATTING :Calculate the padding to align the labels
                pad_width = max_label_widths[i % num_rows] - len(label_text)
                col_index = (i % num_columns) * 2  # Calculate the column index based on the modulo

                # FORMATTING: Calculate the row index based on the column index to make form even
                row_index = i // num_columns
                label = tk.Label(edit_window, text=label_text, padx=pad_width * 7)  # Adjust the multiplier as needed
                label.grid(row=row_index, column=col_index, sticky=tk.E)  # Use modulo to alternate between columns

                # Disable the entry field for CRN so that primary key cannot be adjusted
                if label_text == 'CRN':
                    entry = tk.Entry(edit_window, textvariable=entry_values[i], state='readonly', width=20)  # Set width for larger entry fields
                else:
                    entry = tk.Entry(edit_window, textvariable=entry_values[i], width=20)  # Set width for larger entry fields
                entry.grid(row=row_index, column=col_index + 1, padx=1, pady=1, sticky=tk.W)  # Use modulo to alternate between columns and add padding

            # FORMATTING: Set a uniform row weight for all rows
            for i in range(num_rows // num_columns + 1):
                edit_window.grid_rowconfigure(i, weight=1)

            # FORMATTING: Set a uniform column weight for all columns
            for i in range(num_columns * 2):
                edit_window.grid_columnconfigure(i, weight=1)

            # Function to update the record in the database
            def update_record():
                # Corrected the field names in the update query
                update_query = "UPDATE teamb SET Code = %s, TAMUK = %s, Subject = %s, Course = %s, CRN = %s,unused=%s, Building = %s,Room = %s, Days = %s, Time = %s, Duration = %s, Semester = %s, Year = %s, Room_Type = %s, Enrollments = %s, Exceed_Funds = %s, SCH_Exceed_Funds = %s, LLE_Affected = %s, ULE_Affected = %s WHERE CRN = %s"

                #collect entry_values and assign them to values for sql statement  
                values = [str(entry.get()) for i, entry in enumerate(entry_values[:19])]
                values.append(uid[4])

                # Convert all values to strings explicitly
                values = tuple(str(value) for value in values)
                cursor.execute(update_query, values)
                conn.commit()
                edit_window.destroy()
                mb.showinfo("Updated", "Data updated successfully")
               


            # Create a button to update the record
            update_button = tk.Button(edit_window, text="Update", command=update_record)
            update_button.grid(row=num_rows // num_columns + 1, columnspan=num_columns * 2, pady=20)  # Added pady for spacing
            edit_window.mainloop()
        else:
            mb.showerror("Error", "Record not found")
    except mysql.connector.Error as e:
        # Handle any potential errors during the execution
        mb.showerror("Error", str(e))
    finally:
        # Close the database connection
        conn.close()



#delete function
def delete_data(table,selected_item):

    # Extract the data from the selected item
    uid = table.item(selected_item)['values']
    # Create a confirmation pop-up
    confirmed = mb.askyesno("Confirmation", "Are you sure you want to delete this data?")
    
    if not confirmed:
        return  # User canceled the deletion
    
    # Create a connection to the database
    conn = connect_to_database()

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define the SQL query 
    del_query = "DELETE FROM teamb WHERE CRN = %s"

    try:
        # Execute the delete query with the provided 'crn' value
        cursor.execute(del_query, (uid[4],))

        # Commit the changes to the database
        conn.autocommit = True

        # Delete the selected item from the table
        table.delete(selected_item)
        mb.showinfo("Deleted stuff", "Data deleted successfully")
    except mysql.connector.Error as e:
        # Handle any potential errors during the execution
        mb.showerror("Error", str(e))
    finally:
        # Close the database connection
        conn.close()
                
    return None

def add_record():
    
    add_window = tk.Toplevel()
    add_window.title("Add Record")

    add_window.geometry('400x700')

    entry_labels = ['Subject', 'Course', 'CRN', 'Building', 'Room', 'Days', 'Time', 'Duration', 'Semester', 'Year', 'Room Type', 'Enrollments', 'Exceed Funds', 'SCH Exceed Funds', 'LLE Affected', 'ULE Affected' ]
    entry_values = []
    
    
    # Create an entry for each label
    for label in entry_labels:
        # Create a Label
        label_widget = tk.Label(add_window, text=label)
        label_widget.pack()

        # Create an Entry
        entry_widget = tk.Entry(add_window)
        entry_widget.pack()
        # Set default values
        if label == 'Enrollments':
            entry_widget.insert(0, '000000000000000')
        elif label in ['Exceed Funds','Days', 'Room Type','Room','Duration' 'SCH Exceed Funds', 'LLE Affected', 'ULE Affected']:
            entry_widget.insert(0, '000')
        elif label in ['Course','Building', 'Time']:
            entry_widget.insert(0, '0000')
            

        # Store the Entry widget in the list
        entry_values.append(entry_widget)

    # Function to handle the submit action
    # ...

    def submit_action():

        try:
            # Establish a connection to the database
            conn = connect_to_database()
            cursor = conn.cursor()

            # Modify this query to match your database schema
            query = "INSERT INTO teamb (Code, TAMUK, Subject, Course, CRN, unused, Building, Room, Days, Time, Duration, Semester, Year, Room_Type, Enrollments, Exceed_Funds, SCH_Exceed_Funds, LLE_Affected, ULE_Affected) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            print([type(item) for item in entry_values])  # Debugging line
            data = [entry.get() for entry in entry_values]
            data.insert(0, '5')
            data.insert(1, '003639')
            data.insert(5, ' ')  # Inserting None (or '') at the position of the "unused" column

            cursor.execute(query, tuple(data))  # Converting list to tuple for the query

            # Commit the changes
            conn.commit()

            print("Record inserted successfully.")
            # Maybe show a message box to the user here

        except mysql.connector.Error as error:
            if isinstance(error, mysql.connector.IntegrityError) and "Duplicate entry" in str(error):
            # CRN is already in use
                mb.showerror("Error", "CRN is already in use.")
            else:
                print("Failed to insert record into database: {}".format(error))
            

        finally:
            # Close the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")


    # Submit Button
    submit_button = tk.Button(add_window, text="Submit", command=submit_action)
    submit_button.pack()


"""
GUI Calendar Application

This Python script creates a graphical user interface (GUI) calendar application using tkinter and tkcalendar modules.
The application allows users to select a date from the calendar and displays the selected date in the window.
The calendar is set to day/month/year format ('d/m/yy') and includes a button to trigger date selection.

Libraries Used:
- tkinter: Used for creating the GUI and its components.
- tkcalendar: Provides the calendar widget for date selection.

Functionalities:
1. Displays a calendar widget for date selection.
2. Retrieves and displays the selected date when a button is clicked.

Usage:
open your ternminal install these libraries
------ pip install tk
-------pip install tkcalendar

1. Run the script.
2. Click the "Select Date" button to choose a date from the calendar.
3. The selected date will be displayed below the calendar.



"""

# Import necessary libraries
from tkinter import *
from tkcalendar import *

# Create the main Tkinter window
root = Tk()

# Function to display the selected date
def choice_date():
    present_date = display_cal.get_date()  # Get the selected date from the calendar
    user_date = Label(text=present_date)   # Create a label to display the date
    user_date.pack(padx=2, pady=2)         # Pack the label into the window

# Create a calendar widget with date settings
display_cal = Calendar(root, setmode="day", date_pattern='d/m/yy')
display_cal.pack(padx=15, pady=15)  # Pack the calendar widget into the window

# Create a button to select the date
open_cal = Button(root, text="Select Date", command=choice_date)
open_cal.pack(padx=15, pady=15)  # Pack the button into the window

# Set window properties
root.geometry('400x400')      # Set initial window size
root.title("GUI CALENDAR")    # Set window title
root.configure(bg="blue")     # Set window background color

# Start the Tkinter event loop
root.mainloop()

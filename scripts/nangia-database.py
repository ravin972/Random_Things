import tkinter as tk
from tkinter import filedialog
import sqlite3
import os

# Create a database or connect to an existing one
conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

# Create a table to store user data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS uploaded_files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        file_path TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')
conn.commit()

# Function to insert user data and uploaded files into the database
def insert_data():
    name = name_entry.get()
    email = email_entry.get()
    
    # Retrieve the list of selected files and folders
    selected_files = uploaded_file_listbox.get(0, tk.END)
    
    # Insert user data into the database
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    user_id = cursor.lastrowid
    
    # Insert uploaded files into the database
    for file_path in selected_files:
        cursor.execute("INSERT INTO uploaded_files (user_id, file_path) VALUES (?, ?)", (user_id, file_path))
    
    conn.commit()
    
    # Clear input fields and file listbox
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    uploaded_file_listbox.delete(0, tk.END)
    
    # Show the search form after inserting data
    show_search_form()

# Function to retrieve user data and uploaded files based on the name
def retrieve_data():
    name = search_entry.get()
    cursor.execute("SELECT id FROM users WHERE name=?", (name,))
    result = cursor.fetchone()
    
    if result:
        user_id = result[0]
        cursor.execute("SELECT name, email FROM users WHERE id=?", (user_id,))
        user_data = cursor.fetchone()
        
        cursor.execute("SELECT file_path FROM uploaded_files WHERE user_id=?", (user_id,))
        uploaded_files = cursor.fetchall()
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Name: {user_data[0]}\nEmail: {user_data[1]}\nUploaded Files:\n")
        
        for file_path in uploaded_files:
            result_text.insert(tk.END, f"- {file_path[0]}\n")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "No matching records found.")

# Function to show the search form
def show_search_form():
    insert_button.pack_forget()
    search_button.pack_forget()
    
    name_label.pack()
    name_entry.pack()
    email_label.pack()
    email_entry.pack()
    upload_button.pack()
    uploaded_file_label.pack()
    
    search_label.pack()
    search_entry.pack()
    search_button.pack()

# Function to open a file dialog for uploading files or folders
def upload_files():
    file_paths = filedialog.askopenfilenames()
    
    for file_path in file_paths:
        uploaded_file_listbox.insert(tk.END, file_path)

# Create the main application window
app = tk.Tk()
app.title("User Data Storage and Retrieval")

# Create input fields and labels for data insertion
name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

# Create a listbox for uploaded files
uploaded_file_listbox = tk.Listbox(app, selectmode=tk.MULTIPLE, height=5)
uploaded_file_listbox.pack()

# Create button to insert data and upload files
insert_button = tk.Button(app, text="Insert Data", command=insert_data)
insert_button.pack()

# Create button to upload files
upload_button = tk.Button(app, text="Upload Files", command=upload_files)
upload_button.pack()

# Label to display the selected file paths
uploaded_file_label = tk.Label(app, text="No files selected")
uploaded_file_label.pack()

# Create input field and label for data retrieval
search_label = tk.Label(app, text="Search by Name:")
search_label.pack()
search_entry = tk.Entry(app)
search_entry.pack()

# Create a text widget to display search results
result_text = tk.Text(app, height=10, width=40)
result_text.pack()

app.mainloop()

# Close the database connection when the application is closed
conn.close()

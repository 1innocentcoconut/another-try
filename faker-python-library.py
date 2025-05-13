import tkinter as tk
from tkinter import ttk
from faker import Faker

def generate_fake_data():
    faker = Faker()
    fake_name = faker.name()
    fake_address = faker.address()
    fake_phone_number = faker.phone_number()

    output_text.set(f"Name: {fake_name}\nAddress: {fake_address}\nPhone Number: {fake_phone_number}")

# Create the main window
root = tk.Tk()
root.title("Fake Data Generator")

# Create a label to display the generated fake data
output_text = tk.StringVar()
output_label = ttk.Label(root, textvariable=output_text, wraplength=300)
output_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Create a button to generate fake data
generate_button = ttk.Button(root, text="Generate Fake Data", command=generate_fake_data)
generate_button.grid(row=1, column=0, padx=10, pady=10)

# Run the application
root.mainloop()

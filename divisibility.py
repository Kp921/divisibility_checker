import tkinter as tk
from tkinter import messagebox

# Function to find divisors and display them
def find_divisors():
    try:
        x = int(entry_number.get())
        result_text = f"The number {x} is divisible by:\n"
        for j in range(1, x + 1):
            if x % j == 0:
                result_text += f"{j}\n"
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

# Function to clear the input and result
def clear():
    entry_number.delete(0, tk.END)
    text_result.delete(1.0, tk.END)

# Function to end the program
def end_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Divisibility Checker")
root.configure(bg='lightblue')  # Set background color

# Create and place the number input field
tk.Label(root, text="Enter a number:", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10)
entry_number = tk.Entry(root, bg='white', fg='black', font=('Arial', 12))
entry_number.grid(row=0, column=1, padx=10, pady=10)

# Create and place the result text area
text_result = tk.Text(root, height=10, width=30, bg='white', fg='black', font=('Arial', 12))
text_result.grid(row=1, columnspan=2, padx=10, pady=10)

# Create and place the check button
check_button = tk.Button(root, text="Check Divisibility", command=find_divisors, bg='green', fg='white', font=('Arial', 12))
check_button.grid(row=2, column=0, pady=10, padx=10, sticky="e")

# Create and place the continue button
continue_button = tk.Button(root, text="Continue", command=clear, bg='blue', fg='white', font=('Arial', 12))
continue_button.grid(row=2, column=1, pady=10, padx=10, sticky="w")

# Create and place the end button
end_button = tk.Button(root, text="End", command=end_program, bg='red', fg='white', font=('Arial', 12))
end_button.grid(row=3, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()

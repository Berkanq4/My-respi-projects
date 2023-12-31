import tkinter as tk

def count_to_number():
    # Get the number from the entry widget
    try:
        end_number = int(entry.get())
    except ValueError:
        # If the entry is not a number, display an error
        text_box.insert(tk.END, "Please enter a valid integer.\n")
        return

    # Insert numbers from 1 to end_number into the text box
    for number in range(1, end_number + 1):
        text_box.insert(tk.END, f"{number}\n")

def print_smile():
    # This function prints a smile in the text box
    text_box.insert(tk.END, ":)\n")

def perform_actions():
    # Clear the text box for new input
    text_box.delete('1.0', tk.END)
    
    # Call the functions that you want to execute
    count_to_number()
    print_smile()

window = tk.Tk()
window.title("Tkinter Counter")
window.geometry("500x500")

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

button = tk.Button(
    text="Click me!",
    width=10,
    height=3,
    bg="black",
    fg="#BDB76B",
    command=perform_actions  # Link the button to the perform_actions function
)
button.pack()

# Create a Text widget for displaying the numbers
text_box = tk.Text(window, height=10, width=50)
text_box.pack()

window.mainloop()

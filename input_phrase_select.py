from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, IntVar, Button, ttk
from tkinter.ttk import Style, Label
from ttkthemes import ThemedStyle
import sys

# Function to read file contents
def read_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

# Function to save word cloud image
def save_image(wordcloud):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    wordcloud.to_file(save_path)

# Function to calculate frequencies and generate word cloud
def calculate_frequencies(file_contents, phrase_length):
    # Tokenize the text into words and phrases
    words = file_contents.lower().split()
    phrases = [" ".join(words[i:i+phrase_length]) for i in range(len(words)-phrase_length+1)]

    # Count word frequencies
    frequencies = {}
    for phrase in phrases:
        frequencies[phrase] = frequencies.get(phrase, 0) + 1

    # Generate word cloud
    wordcloud = WordCloud()
    wordcloud.generate_from_frequencies(frequencies)

    # Display word cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # Save word cloud image
    # save_image(wordcloud)

# Get file contents from user
file_contents = read_file()

# Create GUI for selecting phrase length
root = Tk()
root.title("Word Cloud Generator")

# Apply themed style to the GUI
style = ThemedStyle(root)
style.set_theme("arc")  # Choose a theme (e.g., "clearlooks", "plastik", "radiance", "scidblue")

label = Label(root, text="Select phrase length:")
label.pack()

phrase_length_var = IntVar()
phrase_length_var.set(2)  # Default value

def generate_word_cloud():
    phrase_length = phrase_length_var.get()
    calculate_frequencies(file_contents, phrase_length)
    root.destroy()  # Close the window after generating word cloud
    sys.exit()      # Exit the program

options = ['Bigram (2)', 'Trigram (3)', 'Four-gram (4)', 'Five-gram (5)']

dropdown = ttk.Combobox(root, values=options, state="readonly")
dropdown.pack()

# Create tooltips for options
tooltips = {
    'Bigram (2)': "A pair of consecutive words.",
    'Trigram (3)': "A set of three consecutive words.",
    'Four-gram (4)': "A set of four consecutive words.",
    'Five-gram (5)': "A set of five consecutive words."
}

tooltip_label = Label(root, text="", wraplength=300)
tooltip_label.pack_forget()  # Initially hide the tooltip

def show_tooltip(option):
    tooltip_label.config(text=tooltips[option])
    tooltip_label.pack()

for option in options:
    dropdown.bind("<<ComboboxSelected>>", lambda e, option=option: show_tooltip(option))
    dropdown.bind("<Leave>", lambda e: tooltip_label.pack_forget())

button = Button(root, text="Generate Word Cloud", command=generate_word_cloud)
button.pack()

root.mainloop()

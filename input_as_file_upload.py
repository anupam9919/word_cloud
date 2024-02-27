from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import string
from nltk.corpus import stopwords
import nltk
import tkinter as tk
from tkinter import filedialog

# Initialize tkinter
root = tk.Tk()
root.withdraw()  # Hide the main window

# Function to open a file dialog and get the file path
def get_file_path():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    return file_path

# Function to read file contents
def read_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

# Calculate word frequencies and generate word cloud
def calculate_frequencies(file_contents):
    # Define punctuations and uninteresting words
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    uninteresting_words = set(stopwords.words('english'))
    
    # Process the text
    cleaned_text = ""
    for char in file_contents:
        if char.isalpha() or char.isspace():
            cleaned_text += char

    words = cleaned_text.lower().split()
    cleaned_words = [word for word in words if word not in uninteresting_words]

    # Count word frequencies
    frequencies = {}
    for word in cleaned_words:
        frequencies[word] = frequencies.get(word, 0) + 1

    # Generate word cloud
    wordcloud = WordCloud()
    wordcloud.generate_from_frequencies(frequencies)

    # Display word cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
# Get file path from user
file_path = get_file_path()

# Read file contents
file_contents = read_file(file_path)

# Generate word cloud
calculate_frequencies(file_contents)

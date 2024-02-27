from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import string
from nltk.corpus import stopwords
import nltk

# Sample text
text = "Your sample text goes here"

# Function to save text to file
def save_text_to_file(text):
    with open('input.txt', 'w') as file:
        file.write(text)

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

# Get user input
user_input = input("Enter text: ")
save_text_to_file(user_input)
calculate_frequencies(user_input)

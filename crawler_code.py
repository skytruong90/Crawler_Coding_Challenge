import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Function to extract the words from the HTML content
def extract_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    history_section = soup.find(id="History")
    h2_tag = history_section.find_previous("h2")
    next_tag = h2_tag.next_sibling
    text=""
    while(next_tag.name != "h2"):
        next_tag = next_tag.find_next()
        text +=next_tag.get_text()
    # Tokenize the text and remove any punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    # Convert all words to lowercase
    words = [word.lower() for word in words]
    return words

# Function to count the occurrences of each word
def count_words(words, exclude_words):
    # Create a Counter object to count the occurrences of each word
    word_count = Counter(words)
    # Remove any words that should be excluded from the search
    for word in exclude_words:
        del word_count[word]
    return word_count

# Function to return the top N most common words
def get_top_words(word_count, num_words):
    return word_count.most_common(num_words)

# Main function to scrape the webpage and output the most common words
def main(url, num_words=10, exclude_words=[]):
    # Get the HTML content of the webpage
    response = requests.get(url)
    html_content = response.text
    # Extract the words from the HTML content
    words = extract_words(html_content)
    # Count the occurrences of each word
    word_count = count_words(words, exclude_words)
    # Get the top N most common words
    top_words = get_top_words(word_count, num_words)
    # Output the results
    for word, count in top_words:
        print(f'{word}: {count}')

# URL of the webpage to scrape
url = "https://en.wikipedia.org/wiki/Microsoft"
# Get details from the user
num_words = int(input("Enter the number of words to return: "))
exclude_words = input("Enter a list of words to exclude from the search, separated by commas: ").split(',')

# Call the main function with the user-provided details
main(url, num_words, exclude_words)
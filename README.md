# Title: Crawler Coding Challenge
### This is a coding challenge that I worked on by myself and the programming language I used is Python. 

## How to install:
1. Clone the repository: https://github.com/skytruong90/Crawler_Coding_Challenge.git
2. The main code is inside a folder called crawler_code.py when you download everything.
3. Run the project with a Pycharm IDE.

## My Objective: 
Is to implement a console application that displays the most common words used in a portion of a webpage.
You can find more detail about the challenge in a document called, "Crawler Coding Challenge".

## Plan Sovling this challenge:
1. Import the necessary libraries: requests, BeautifulSoup, Counter, and re.
2. Define a function extract_words(html_content) that takes in the HTML content of a webpage as an argument.
3. Use the BeautifulSoup library to parse the HTML content and find the section of the page with the id attribute of "History".
4. Find the previous h2 tag and loop through the siblings of the h2 tag until the next h2 tag is found, concatenating all of the text of the elements between the two h2 tags into a variable 'text'.
5. Tokenize the text using a regular expression and remove any punctuation.
6. Convert all of the words to lowercase and return the resulting list of words.
7. Define a function count_words(words, exclude_words) that takes in a list of words and a list of words to exclude as arguments.
8. Create a Counter object to count the occurrences of each word.
9. Remove any words that should be excluded from the search.
10. Return the resulting Counter object.
11. Define a function get_top_words(word_count, num_words) that takes in a Counter object and the number of words to return as arguments.
12. Use the most_common() method of the Counter object to return the top N most common words.
13. Define the main function main(url, num_words=10, exclude_words=[]) that takes in the URL of the webpage to scrape, the number of words to return, and a list of words to exclude from the search.
14. Use the requests library to get the HTML content of the webpage.
15. Pass the HTML content to the extract_words function to get the list of words.
16. Pass the list of words and the list of excluded words to the count_words function to get the Counter object.
17. Pass the Counter object and the number of words to return to the get_top_words function to get the top N most common words.
18. Output the results.
19. Get the number of words to return from the user by calling input("Enter the number of words to return: ") and converting the input to integer.
20. Get the list of words to exclude from the user by calling input("Enter a list of words to exclude from the search, separated by commas: ") and splitting the input by comma.
21. Call the main function by passing the URL of the webpage to scrape, the number of words to return, and a list of words to exclude from the search obtained from the user.

## Explanation of the python code:
This code is a Python script that uses the requests library to scrape the contents of a webpage, in this case the Wikipedia page for Microsoft, and then uses the BeautifulSoup library to parse the HTML content of the page. The script defines several functions that work together to extract words from the page, count the occurrences of each word, and return the top N most common words.

The extract_words function takes in the HTML content of the webpage as an argument and uses the BeautifulSoup library to find a specific section of the page with the id attribute of "History". It then finds the previous h2 tag, and then loops through the siblings of the h2 tag until the next h2 tag is found. This loop concatenates all of the text of the elements between the two h2 tags into the variable 'text'. The function then tokenizes the text using a regular expression and removes any punctuation. It then converts all of the words to lowercase and returns the resulting list of words.

The count_words function takes in the list of words and a list of words to exclude as arguments. It creates a Counter object to count the occurrences of each word, and then removes any words that should be excluded from the search. It then returns the resulting Counter object.

The get_top_words function takes in the Counter object and the number of words to return as arguments, and then uses the most_common() method of the Counter object to return the top N most common words.

The main function is called with the URL of the webpage to scrape, the number of words to return, and a list of words to exclude from the search. It uses the requests library to get the HTML content of the webpage, and then passes this content to the extract_words function to get the list of words. It then passes this list of words and the list of excluded words to the count_words function to get the Counter object. Finally, it passes the Counter object and the number of words to return to the get_top_words function to get the top N most common words. It then outputs the results.

## Sceenshot:
Here is an example of what the output of the script might look like when run with the default URL of "https://en.wikipedia.org/wiki/Microsoft" and default values of 10 words to return and an empty list of excluded words:
<img src= "Screenshot 2023-01-26 155320.png" width="700">

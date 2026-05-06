# Day 35 Project: Word Counter
# Complete the TODOs below. Do not look at solution/ until you've tried.

import string   # string.punctuation gives you all punctuation characters

print('Enter text (blank line to finish):')

# TODO: Collect lines from the user until they enter a blank line.
#       Join all lines into a single string.

# TODO: Clean and split the text:
#       - Lowercase everything
#       - Remove punctuation from each word (hint: use .strip(string.punctuation))
#       - Split into a list of words
#       - Remove any empty strings that result from stripping

# TODO: Build a word frequency dictionary using a dict comprehension
#       or a counting loop. Each key is a word, value is its count.

# TODO: Report the following:
#       1. Total word count (including duplicates)
#       2. Number of unique words
#       3. Top 5 most frequent words and their counts
#          (hint: sort by value descending, take first 5)
#       4. The 3 least frequent words
#       5. All words that appear exactly once (sorted alphabetically)
#       6. All unique first letters used (as a sorted list)

# TODO: Ask the user for a word and report its frequency using .get()

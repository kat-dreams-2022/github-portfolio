# Import the sys module to use command line arguments.
import sys

# Retrieve all command line arguments after the script name and store them in the list 'duplicated_words'.
duplicated_words = sys.argv[1:]

# Convert 'duplicated_words' to a set to remove duplicates, then sort it in reverse order and store it in 'unique_words'.
unique_words = sorted(set(duplicated_words), reverse=True)

# Print the list, which contains only unique words sorted in descending order.
print(unique_words)

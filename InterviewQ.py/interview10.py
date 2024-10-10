# Python3 Program to find the total
# number of distinct years
import re

def distinct_years(str):
	matches = re.findall(r'(\d+-\d+-\d+)', str) # regex
	# extracting distinct years
	years = set(i[-4:] for i in matches)
	return len(years)


# Driver code
if __name__ == "__main__":
	str = "UN was established on 24-10-1945.\
		India got freedom on 15-08-1947."

	print(distinct_years(str))


# another approach learn both approches

def distinct_years_alternate(input_str):
    words = input_str.split()  # Split the input string into words
    years = set()  # Use a set to store distinct years
    
    for word in words:
        # Clean any trailing punctuation (e.g., '.', ',', etc.)
        clean_word = word.strip(".,")
        
        if '-' in clean_word:
            parts = clean_word.split('-')  # Split by '-'
            if len(parts) == 3 and parts[2].isdigit() and len(parts[2]) == 4:
                # Add only valid 4-digit years
                years.add(parts[2])
    
    return len(years)

# Driver code
if __name__ == "__main__":
    input_str = "UN was established on 24-10-1945. India got freedom on 15-08-1947, and Berlin Wall fell in 09-11-1989."
    print(distinct_years_alternate(input_str))


import re

def extract_names(sentence):
    # Regular expression to find capitalized words
    pattern = r'\b[A-Z][a-z]*\b'

    # Find all matches in the sentence
    matches = re.findall(pattern, sentence)

    # Filter out single-letter words
    names = [match for match in matches if len(match) > 1]

    return names

# Example usage:
sentence = "Krishi Harikrishnan tanish "
names = extract_names(sentence)
print(names)  # Output: ['John', 'Smith', 'Gemini']

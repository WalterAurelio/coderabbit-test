# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in the given string.
    
    Parameters:
        text (str): The string to reverse.
    
    Returns:
        str: The input string with characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence where words are sequences separated by whitespace.
    
    Parameters:
        sentence (str): The string to analyze.
    
    Returns:
        int: Number of words in `sentence`. An empty or whitespace-only string yields 0.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a Celsius temperature to Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32

import random
import string

# In-memory storage for URL mappings
# Key: short_code (str), Value: original long_url (str)
url_mapping = {}

def generate_short_code(length=6):
    """
    Generate a random short code consisting of letters and digits.

    Args:
        length (int): The number of characters in the generated short code.
                      Default is 6.

    Returns:
        str: Randomly generated short code.
    """
    # Choices: uppercase, lowercase letters, and digits
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def shorten_url(long_url):
    """
    Shorten a given long URL and store its mapping in memory.

    Args:
        long_url (str): The original URL to shorten.

    Returns:
        str: The shortened URL in the format:
             http://127.0.0.1:5000/<short_code>
    """
    # Generate a unique short code
    short_code = generate_short_code()

    # Store the mapping in memory
    url_mapping[short_code] = long_url

    # Return the full shortened URL
    return f"http://127.0.0.1:5000/{short_code}"


def get_original_url(short_code):
    """
    Retrieve the original long URL for a given short code.

    Args:
        short_code (str): The short code to look up.

    Returns:
        str or None: The original long URL if found, otherwise None.
    """
    # Fetch from the in-memory mapping
    return url_mapping.get(short_code)

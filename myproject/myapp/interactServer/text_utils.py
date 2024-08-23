import re
import pyperclip

def remove_line_breaks(text):
    # Remove leading and trailing spaces/tabs from each line
    text = re.sub(r'^[\t ]+|[\t ]+$', '', text, flags=re.MULTILINE)

    # Replace newlines between words with a space
    text = re.sub(r'(?<=\S)\n(?=\S)', ' ', text)

    return text

def setClipboard(answer):
    pyperclip.copy(answer)
    print("Data copied to clipboard.")
    
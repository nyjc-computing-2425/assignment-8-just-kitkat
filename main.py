def reverse(text):
    """
    Reverses `text`

    Argument
    ---------------
    text: str

    Return
    ---------------
    str
    """
    if text == "":
        return ""
    return reverse(text[1:]) + text[0]


def is_palindrome(text):
    """
    Checks if `text` is a palindrome

    Argument
    ---------------
    text: str

    Return
    ---------------
    bool
    """
    text = text.lower()
    new_text = ""
    for i in text:
        if i.isalnum():  # ignore punctuation and whitepsace
            new_text += i
    text = new_text
    # Base case
    if len(text) <= 1:
        return True

    return text[0] == text[-1] and is_palindrome(text[1:-1])

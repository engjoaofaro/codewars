"""
Description:
Write a function to split a string and convert it into an array of words.
"""
def string_to_array(s):
    if s:
        return s.split()
    else:
        return []
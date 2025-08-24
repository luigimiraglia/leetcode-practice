# Problem: String Compression
# Link: https://leetcode.com/problems/string-compression/
# Difficulty: Medium
# Approach: Use two pointers (read/write). Count consecutive characters and write the character
#           followed by its count if > 1.

from typing import List

def compress(chars: List[str]) -> int:
    write = 0
    read = 0

    while read < len(chars):
        char = chars[read]
        count = 0

        # Count occurrences of current char
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1

        # Write the character
        chars[write] = char
        write += 1

        # If count > 1, write each digit
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    # Trim the list to the new length
    while len(chars) > write:
        chars.pop()

    return write

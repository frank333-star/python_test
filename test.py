import re

text = "word is here"
match = re.search(r"\bisa\b", text)
if match:
    print("Example 11 - Word boundary: Found:", match.group())  # 输出: Found: word
else:
    print("Example 11 - Word boundary: Not found")
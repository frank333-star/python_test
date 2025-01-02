import re

# 示例 1: 字面量字符
# 匹配字符串 "hello"
text = "hello world"
match = re.search(r"hello", text)
if match:
    print("Example 1 - Literal characters: Found:", match.group())  # 输出: Found: hello
else:
    print("Example 1 - Literal characters: Not found")

# 示例 2: 任意字符
# 匹配 'a' 后跟任意字符，再跟 'b'
text = "acb"
match = re.search(r"a.b", text)
if match:
    print("Example 2 - Any character: Found:", match.group())  # 输出: Found: acb
else:
    print("Example 2 - Any character: Not found")

# 示例 3: 字符集
# 匹配字符串中的元音字母
text = "apple"
matches = re.findall(r"[aeiou]", text)
print("Example 3 - Character set: Vowels found:", matches)  # 输出: Vowels found: ['a', 'e']

# 示例 4: 字符集（范围）
# 匹配字符串中的小写字母
text = "Hello World"
matches = re.findall(r"[a-z]", text)
print("Example 4 - Character set (range): Lowercase letters found:", matches)  # 输出: Lowercase letters found: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

# 示例 5: 字符集（排除字符）
# 匹配所有非小写字母的字符
text = "Hello123"
matches = re.findall(r"[^a-z]", text)
print("Example 5 - Exclude characters: Non-lowercase characters found:", matches)  # 输出: Non-lowercase characters found: ['H', '1', '2', '3']

# 示例 6: 重复匹配（量词）
# 匹配零个或多个字母 'a'
text = "aaaab"
match = re.search(r"a*", text)
if match:
    print("Example 6 - Quantifier (zero or more): Found:", match.group())  # 输出: Found: aaaa
else:
    print("Example 6 - Quantifier (zero or more): Not found")

# 示例 7: 开始和结束匹配
# 匹配字符串以 'abc' 开头
text = "abc123"
match = re.match(r"^abc", text)
if match:
    print("Example 7 - Start match: Found:", match.group())  # 输出: Found: abc
else:
    print("Example 7 - Start match: Not found")

# 匹配字符串以 'abc' 结尾
text = "123abc"
match = re.search(r"abc$", text)
if match:
    print("Example 7 - End match: Found:", match.group())  # 输出: Found: abc
else:
    print("Example 7 - End match: Not found")

# 示例 8: 选择（OR 操作符）
# 匹配 'a' 或 'b'
text = "apple banana"
matches = re.findall(r"a|b", text)
print("Example 8 - OR operator: Found characters:", matches)  # 输出: Found characters: ['a', 'b', 'a', 'b', 'a', 'a']

# 示例 9: 分组（捕获组）
# 匹配 'ab' 重复一次或多次
text = "ababab"
match = re.search(r"(ab)+", text)
if match:
    print("Example 9 - Capturing group: Found:", match.group())  # 输出: Found: ababab
else:
    print("Example 9 - Capturing group: Not found")

# 示例 10: 非捕获组
# 匹配 'ab' 重复一次或多次，但不捕获
text = "ababab"
match = re.search(r"(?:ab)+", text)
if match:
    print("Example 10 - Non-capturing group: Found:", match.group())  # 输出: Found: ababab
else:
    print("Example 10 - Non-capturing group: Not found")

# 示例 11: 边界匹配
# 匹配完整单词 'word'
text = "word is here"
match = re.search(r"\bword\b", text)
if match:
    print("Example 11 - Word boundary: Found:", match.group())  # 输出: Found: word
else:
    print("Example 11 - Word boundary: Not found")

# 示例 12: 前瞻（Lookahead）
# 前瞻匹配后面跟着数字
text = "abc123"
match = re.search(r"(?=\d)", text)
if match:
    print("Example 12 - Lookahead: Found:", match.group())  # 输出: Found: (空，因为没有匹配内容，前瞻仅检查条件)
else:
    print("Example 12 - Lookahead: Not found")

# 示例 13: 后顾（Lookbehind）
# 后顾匹配前面是数字的字符串
text = "123abc"
match = re.search(r"(?<=\d)abc", text)
if match:
    print("Example 13 - Lookbehind: Found:", match.group())  # 输出: Found: abc
else:
    print("Example 13 - Lookbehind: Not found")

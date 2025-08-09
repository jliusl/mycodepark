def isValid(s):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(pairs[ch])
        elif not stack or stack[-1] != ch:
            return False
        else:
            stack.pop()

    return not stack


a = '()[]{}'
b = '{(})'
print(isValid(a))
print(isValid(b))
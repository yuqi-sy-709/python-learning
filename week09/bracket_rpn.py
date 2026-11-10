from stack import Stack

def is_valid(s):
    st = Stack()
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            st.push(ch)
        else:
            if st.is_empty():
                return False
            if st.pop() != match[ch]:
                return False
    return st.is_empty()

if __name__ == '__main__':
    print(is_valid("()[]{}"))   # True
    print(is_valid("(]"))       # False
    print(is_valid("([)]"))     # False
    print(is_valid("{[]}"))     # True
    print(is_valid("]"))        # False
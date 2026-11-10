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

def eval_rpn(tokens):
    st = Stack()
    for t in tokens:
        if t in "+-*/":
            b = st.pop()
            a = st.pop()
            if t == '+':
                st.push(a + b)
            elif t == '-':
                st.push(a - b)
            elif t == '*':
                st.push(a * b)
            else:
                st.push(int(a / b))
        else:
            st.push(int(t))
    return st.pop()

if __name__ == '__main__':
    print(is_valid("()[]{}"))   # True
    print(is_valid("(]"))       # False
    print(is_valid("([)]"))     # False
    print(is_valid("{[]}"))     # True
    print(is_valid("]"))        # False
    print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
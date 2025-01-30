class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_balanced(s):
    """Проверяет, сбалансирована ли строка скобок."""
    stack = Stack()
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if mapping[char] != top:
                return False
    return stack.is_empty()

if __name__ == '__main__':
    test_strings = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{",
        "{{[(])]}}",
        "[[{())}]",
        "([)]",
        "",
        "(())",
        "{{}"
    ]

    for s in test_strings:
        if is_balanced(s):
            print(f"'{s}' - Сбалансированно")
        else:
            print(f"'{s}' - Несбалансированно")
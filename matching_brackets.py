# Checks if brackets in a string are balanced: prints OK or ERROR
expression = input()
my_stack = []
statement = "OK"
# closing bracket must match the last opened one on top of the stack
braces_dictionary = { 
    "(": ")",
    "[": "]",
    "{": "}"
}
for char in expression:
    if char in "([{":
        my_stack.append(char)
        continue
    if char in ")]}":
        if len(my_stack):
            if braces_dictionary[my_stack[-1]] == char:
                del my_stack[-1]
            else:
                statement = "ERROR"
        else:
            statement = "ERROR"
if len(my_stack):
    statement = "ERROR"
print(statement)

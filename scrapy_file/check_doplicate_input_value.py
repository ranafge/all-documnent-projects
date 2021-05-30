
def accept_inputs(num):
    inputs = set()
    while len(inputs) < num:
        value = input('Enter a value: ')
        if value in inputs:
            print('Number already exists')
        inputs.add(value)
    return inputs


print(accept_inputs(3))

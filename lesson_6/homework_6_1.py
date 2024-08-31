my_input = input("Please enter the text: ")

all_symbols_in_my_input = set(my_input)

unique_symbols_counter = 0

for symbol in all_symbols_in_my_input:
    if my_input.count(symbol) == 1:
        unique_symbols_counter += 1

print(True if unique_symbols_counter>10 else False)

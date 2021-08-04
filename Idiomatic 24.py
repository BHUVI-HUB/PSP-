# Harmful

some_other_list = range(10)
some_list = list()
for element in some_other_list:
if is_prime(element):
some_list.append(element + 5)

# Idiomatic

some_other_list = range(10)
some_list = [element + 5
for element in some_other_list
if is_prime(element)]

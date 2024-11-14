def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params(3, 4, 5)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [2, True, "String"]
values_dict = {"a": 3, "b": False, "c": "str"}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [2.2, "Urban"]
print_params(*values_list_2, 42)
# the variable "args" is already defined
# args = ["script.py", "1", "2", "3", "4"]
my_list = []
for i in args[1:]:
    my_list.append(int(i))

print(str(my_list))

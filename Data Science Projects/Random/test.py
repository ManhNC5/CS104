

my_list = [0, 1, 2, 3, 4, 6]

result = max(my_list)

x = []

for i in range(result+1):
    if i not in my_list:
        x.append(i)
print(max(x))
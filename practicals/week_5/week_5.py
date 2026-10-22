names = ['Bob', 'Hans', 'Zahara', 'Amithbha', 'Dov', 'Maria']
print("QUESTION 1 (a):", names[-2:-5:-1])
print("QUESTION 1 (b):", names[1:2])
print("QUESTION 1 (c):", names[0:3:1])


names_1 = ['Bob', 'Hans', 'Zahara', 'Bob', 'Amithbha', 'Dov', 'Maria']
names_1.remove('Bob')
print(names_1)

part_3_string = ["Nothing much."]
new_list = ["Whats'up?"] + part_3_string
print(new_list)

part_4_list = [1, 3, 97, 0.1, -3.4, 86.95, -102]
part_4_list.sort(reverse=True)
print(part_4_list)

def every_second(original:list) -> list:
    new_list = []
    for i in range(len(original)):
        if i%2==0:
            new_list.append(original[i])
    return new_list

print("QUESTION 5: ", every_second([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


def every_ith(original:list, integer: int)-> int:
    new_list = []
    for i in range(len(original)):
        if i%integer ==0:
            new_list.append(original[i])
    return new_list

print("QUESTION 6: ", every_ith([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],3))

def every_second_revisited(original:list)-> list:
    return every_ith(original, 2)

print("QUESTION 7: ", every_second_revisited([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


def print_list(original:list):
    for i in range(len(original)):
        print(original[i], end=" ")
    print("")
print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

def print_list(original:list):
    for i in range(len(original)):
        if i%2!=0:
            print(original[i], end=" ")
    print("")
print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

def print_list_reverse_even(original:list):
    for i in range(len(original)):
        if i%2!=0:
            print(original[i], end=" ")
    print("")
print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print("###################### QUESTION 01 ###################")

def does_str_ends_with_letter_c(string: str) -> bool:
    return string.endswith('c')

def does_str_contains_only_letter(string:str) -> bool:
    return string.isalpha()

def replace_character_a_with_b(string:str) -> str:
    return string.replace('a', 'b')

def pad_number_with_zero(number:str)-> str:
    return number.ljust(6, "0")

def does_str_contains_only_uppercase(string:str)-> str:
    return string.isupper()

def remove_trainling_zeroes(string:str) ->str:
    return string.rstrip('0')

print(does_str_ends_with_letter_c("abc"))
print(does_str_ends_with_letter_c("ab"))

print(does_str_contains_only_letter("asdfawdsd"))
print(does_str_contains_only_letter("123412asdfasd"))

print(replace_character_a_with_b('aabb'))
print(replace_character_a_with_b('efgh'))

print(pad_number_with_zero("12"))
print(pad_number_with_zero('123456'))

print(does_str_contains_only_uppercase('Nishant'))
print(does_str_contains_only_uppercase('nishant'))

print(remove_trainling_zeroes('13432000'))
print(remove_trainling_zeroes('00000000'))


print("\n###################### QUESTION 01 ###################")
def question_second(part_one_string:str, part_two_string:str):
    print("Assigned the " + part_one_string + " to variable s")
    s = part_one_string
    
    print("\nPART - 01 (A) - Printing each character in a separate line.")
    for n in s:
        print(n)

    print("\nPART - 01 (B) - Print each character with a comma and a tab.")
    for index in range(len(s)):
        if(index != len(s)-1):
            print(s[index] + ",\t", end="")
        else:
            print(s[index])

    print("\nPART 02 - Print each character with a comma and a tab.")
    t = part_two_string
    for index in range(len(t)):
        print("Index: " , index , "Character: " ,  t[index])

    for index in range(len(t)):
        if(index%2 == 0):
            print(t[index])
    
question_second("superconductivity", "parsimonious")
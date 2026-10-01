def question_1_a(my_height: float) -> bool:
    tall: bool
    if (my_height >= 3.2):
        tall = True
    else:
        tall = False

    return tall

print("########################## QUESTION 1 - A: ")
print(question_1_a(3.1))
print(question_1_a(3.2))
print(question_1_a(3.3))

def question_1_b(my_height: float, min_height: float) -> bool:
    close: bool
    if((my_height > min_height) or (my_height - min_height) > 0.04):
        close = True
    else:
        close = False
    return close

print("########################## QUESTION 1 - B: ")
print(question_1_b(1.8, 1.7))
print(question_1_b(1.8, 1.85))
print(question_1_b(1.8, 1.84))

def question_1_c(mat_223: bool, mat_240: float) -> bool:
    csc_311 = mat_223 or mat_240
    return csc_311

print("########################## QUESTION 1 - C: ")
print(question_1_c(True, True))
print(question_1_c(True, False))
print(question_1_c(False, True))
print(question_1_c(False, False))

def question_1_d(mat_223: bool, mat_240: float, g:bool) -> bool:
    csc_311 = g and( mat_223 or mat_240)
    return csc_311

print("########################## QUESTION 1 - C: ")
print(question_1_d(True, True, True))
print(question_1_d(True, False, True))
print(question_1_d(False, True, False))
print(question_1_d(False, False, True))


"""
QUESTION 2
(e) - (c) '12'
(f) - (e) None of the above
(g) - (b) ‘111111'
(h) - '1'
(i) - 'c'
(j) - 'c'
(k) - 0
(l) - (a) - '' - because the slice start index is greater than the stop index
    - (b) - '' - because the slice start index and the stop index are same
    - (c) - 'n'
    - (d) - 'e'
    - (e) - '' - because the start index is greater than the stop index
    - (f) - '' - because the start index and the stop index are same
    - (g) - 'see'
    - (h) - 'is' - because it moves backword till the end, since there is no stop sign
    - (i) - 'i' - because it will move backword and will include the first character and then string will be empty.
    - (j) - 'silencery'
    - (k) - 'en'
"""
def leetcodes_answered(num_weeks: int, questions_per_week: int) -> int:
'''Return the total number of leetcode questions done over num_weeks
where in each week questions_per_week were answered
>>> leetcodes_answered(2, 30)
60
>>> leetcodes_answered(1, 8)
8
'''
return num_weeks * questions_per_week
# two of us are doing leetcode but at different rates and different amounts of time
person_a = leetcodes_answered(2, 8)
person_b_rate = 30
person_b = leetcodes_answered(1, person_b_rate)
grand_total = person_a + person_b
print("With the two of us combined, we will have done", grand_total, "questions")
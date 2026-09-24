''' Reminder that all the weights listed in this file ARE NOT a reflection
of how your real grade will be broken down in this course. Always,
refer to your syllabus for this information.
'''
def percentage(raw_mark: float, max_mark: float) -> float:
'''Return the percentage mark on a piece of work that received a mark of
raw_mark where the maximum possible mark is max_mark.
>>> percentage(15.0, 20.0)
75.0
NOTE: Please add extra examples!
'''
pass
def contribution(mark_as_percent: float, weight: float) -> float:
'''Given a piece of work that earned mark_as_percent percent and was
worth weight marks in the marking scheme, return the number of marks it
contributes to the final course mark.
>>> contribution(50.0, 12.5)
6.25
'''
return mark_as_percent * (weight / 100)
def raw_contribution(raw_mark: float, max_mark: float, weight: float) -> float:
'''Given a piece of work where the student earned raw_mark marks out of a
maximum of max_marks marks possible, return the number of marks it
contributes to the final course mark if this piece of work is worth weight
marks in the course marking scheme.
>>> raw_contribution(13.5, 15.0, 10.0)
9.0
'''
pass
def assignments_contribution(a1, a2, a3):
'''NOTE: The type annotations are missing! Please add them.
Given raw marks a1, a2 and a3 for the three course assignments,
calculate the contribution to the final course grade.
Assume each assignment is marked out of 50.
The assignments are worth 5%, 12.5%, and 5%, respectively, so the
return value of this function has a max of 22.5.
>>> assignments_contribution(30.0, 32.0, 20.0)
13
'''
pass
def prep_review_practice_contribution(prep_review: float, practice: float) -> int:
'''Given raw marks for prep and review (Sunday and Friday PCRS assignments)
and practice (clickers, PCRS practice, or labs), calculate the contribution
to the final course grade.
NOTE: Prep and Review is marked out of 27, and practice is marked out of 8.
The former has a contribution of 7.5%, and the latter has a contribution of
10%,
so the return value of this function has a max of 17.5.
>>> prep_review_practice_contribution(18.0, 8.0)
15
'''
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
    return (raw_mark / max_mark) * 100

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
    return percentage(raw_mark , max_mark) * (weight / 100)

def assignments_contribution(a1:float, a2:float, a3:float) -> int:
    '''NOTE: The type annotations are missing! Please add them.
    Given raw marks a1, a2 and a3 for the three course assignments,
    calculate the contribution to the final course grade.
    Assume each assignment is marked out of 50.
    The assignments are worth 5%, 12.5%, and 5%, respectively, so the
    return value of this function has a max of 22.5.
    >>> assignments_contribution(30.0, 32.0, 20.0)
    13
    '''
    return int(raw_contribution(30.0, 50, 5) + raw_contribution(32.0, 50, 12.5) + raw_contribution(20.0, 50, 5))

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
    return int(raw_contribution(prep_review, 27, 7.5) + raw_contribution(practice, 8, 10))

def term_work_mark(assignments: float, prep_review: float, practice: float, midterm: float) -> float:
    '''Given the contribution of:
    assignments (out of 22.5)
    prepare and review (out of 7.5)
    practice (out of 10)
    and midterm (as a percentage),
    return the term mark grade.
    NOTE: the midterm is worth 30%, so the returned mark represents a mark out of 70.
    >>> term_work_mark(16.0, 8.0, 5.0, 80.0)
    53.0
    '''
    return assignments + prep_review + practice + contribution(midterm, 30)

def exam_required(term_work: float, desired_grade: int) -> float:
    '''Given a term work mark of term_work representing 70% of the points in the
    grading scheme, calculate and return the percentage required on the exam for
    the final mark to be desired_grade.
    >>> exam_required(46.0, 82)
    120.0
    '''


    return (( desired_grade - term_work ) / 30 ) * 100
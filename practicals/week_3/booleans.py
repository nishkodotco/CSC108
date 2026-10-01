
print("###################### QUESTION 1 ###################3")

def marathon_time(half_marathon_time:int, is_hilly:bool)-> int:
    marathon_time = (half_marathon_time * 2) + 15
    if(is_hilly):
        return marathon_time + 15
    else:
        return marathon_time

print(marathon_time(30, True))
print(marathon_time(30, False))



print("###################### QUESTION 2 ###################")

def total_ticket_price(number_of_regular_tickets: int, number_of_students_tickets: int, is_holiday:bool) -> float:
    REGULAR_TICKET_PRICE = 4.5
    STUDENT_TICKET_PRICE = 2.5
    cost_of_regular_tickets = number_of_regular_tickets * REGULAR_TICKET_PRICE
    cost_of_students_tickets = number_of_students_tickets * STUDENT_TICKET_PRICE

    total_number_of_tickets = number_of_students_tickets + number_of_regular_tickets

    if(is_holiday):
        if(total_number_of_tickets >= 6):
            return (cost_of_regular_tickets + cost_of_students_tickets) * 0.95
        else:
            return (cost_of_regular_tickets + cost_of_students_tickets)
    else:
        if(total_number_of_tickets >= 10):
            return (cost_of_regular_tickets + cost_of_students_tickets) * 0.90
        else:
            return (cost_of_regular_tickets + cost_of_students_tickets)

print("10, 10, True: ")
print(total_ticket_price( 10, 10, True))
print("10, 10, False: ")
print(total_ticket_price(10, 10, False))


print("###################### QUESTION 3 ###################")

def australian_time(is_toronto_on_daylight:bool, is_melbourne_on_daylight:bool) -> int:
    if(is_melbourne_on_daylight and is_melbourne_on_daylight):
        return 15
    elif(is_toronto_on_daylight and not)
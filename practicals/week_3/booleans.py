def marathon_time(half_marathon_time:int, is_hilly:bool)-> int:
    marathon_time = (half_marathon_time * 2) + 15
    if(is_hilly):
        return marathon_time + 15
    else:
        return marathon_time

print("###################### QUESTION 1 ###################3")

print(marathon_time(30, True))
print(marathon_time(30, False))
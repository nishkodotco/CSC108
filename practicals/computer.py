distance = 40
print("Did you know your distance from school is")
print(distance)
print("km?")
speed = 1.25
commute_time = distance / speed
print("and your commute takes")
print(commute_time)
print("minutes due to traffic?")
# if there was no traffic you can go even faster
no_traffic_commute_time = distance / (speed + 0.25)
print("If you had no traffic your commute would take")
print(no_traffic_commute_time)
print("minutes.")
# let's pretend you're closer to the school
distance = distance - 25
print("Congrats! Your distance to the school is now")
print(distance)
# But see that no_traffic_commute_time hasn't changed
print("And your no traffic commute time is")
no_traffic_commute_time = distance / (speed + 0.25)
print(no_traffic_commute_time)

def log(activities, durations):
    if len(activities) != len(durations):
        print("The number of activities and durations should be the same.")
        return
    
    log = {}
    for i in range(len(activities)):
        activity = activities[i]
        duration = durations[i]
        log[activity] = duration
    
    return log
def calories_burned(duration):
    total_calories = 0
    for duration in duration:
        total_calories += duration * 3.5 
    return total_calories

def summary(activities, calories):
    print("Activity Summary:")
    for activity, duration in activities.items():
        print(f"{activity}: Duration = {duration} minutes, Calories Burned = {duration * 3.5}")
    print("Total Calories Burned for the day:", calories)

activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]
summary(log(activities, durations), calories_burned(durations))
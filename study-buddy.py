total_hours = int(input("Enter expected amount of hours to study per week: "))
num_courses = int(input("Enter total number of courses: "))
num_hours_per_course = total_hours/num_courses
my_courses = {}
hours_spent = {}
for i in range(num_courses):
    my_courses[i] = num_hours_per_course
    print("for course " +str(i))
    hours = int(input("Enter hours spent on the course: "))
    hours_spent[i] = hours
    if hours < my_courses[i]:
        my_courses[i] = my_courses[i] - hours
    else:
        my_courses[i] = 0
total_hours_spent = 0
for h in hours_spent:
    total_hours_spent += hours_spent[h]

print("You have the following hours remaining for each course:")
print(my_courses)
if total_hours_spent > total_hours:
    print("Take a break for your mental well-being!")
else:
    print("You're almost there!")
        


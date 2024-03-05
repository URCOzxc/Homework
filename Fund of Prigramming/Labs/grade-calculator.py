print("Please enter grades (Z terminates the list): ")

total_grade = 0
total_pass = 0
total_fail = 0
GPA = 0

letter = ()
while letter != "Z":

    letter = input()
    letter = letter.upper()
    if letter == "Z" and total_grade == 0:
        exit()
    if letter == "A":
        total_pass += 1
        total_grade += 1
        GPA += 4.0
    if letter == "B":
        total_pass += 1
        total_grade += 1
        GPA += 3.0
    if letter == "C":
        total_pass += 1
        total_grade += 1
        GPA += 2.0
    if letter == "D":
        total_pass += 1
        total_grade += 1
        GPA += 1.0
    if letter == "F":    
        total_fail += 1
        total_grade += 1
        GPA += 0.0
    
pass_grade = total_pass / total_grade * 100   
fail_grade = total_fail / total_grade * 100 
grade_point_average = GPA / total_grade

print(f"Students passing: {total_pass} ({pass_grade:.2f}%)")
print(f"Students failing: {total_fail} ({fail_grade:.2f}%)")

print(f"Class GPA: {grade_point_average:.2f}")
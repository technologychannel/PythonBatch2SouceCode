marks = int(input("Enter mark: "))

if marks >= 90 and marks<=100:
    print("Grade: A")
elif marks>=75 and marks<90:
    print("Grade: B")
elif marks>=50:
    print("Grade: C")
else:
    print("Fail")

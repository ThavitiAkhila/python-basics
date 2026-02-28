marks=int(input())
if marks >= 0 && marks <= 100:
    if marks > 90:
        print("out standing")
    elif marks >= 80:
        print("Distinction")
    elif marks >= 70:
        print("First class")
    elif marks >= 60:
        print("Second class")
    elif marks >= 50:
        print("Third class")
    else:
        print("Fail")
else:
    print("Invalid marks obtained")
agesList = [87,65,25,18,17,36,70,50,83,10]

for i in range(0, 10):
    age = input("Please enter an age: ")
    if age > 120 or age < 0:
        print("Please enter a valid age!")
    else:
        agesList[i] = age

print(agesList)

agesTotal = 0
for i in range(0,10):
    agesTotal += agesList[i]
average = agesTotal/10.0
print "The average age is: %.2f"% average

for i in range(0,10):
     if agesList[i] < average:
         print "%d is younger than the average"% agesList[i]
     else:
         print "Not younger than the average"

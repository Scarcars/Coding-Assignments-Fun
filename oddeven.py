import random
even = "even"
odd = "odd"
print ("Im thinkinking of a number. Is it odd or even?")
g = input()
i = random.randint (1, 256)
if (i % 2) == 0 and g == "even":
    print ("My number was", i, "Well done!")
elif (i % 2) != 0 and g == "odd":
    print ("My number was", i, "Well done!")
elif (i % 2) == 0 and g == "odd":
     print ("My number was", i, "Sorry!")
elif (i % 2) != 0 and g == "even":
     print ("My number was", i, "Sorry!")
else: print ("You didn't enter odd or even.  You forfeit!  (My number was", i,"if you're wondering.")



    

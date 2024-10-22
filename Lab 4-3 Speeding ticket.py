limit = int(input())
speed = int(input())

if speed <= limit - 10:
    print ("$50")
elif speed >= limit + 6 and speed <= limit + 20:
    print ("$75")
elif speed >= limit + 21 and speed <= limit + 40:
    print ("$150")
elif speed >= limit + 40:
    print ("$300")
else: print ("$0")

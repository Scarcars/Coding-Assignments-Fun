#SMC is the small monster collector
#IT is the price for an individual ticket
#GP is the price if the group is over 25

SMC = 9.50
IT = 12
GP = 7.25
Movie_goers = int(input("Enter the number of moviegoers:"))
P = GP * Movie_goers

if Movie_goers >= 25:
    print ("The total ticket price is", "${:.2f}" . format(P))
    
elif Movie_goers < 25:
    print("The total ticket price is", "${:.2f}" . format (Movie_goers * IT + SMC - IT))
    
    

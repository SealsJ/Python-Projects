#Create a function that will tell the user how long they have spent preparing the lasagna
def preparationTimeInMinutes(layers):
    prep_time = layers * 2
    print("It took you", prep_time, "minutes to prepare the lasagna.")

preparationTimeInMinutes(4)

#Define a variable that details the amount of time the lasagna needs to be in the oven
expected_minutes_in_the_oven = 40

#Establish a function that allows the user to determine the amount of time left
def remainingMinutesInOven(time_in):
    time_left = expected_minutes_in_the_oven - time_in
    print("There is", time_left, "minutes left for the lasagna to cook.")

remainingMinutesInOven(35)

#Now we create a function that adds the two previous functions
#to tell the user how much total time they have put in to 
#prepare the lasagna at that specific moment

def totalTimeInMinutes(layers, time_in):
    prep_time = layers * 2
    total_prep = prep_time + time_in
    print("You have spent a total of", total_prep, "minutes preparing this lasagna.")

totalTimeInMinutes(4, 35)
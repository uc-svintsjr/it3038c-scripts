#Name: Joseph Svintsitsky
#Module: Lab 5
#Due Date: 9/26/2021
#Assignment: Take a birthday date input and calculate how many seconds old you are
#Resources: https://gist.github.com/shahri23/1804a3acb7ffb58a1ec8f1eda304af1a

from datetime import datetime

#This will promt the end user to enter their DOB
print("Please enter your birthday (dd/mm/yyyy) ")
day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))

#This will calculate in the seconds the current date compared to the DOB and subtract it
timeInSeconds = (datetime.now() - datetime(day=day, month=month, year=year)).total_seconds()

#Dictionary object references the value calculated by the method above
print("You are {} seconds old.".format(timeInSeconds))
print("Feel old yet?")
__author__ = 'sreejath'
# Learn Python the Hard Way
print("I love chicken!")
print("Counting my chickens before they are hatched")
print("Hens", 5)
print("What is 3+2? ", 3 + 4 / 2.00)
print("What is 5-7?", 5 - 7)

cars = 40
drivers = 30
passengers = 90
passenger_capacity = 4
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * passenger_capacity

print("There are ", cars, " cars available.")
print("The car pool can transport ", carpool_capacity, " passengers.")
print(cars_not_driven, " cars cannot be used due to lack of drivers.")
print("Average passengers per car is ", passengers / cars_driven)
print("Unused space per car is ", passenger_capacity - (passengers / cars_driven))
print("Total excess capacity is ", carpool_capacity - passengers)
print("If ", cars_not_driven, " more passengers could drive, this car pool could support an additional ",
      (cars * passenger_capacity) - carpool_capacity, " passengers")

my_name = "Sreejath"
my_height = 174
my_weight = 70
my_age = 39

print('My name is %s. I am %d cm tall, weigh %d kgs and am %d years old' % (my_name, my_height, my_weight, my_age))
print("%r" % ('asdf'))

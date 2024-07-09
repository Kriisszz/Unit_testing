import unittest


# adding the function that calculates the total cost of the car rental.
def rental_cost_f(rental_days, rental_cost):
    return rental_days*rental_cost


# function to get the hotel cost
def hotel_cost_f(num_nights, hotel_cost):
    return num_nights*hotel_cost


# function to calculate the flight price
def plane_cost_f(city_flight):
    # creating random destinations with flight prices.
    abudhabi_flightprice = 500
    phuket_flightprice = 550
    brussels_flightprice = 70
    amsterdam_flightprice = 75
    if city_flight.lower() == "abudhabi":
        plane_cost = abudhabi_flightprice
    elif city_flight.lower() == "phuket":
        plane_cost = phuket_flightprice
    elif city_flight.lower() == "brussels":
        plane_cost = brussels_flightprice
    elif city_flight.lower() == "amsterdam":
        plane_cost = amsterdam_flightprice
    else:
        plane_cost = 0
    return plane_cost


# function to choose the city
def city_flight_fun():
    # asking for the details of the travel
    while True:
        try:
            city_flight = str(input("Add your destination please."))
            if city_flight.lower() == "abudhabi":
                break
            elif city_flight.lower() == "phuket":
                break
            elif city_flight.lower() == "brussels":
                break
            elif city_flight.lower() == "amsterdam":
                break
            else:
                city_flight = str(input("Destination can only be Abudhabi, \
Phuket, Amsterdam or Brussels."))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return city_flight


# function to get the total cost of the holiday
def total_cost_f(rental_price, plane_price, hotel_price):
    return rental_price+plane_price+hotel_price


city_flight = city_flight_fun()

while True:
    try:
        num_nights = int(input("Please add the number of nights you are going\
to spend there."))
        if num_nights > 0:
            break
        else:
            print("Please add a positive number!")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
while True:
    try:
        rental_days = int(input("Please add the number of days you are \
going to rent a car for."))
        if rental_days > 0:
            break
        else:
            print("Please add a positive number!")
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")


# creating random destinations with rental prices.
abudhabi_rentalprice = 5
phuket_rentalprice = 6
brussels_rentalprice = 7
amsterdam_rentalprice = 8

# creating random hotel prices for each destination.
abudhabi_hotelprice = 20
phuket_hotelprice = 15
brussels_hotelprice = 40
amsterdam_hotelprice = 45

# adding an extra if method and variable to determine the exact prices
if city_flight.lower() == "abudhabi":
    hotel_cost = abudhabi_hotelprice
    rental_cost = abudhabi_rentalprice
elif city_flight.lower() == "phuket":
    hotel_cost = phuket_hotelprice
    rental_cost = phuket_rentalprice
elif city_flight.lower() == "brussels":
    hotel_cost = brussels_hotelprice
    rental_cost = brussels_rentalprice
elif city_flight.lower() == "amsterdam":
    hotel_cost = amsterdam_hotelprice
    rental_cost = amsterdam_rentalprice
else:
    print("destination is not available")

# function to get the total price for the hotel
hotel_price = hotel_cost_f(num_nights, hotel_cost)

# getting the flight price
plane_price = plane_cost_f(city_flight)

rental_price = rental_cost_f(rental_days, rental_cost)
# calculating the total cost of the holidays.

total_price = total_cost_f(rental_price, plane_price, hotel_price)
print("The total cost of your holidays would be £", total_price, ".")
print("This is consisted of £", hotel_price, " for the hotel")
print(" and £", rental_price, "for car rental and also £", plane_price, "\
    for the flight ticket")


# Unit Testing
class TestHoliday(unittest.TestCase):
    """There are 3 use cases Im testing, first is to get the flight price,
    second is to get the cost of the hotel and third
    is the total cost of the holiday"""

    # use case number 1
    def test_plane_cost_fun(self):
        word = "brussels"

        result = plane_cost_f(word)

        self.assertEqual(result, 70)

    # use case number 2
    def test_hotel_cost_fun(self):
        test_num_one = 8
        test_num_two = 40

        result = hotel_cost_f(test_num_one, test_num_two)

        self.assertEqual(result, 320)

    # use case number 3
    def test_total_cost_f(self):
        test_num_one = 120
        test_num_two = 550
        test_num_three = 200

        result = total_cost_f(test_num_one, test_num_two, test_num_three)

        self.assertEqual(result, 870)


if __name__ == "__main__":
    unittest.main()

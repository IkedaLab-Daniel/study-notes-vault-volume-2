class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        open_seats = self.open_seats()

        if open_seats > 0:
            self.passengers.append(name)
            print("Added")
        else:
            print("No more seat left")

    def open_seats(self):
        passengers_count = len(self.passengers)
        return self.capacity - passengers_count
    

flight = Flight(3)
flight.add_passenger("Mark")
flight.add_passenger("Daniel")
flight.add_passenger("Callejas")
flight.add_passenger("foo")
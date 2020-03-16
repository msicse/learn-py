class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():
    #create flight object
    f = Flight(origin="New York", destination= "Paris", duration=540)

    # UPDATE duration
    f.duration +=10
    # print details
    print(f.origin)
    print(f.destination)
    print(f.duration)


if __name__ == "__main__":
    main()


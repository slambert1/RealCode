#This program calculates the falling distance, in meters, from 1 to 10.
#This prgroam can be used to determine the distance an object falls in a specific time period.
g = 9.8
def main():
    for time in range (1,11):
        total_distance = falling_distance(time)
        print('The falling distance is', falling_distance(time), 'meters')

def falling_distance(time):
    d = .5 * g * (time**2)
    return d

main()

def distanceBetweenBusStops(distance, start, destination):
    if start> destination:
        start,destination = destination , start
    clock_wise_dt = sum(distance[start:destination])
    counter_clock_wise = sum(distance) - clock_wise_dt
    return min(clock_wise_dt,counter_clock_wise)


if __name__ == '__main__':
    distance = [7,10,1,12,11,14,5,0]
    start = 7
    destination = 2
    print(distanceBetweenBusStops(distance, start, destination))
# A hotel has N advanced booking for the next season and it has K rooms.
# Bookings contain an arrival date and a departure date.
# Find out whether there are enough rooms in the hotel to satisfy the demad



def hotel(arrive, depart, K):
    events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
    events.sort(key=lambda x: (x[0], x[1]))
    guests = 0
    for e in events:
        if e[1] == 1:
            guests += 1
        elif e[1] == 0:
            guests -= 1
        if guests > K:
            return False
    return True

A = [1, 3, 5]
B= [2, 6, 8]
C = 1
print hotel(A, B, C)

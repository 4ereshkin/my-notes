atp = [
    ("АТП1", 55.669612, 37.432848),
    ("АТП2", 55.677900, 37.578832),
    ("АТП3", 55.650003, 37.535391),
]

senders = [
    ('A1', 55.686456, 37.433226),
    ('A2', 55.645701, 37.472781),
    ('A3', 55.652240, 37.519359),
    ('A4', 55.673585, 37.519495),
    ('A5', 55.689595, 37.557605),
    ('A6', 55.677544, 37.486400),
    *atp
]

receivers = [
    ('B1', 55.678255, 37.448949),
    ('B2', 55.689558, 37.483274),
    ('B3', 55.661906, 37.455515),
    ('B4', 55.656305, 37.479661),
    ('B5', 55.652839, 37.499034),
    ('B6', 55.668998, 37.480567),
    ('B7', 55.670867, 37.496607),
    ('B8', 55.660185, 37.554447),
    ('B9', 55.676162, 37.536855),
    ('B10', 55.692189, 37.528762),
    ('B11', 55.682019, 37.516726),
    *atp
]



from math import sin, cos, sqrt, atan2, radians 

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Determine the column widths
sender_width = 10
receiver_width = 10

# Print headers
header = ["Sender"] + [receiver[0] for receiver in receivers]
print(f"{'Sender':<{sender_width}}", end='')
for rec in receivers:
    print(f"{rec[0]:<{receiver_width}}", end='')
print()

for sender in senders:
    print(f"{sender[0]:<{sender_width}}", end='')
    for receiver in receivers:
        distance = calculate_distance(sender[1], sender[2], receiver[1], receiver[2])
        print(f"{distance:.0f}".ljust(receiver_width), end='')
    print()
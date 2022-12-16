class Elem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Elem with x: {self.x}, y: {self.y}"

def falls_within(x, y, sb):
    max_dist = abs(sb[0].x - sb[1].x) + abs(sb[0].y - sb[1].y)
    sensor = sb[0]
    min_x, max_x = sensor.x - max_dist, sensor.x + max_dist
    min_y, max_y = sensor.y - max_dist, sensor.y + max_dist
    if x >= min_x and x < sensor.x:
        return y >= sensor.y - abs(x - min_x) and y <= sensor.y + abs(x - min_x)
    elif x == sensor.x:
        return y >= min_y and y <= max_y 
    elif x > sensor.x and x <= max_x:
        return y >= sensor.y - abs(x - max_x) and y <= sensor.y + abs(x - max_x)

with open("day15.txt") as f:
    sensor_beacons = []

    for line in f:
        s = str.replace(line, "Sensor at x=", "")
        s = str.replace(s, ": closest beacon is at x=", ",")
        s = str.replace(s, "y=", "")
        s = str.replace(s, " ", "")
        s = str.strip(s)
        s = str.split(s, ",")

        sensor_beacons.append([Elem(int(s[0]), int(s[1])), Elem(int(s[2]), int(s[3]))])

    min_x, max_x = float("inf"), float("-inf")
    for sb in sensor_beacons:
        max_dist = abs(sb[0].x - sb[1].x) + abs(sb[0].y - sb[1].y)
        min_x = min(min_x, sb[1].x - max_dist)
        max_x = max(max_x, sb[1].x + max_dist)
    
    ans = 0
    y = 10
    for x in range(min_x, max_x + 30000):
        print(f"{x} out of {max_x}, ans: {ans}")
        for sb in sensor_beacons:
            if falls_within(x, y, sb):
                ans += 1
                break

    print(ans)
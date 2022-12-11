class CRT:
    def __init__(self, screen, pos):
        self.screen = screen
        self.pos = pos

    def adjust_crt_screen(self, mid_pos):
        self.screen += "#" if self.pos in [mid_pos - 1, mid_pos, mid_pos + 1] else "."
        self.pos += 1
        if (self.pos) % 40 == 0 and self.pos != 0: 
            self.pos = 0
            self.screen += "\n"

with open('day10.txt') as f:
    measurements = 0
    x = 1
    mid_pos = 1
    cycle = 1
    crt = CRT("", 0)
    for line in f:        
        if str.startswith(line, "addx"):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]: measurements += x * cycle
            crt.adjust_crt_screen(mid_pos)
            
            cycle += 1
            sp = str.split(str.strip(line), " ")
            x += int(sp[1])
            crt.adjust_crt_screen(mid_pos)
            mid_pos += int(sp[1])
            if cycle in [20, 60, 100, 140, 180, 220]: measurements += x * cycle

        elif str.startswith(line, "noop"):
            cycle += 1
            crt.adjust_crt_screen(mid_pos)
            if cycle in [20, 60, 100, 140, 180, 220]: measurements += x * cycle

    print(measurements)
    print(crt.screen)
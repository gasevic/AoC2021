import sys

x=0
z_aim=0
z2=0

with open(sys.argv[-1]) as f:
    for line in f:
        if line.split()[0] == "forward" :
            x = x + int(line.split()[1])
            z2 = z2 + z_aim * int(line.split()[1])
        if line.split()[0] == "down" :
            z_aim = z_aim + int(line.split()[1])
        if line.split()[0] == "up" :
            z_aim = z_aim - int(line.split()[1])

print('Part1 {}'.format(x*z_aim))
print('Part2 {}'.format(x*z2))
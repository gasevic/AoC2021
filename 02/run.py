import sys

x=0
z=0
x2=0
z2=0
aim=0

with open(sys.argv[-1]) as f:
    for line in f:
        if line.split()[0] == "forward" :
            x = x + int(line.split()[1])
            x2 = x2 + int(line.split()[1])
            z2 = z2 + aim * int(line.split()[1])
        if line.split()[0] == "down" :
            z = z + int(line.split()[1])
            aim = aim + int(line.split()[1])
        if line.split()[0] == "up" :
            z = z - int(line.split()[1])
            aim = aim - int(line.split()[1])

print('Part1 {}'.format(x*z))
print('Part2 {}'.format(x2*z2))
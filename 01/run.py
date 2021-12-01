import sys

with open(sys.argv[-1]) as f:
    lines = f.readlines()

tmp = 0
tmp2 = 0
count_part1=-1
count_part2=-1
sum1=0
sum2=0
sum3=0
i=0

for line in lines:
    i = i + 1

    if i == 1 :
        sum1 = sum1 + int(line)
    if i == 2 :
        sum1 = sum1 + int(line)
        sum2 = sum2 + int(line)
    if i == 3 :
        sum1 = sum1 + int(line)
        sum2 = sum2 + int(line)
        sum3 = sum3 + int(line)

    if i == 3 :
        if sum1 > tmp2 :
            count_part2 = count_part2 + 1
        tmp2 = sum1
        sum1 = sum2
        sum2 = sum3
        sum3 = 0
        i = 2


    if sum2 > sum1:
        count_part2 = count_part2 + 1


    if int(line) > int(tmp):
        count_part1 = count_part1 + 1
    tmp = line

print('Part1 {}.'.format(count_part1))
print('Part2 {}.'.format(count_part2))
     
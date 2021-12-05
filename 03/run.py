import sys

i=0
array=[]
o_numbers=[]
co2_numbers=[]
gamma=""
epsilon=""
o=""
co2=""

# Part1:

def split_string(word):
    return [char for char in word]

with open(sys.argv[-1]) as f:

    first_line = split_string(f.readline().strip())
    array = [0 for i in range(len(first_line))]

with open(sys.argv[-1]) as f:
    for line in f:
        for char in split_string(line.strip()):
            if char == '0':
                array[i]=array[i]-1
            if char == '1':
                array[i]=array[i]+1
            i=i+1
        i=0
        
for char in array:
    if char < 0:
        gamma+=str(0)
        epsilon+=str(1)
    if char > 0:
        gamma+=str(1)
        epsilon+=str(0)

# Part2: Fill lists with numbers

with open(sys.argv[-1]) as f:
    for line in f:
        if split_string(line.strip())[0] == '1':
            o_numbers.append(line.strip())
        if split_string(line.strip())[0] == '0':
            co2_numbers.append(line.strip())     

# Part2: Sorting lists
        
def sorting(digit,list,method):
    if len(list) == 1:
        return
    if digit == 0:
        return
    temp_value=0

    for entry in list:
        if split_string(entry.strip())[digit] == '1':
            temp_value=temp_value+1
        if split_string(entry.strip())[digit] == '0':
            temp_value=temp_value-1

    for entry in list[:]:
        if method == "most_common":
            if temp_value < 0:
                if split_string(entry.strip())[digit] != "0":
                    list.remove(entry)
            if temp_value > 0:
                if split_string(entry.strip())[digit] != "1":
                    list.remove(entry)
            if temp_value == 0:
                if split_string(entry.strip())[digit] != "1":
                    list.remove(entry)
        if method == "least_common":
            if temp_value > 0:
                if split_string(entry.strip())[digit] != "0":
                    list.remove(entry)
            if temp_value < 0:
                if split_string(entry.strip())[digit] != "1":
                    list.remove(entry)
            if temp_value == 0:
                if split_string(entry.strip())[digit] != "0":
                    list.remove(entry)
    return
            
for j in range(0,len(first_line)):
    sorting(j,o_numbers,"most_common")
    sorting(j,co2_numbers,"least_common")

print('Part1 {}'.format(int(gamma,2)*int(epsilon,2)))
print('Part2 {}'.format(int(o_numbers[0],2)*int(co2_numbers[0],2)))
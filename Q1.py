import sys

column = int(sys.argv[1])
file = sys.argv[2]
unsorted = open(file,'r')
tablelines = unsorted.readlines()

sort = []
count = 0

for line in tablelines:
		sort.append(line.split(' ')[column])
		sort.sort()

output = ",".join(sort)
text_file = open("ans1.txt",'w')
text_file.write(output)
text_file.close()
unsorted.close()



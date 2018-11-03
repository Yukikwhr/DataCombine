import sys
args = sys.argv

if len(args) < 3:
    print("Please select two or more data")
    sys.exit()

for i in range(1, len(args)):
    fr = open(args[i], 'r')
    lines = fr.readlines()
    fr.close()
    with open('combined.csv', 'a') as fw:
        for line in lines:
            fw.writelines(line)

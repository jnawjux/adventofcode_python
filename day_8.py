fileObj=open("day_8_input.txt","r")
content=[(i.split(" ")) for i in fileObj.readlines()]


acc = 0
run_code = list()

run = 0

print(content[0][1][1:])

def run_line(i):
    if content[i][0] == 'acc':
        run_code.append(i)
        acc = acc + int(content[i][1][1:]) if content[run][1][0] == "+" else acc - int(content[i][1][1:])
        run_code.append(i)
        run += 1
    elif content[i][0] == 'jmp':
        run_code.append(i)
        jmp_total = int(content[i][1][1:]) - 1
        run = run + jmp_total if content[i][1][0] == "+" else run - jmp_total
    else:
        run_code.append(i)
        run += 1


while run < len(content):
    if run in run_code:
        acc = 5
        run_line(run)
    else:
        run_line(run)



print(acc)
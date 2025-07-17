ldel= input("Enter exact line:")
with open('log.txt', 'r') as f :
    lines= f.readlines()
with open('log.txt', 'w') as f :
    for line in lines:
        if line.strip() != ldel.strip():
            f.write(line)
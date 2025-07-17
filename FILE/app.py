with open("log.txt", 'a+') as f:
    f.write("\n Six ")
    f.seek(0)
    data=f.read()
    print("Current data: \n",data)
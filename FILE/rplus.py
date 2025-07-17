with open("file 1.txt",'w+') as f:
    f.write("Hello Students!!!!")
    f.seek(0)
    data=f.read()
    print("Previous:",data)
    new_data= data.replace("Students", "Future IT Employees")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file 1.txt",'r') as f:
    print("Latest:", f.read()) 
    
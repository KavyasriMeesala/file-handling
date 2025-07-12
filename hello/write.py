with open("sample_binary.bin", "wb") as file :
    data= b'\x48\x65\x6C\x6C\x6F'
    file.write(data)
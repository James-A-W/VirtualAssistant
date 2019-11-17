def Calculate(string):
    print("\n\n\n"+string)
    spl = string.split(" ")
    numb1 = spl[0]
    numb2 = spl[2]
    calc = spl[1]
    print(numb1,calc,numb2)
    if calc == "+":
        return int(numb1)+int(numb2)
    elif calc == "-":
        return int(numb1)-int(numb2)

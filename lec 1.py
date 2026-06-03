a = int(input("ENTER THE FIRST NUMBER -->"))

b = int(input("INPUT YOUR SECOND NUMBER -->"))

OPERATION = str(input("input the operation u wanna do in words --->"))

if OPERATION in ["addition" , "sum" , "plus" , "+"]:
    print(a + b)

elif OPERATION in ["subraction" or "minus" or "-"]:
    print( a - b)

elif OPERATION in ["multiply" , "multiplication" , "*"]:
    print(a * b)

elif OPERATION in ["divison" , "division",  "/"]:
    print(a/b)

else:
    print("invalid operation")




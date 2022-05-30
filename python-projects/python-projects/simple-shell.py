
"""
This is a simple shell made using python.
It can only support arithmetic calculations
A newe version of this software is soon to be 
released and our team is working towards it. 
""" 
while 1:
    x = input(">>>")
    if x == "Exit":
        break

    try:
        y = eval(x)
        if y: print(y)
    except:
        try:
            exec(x)

        except Exception as e:
            print("Error:", e)







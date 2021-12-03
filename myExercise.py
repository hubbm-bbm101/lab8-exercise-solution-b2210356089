import sys
with open(sys.argv[1]) as file:
    for i in sys.argv[2].split(","):
        a = 0
        for line in file:
            if line.startswith(i):
                print("Name: {}, University: {}".format(i, line.split(":")[1]))
                a += 1
        if a == 0:
            print("No record of {} was found!".format(i))
                
          





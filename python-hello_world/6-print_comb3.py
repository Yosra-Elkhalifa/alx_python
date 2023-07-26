for i in range(9):
    if i == 8 :
        print("{}{}".format(i,j))
        continue
    for j in range(i+1, 10):
        print(end="{}{}, ".format(i,j))
        
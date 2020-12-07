def output(v, diff_x, diff_y, acc, dir, flex):
    #results = input()
    """
    if(acc[0][9]>1):
        print("left", acc)
        results = "left"
    elif(acc[0][9]<-1):
        print("right",acc)
        results = "right"
    """
    #print("diff ", diff)
    if(flex[-1]<0.6):
        results = "home"

    elif(dir=="up"):
        if(acc[1][-1]<-2):
            print("up", diff_y)
            results = "up10"
        else:
            #dir = ""
            return "dir"
    elif(dir=="down"):
        if(acc[1][-1]>2):
            print("down", diff_y)
            results = "down10"
        else:
            #dir = ""
            return "dir"
    elif(diff_x[9]>15):
        print("left", diff_x)
        results = "left"
    elif(diff_x[9]<-15):
        print("right",diff_x)
        results = "right"
    elif(diff_y[9]>15):
        print("down", diff_y)
        results = "down10"
    elif(diff_y[9]<-15):
        print("up", diff_y)
        results = "up10"
    else:
        return ""
    print("results ", results)
    return results
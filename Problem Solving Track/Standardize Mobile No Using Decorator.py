def wrapper(f):
    def fun(l):
        # complete the function
        number_sorted=[]
        
        for item in (l):
            #Some Prefix Present
            if len(item)>10:
                if item[0]=='0':
                    # print("O found")
                    number_sorted.append(f"+91 {item[1:6]} {item[6:]}")

                elif item[0]=='9' and item[1]=='1':
                    number_sorted.append(f"+91 {item[2:7]} {item[7:]}")
                
                elif item[0]=='+' and item[1]=="9" and item[2]=="1":
                    number_sorted.append(f"+91 {item[3:8]} {item[8:]}")

            #No prefix Present
            else:
                number_sorted.append(f"+91 {item[0:5]} {item[5:]}")

        for item in sorted(number_sorted):
            print(item)

    return fun

@wrapper
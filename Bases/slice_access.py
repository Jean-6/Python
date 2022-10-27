def main() :
    sub1=my_list[:3]
    #print("sub1 : {}".format(sub1))
    sub2=my_list[1:4]
    #print("sub2 : {}".format(sub2))
    sub3=my_list[len(my_list)-3:]
    #print("sub3 : {}".format(sub3))
    sub4=my_list[::2]
    #print("sub4 : {}".format(sub4))
    sub5=my_list[1::2]
    #print("sub5 : {}".format(sub5))
    sub6=my_list[::-1]
    #print("sub6 : {}".format(sub6))

if __name__ == "__main__":
    main()
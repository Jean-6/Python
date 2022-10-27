def main() :
    count=1
    value=input("")
    value=int(value)
    while count<=10:
        print("{} x {} = {}".format(count,value,(count*value)))
        count=count+1


if __name__ == "__main__":
    main()
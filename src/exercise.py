def main():
    #write your code below this line
    oldest = 0

    while True:
        line = input()
        
        if line == '':
            break

        data =  line.split(',')
        age = int(data[1])

        if age > oldest:
            oldest = age

    print("Age of the oldest: " + str(oldest))

if __name__ == '__main__':
    main()

def main():
    print("Hello World!")

def variables():
    x = 7
    b = "Robert"
    print(x)
    print(b)
    print(str(x) + "   " + " hello "+ str(4))
    print(x * 2)
    print( b * 2 )
    print(type(x))
    print(type(b))
    print(type(7.3))

def string():
    print("---- strings ----")
    str1 = "mine"
    str2 = "craft"
    str3 = 'Steve'
    str4 = """loves 
to 
mine
maybe"""

    print(str1, str2, str3, str4)
    print(str1 + " " + str2)
    x = 42
    str5 = f"X equals {x}"
    print(str5)

def loops():
    print("---- loops ----")
    for i in range(5):
        print(i)

    total = 0
    for i in range(101):
        total = total + i
        #print(f"{total-i} + {i} = {total}")
    print(total)

    total = 1
    for i in [1, 12, 42]:
        total = total * i
    print(total)

    x = 0
    while x < 9:
        x = x + 2
        print(x)

    x = 0
    while True:
        x = x + 2
        print(x)
        if x > 10:
            break

def sequences():
    print("---- sequences ----")
    my_list = [1, 12, 42]
    print(my_list)
    print(my_list[2])
    my_list[2] = 79
    print(my_list)
    my_list.append(12)
    print(my_list)
    my_list.append(-12)
    print(my_list)
    my_list.append("Robert")
    print(my_list)

    print(f"length of the list is: {len(my_list)}")

    for item in my_list:
        print(item)





# main()
# variables()
# string()
# loops()
sequences()
print("dsbdf")
l = [3, "#rf", "fsd"]
print(l)


def test():
    print("this is my very first function")


test()
type(test)
test() + "sufha "  # print always return none data type


def test2():
    return "this is my very first return "


test2()  # return string
test2() + "vikash"


def test3():
    return "sudha", 23, 54.23, [1, 2, 3]


test3()  # en chiz ko as a tuple return kr diya

a, b, c, d = test3()
a
b
c
d


a = 22
b = 34
a
b


a, b = 1, 4
a
b


def test5():
    a = 5 + 6 / 7
    return a


test5()


def test6(a, b, c):
    d = a + b / c
    return d


test6(2, 5, 6)


def test7(a, b):
    return a + b


test7("sudh", "a")
test7(556, 5)

# in python it doesn't require the parameter data type and neither the  data type of variable
# its self paced learning app so it will automatically/internally understand the data type of given entity


l = test7([5, 15, 5215, 5], ["sudh", "vikash"])


print(l)
# write a function to separate the  int in diff  list l1


def test8(l):
    l1 = []
    l2 = []
    for i in l:
        if type(i) == int or type(i) == float:
            l1.append(i)
        elif type(i) == str:
            l2.append(i)

    return l1, l2
    # return {'numbers': l1, 'strings': l2}


test8(l)


l3 = [12, 2, 4, 6, 5, "sudha", "fedsv", [2, 15, 5, 5, 8, 5, 8]]


def test9(l):
    l1 = []
    l2 = []
    for i in l:
        if type(i) == int or type(i) == float:
            l1.append(i)
        elif type(i) == str:
            l2.append(i)
        elif type(i) == list:
            for j in i:
                if type(j) == int or type(j) == float:
                    l1.append(j)
    return l1, l2


test9(l3)

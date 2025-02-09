name = "dave"
count = 1



# greeting("David")

def another():
    color = "blue"
    global count
    count += 1
    print(count)
    def greeting(name):
        # nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()
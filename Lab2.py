

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    numlist=[]
    userinput = input()
    numliststr = userinput.split(",")
    print(numliststr)
    for numstr in numliststr:
        numlist.append(float(numstr))
    print(numlist)
    return numlist


def calc_average(inputlist):
    print("calc_average")
    average = sum(inputlist)/len(inputlist)
    print("Average = ", f"{average:.2f}")


def find_min_max(inputlist):
    print("find_min_max")
    templist=sort_temperature(inputlist)
    print(f"MIN = {templist[0]}, and MAX = {templist[-1]}")
    return (templist[0], templist[-1])



def sort_temperature(inputlist):
    print("sort_temperature")
    templist = inputlist.copy()
    templist.sort()
    return templist


def calc_media_temperature():
    print("calc_median_temperature")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    inputlist = get_user_input()
    calc_average(inputlist)
    find_min_max(inputlist)



if __name__ == "__main__":
    main()

import sys


def main():
    transition = [[[0, 1], [0]], [[4], [2]], [[4], [3]], [[4], [4]]]
    x = input("enter the string: ")
    x = list(x)
    for index in range(len(x)):
        if x[index] == 'a':
            x[index] = '0'
        else:
            x[index] = '1'

    final = "3"
    start = 0
    i = 0
    trans(transition, x, final, start, i)
    print("rejected")


def trans(transition, x, final, state, i):
    for j in range(len(x)):
        for each in transition[state][int(x[j])]:
            if each < 4:
                state = each
                if j == len(x) - 1 and (str(state) in final):
                    print("accepted")
                    sys.exit()
                trans(transition, x[i + 1:], final, state, i)
        i = i + 1


main()

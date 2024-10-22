if __name__ == '__main__':
    arr = list()
    N = int(input())
    for i in range(N):
        cmd = input().split()
        for j in range(len(cmd)):
            if j > 0:
                cmd[j] = int(cmd[j])
        if cmd[0] == "insert":
            arr.insert(cmd[1], cmd[2])
        elif cmd[0] == "print":
            print(arr)
        elif cmd[0] == "remove":
            arr.remove(cmd[1])
        elif cmd[0] == "append":
            arr.append(cmd[1])
        elif cmd[0] == "sort":
            arr.sort()
        elif cmd[0] == "pop":
            arr.pop()
        elif cmd[0] == "reverse":
            arr.sort(reverse=True)
        print(arr)


def run():
    s = {}
    for _ in range(int(input())):
        num = input()
        for i in range(1, len(num) + 1):
            s[num[0:i]] = 1
    print(len(s))
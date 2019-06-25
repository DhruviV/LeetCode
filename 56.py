intervals=[[1,3],[2,6],[8,10],[15,18]]
start=0
intervals.sort(key=lambda interval: interval[0])
answer = []
for interval in intervals:
    print("first time",interval)
    if not answer:
        answer.append(interval)
        continue
    print("now my list",answer)
    print("now interval",interval)
    if interval[0] <= answer[-1][1]:
        print(interval[0])
        print(answer[-1][1])
        answer[-1][1] = max(answer[-1][1], interval[1])
        print(answer[-1][1],"chamges")

    else:
        answer.append(interval)

print(answer)
def ranks(a):
    l = len(a)
    rank = []
    b = list(a)
    b.sort(reverse=True)
    dic = {}

    for i in range(1, l + 1):
        rank.append(i)

    for j in range(l):
        if b[j] not in dic:
            dic[b[j]] = rank[j]
            
    rank = []

    for k in a:
        rank.append(dic.get(k))
    return rank

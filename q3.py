
from functools import partial

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

if __name__ == "__main__":
    data = [
        ("username1", "phone_number1", "email1"),
        ("usernameX", "phone_number1", "emailX"),
        ("usernameZ", "phone_numberZ", "email1Z"),
        ("usernameY", "phone_numberY", "emailX"),
    ]


    #find overlapped group in each item
    group = []
    for x in zip(*data):
        nodupX =  list(dict.fromkeys(x))
        dups_in_source = partial(list_duplicates_of, x)
        for y in nodupX:
            temp = dups_in_source(y)
            group.append(temp) if len(temp) > 1 else None
            print(y, dups_in_source(y))

    #print("group",group)

    #merge overlapped groups to final group
    dict = {}
    for i in range(len(group)):
        dict[i] = False
    res = []

    for i in range(len(group)) :
        if dict[i] != True:
            dict[i] = True
            for j in range(len(group)):
                if dict[j] != True and i!=j:
                    if bool(set(group[i]) & set(group[j])):
                        dict[j] = True
                        in_second_but_not_in_first = set(group[j]) - set(group[i])
                        result = group[i] + list(in_second_but_not_in_first)
                        res.append(result)
                    else:
                        res.append(result)

    # add single item
    for i in range(len(data)-1) :

        canFind = False
        for item in res:
            if i in item:
                canFind = True

        if canFind== False:
            res.append(i)


    print("final result ",res)

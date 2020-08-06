lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

# v1
rez = tuple(map(lambda idx: print(idx[0], round(idx[2] * idx[3] + 10, 2)) if idx[2] * idx[3] < 100 else print(idx[0],\
                                                            round(idx[2] * idx[3], 2)), lst))

# v2
lst_res = tuple(map(lambda idx: (idx[0], round(idx[2] * idx[3] + 10, 2)) if idx[2] * idx[3] < 100 else (idx[0],
                                                                                    round(idx[2] * idx[3], 2)), lst))
print(lst_res)
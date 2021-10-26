import random as r

r_list = []
while len(r_list) < 30:
    r_num = r.randint(1, 100)
    if ((r_num % 2) == 0) and not (r_num in r_list):
        r_list.append(r_num)

print(r_list)
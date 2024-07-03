with open('ecp_user_1.txt', 'r') as f:
    n = f.read()
f.close()


cherta = n.index("|")


polovinka1 = n[:cherta]
polovinka2 = n[cherta+1:]

plus_i_1 = polovinka1.index("+")
plus_i_2 = polovinka2.index("+")


a = polovinka1[:plus_i_1]
p = polovinka1[plus_i_1+1:]

q = polovinka2[:plus_i_2]
y = polovinka2[plus_i_2+1:]


print(f"{a} + {p} + {q} + {y}")



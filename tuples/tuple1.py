#Given an integer, , and  space-separated integers as input, create a tuple, , of those
#integers. Then compute and print the result of hash().



x=int(input())
a=list(map(int, input("").split()))
tpl=tuple(a)
print(hash(tpl))

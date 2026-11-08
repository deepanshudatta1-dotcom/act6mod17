n=int(input("enter any n(try 5, 10,or 50):"))
input("one loop-runs once per item.press enter to run")
for i in range(n):
    pass
print("n=",n,"steps=",n,"->0(n)linear time")
input("two nested loops-runs nxn time.press enter to run")
for i in range(n):
    for j in range(n):
        pass
print("n=",n,"steps=",n*n,"->0(n^2)quadratic time")
input("rule:count the loops.press enter")
print("0 loop -> 0(1) 1 loop -> 0(n) 2nested -> 0(n^2)")
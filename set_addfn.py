Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.
....................................................................



n=int(input())
s=set()
for i in range(n):
    inp=input()
    s.add(inp)
print(len(s))    

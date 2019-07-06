TASK

Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "" represents the values in between.
..............................................




if __name__ == '__main__':
    n = int(input())
for i in range(1,n+1):
    print(i,end='')

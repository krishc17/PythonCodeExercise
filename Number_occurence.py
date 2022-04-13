ls = [1, 2, 2, 3, 3, 4, 5, 5]

dic={}
#this is one of the file
def repeat(ls):
    r={x: ls.count(x) for x in ls}
    print(r)





repeat(ls)

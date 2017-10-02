def bsearch(lst,target):
    low,high=0,len(lst)-1
    while(low<=high):
        mid=(low+high)//2
        if(lst[mid]==target):
            return mid
            break
        if(target<lst[mid]):
            high=mid-1
        if(target>lst[mid]):
            low=mid+1
data_lst=[1,2,3,4,5,6]
target=int(input("请输入需查找的元素："))
position=bsearch(data_lst,target)
print("元素{0}的位置为：{1}".format(target,position))

list1=[1,2,3,4,5,4,3,2]
dup_item=set()
uniq_item=[]
for x in list1:
   if x not in dup_item:
       uniq_item.append(x)
       dup_item.add(x)
       print(dup_item)


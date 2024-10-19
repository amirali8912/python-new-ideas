L1="***********************"
L2="*                     *"
L3="*      WELCOME!       *"
your_list=[]
while 1==1:
    while 1==1:
        print(L1)
        print(L2)
        print(L3)
        print(L2)
        print(L1)
        print("1.see list")
        print("2.add to list")
        print("3.remvoe from list")
        print("4.clear list")
        n=int(input())
        if n == 1:
            print(your_list)
        elif n == 2:
            a=input("enter what you want to add:")
            your_list.append(a)
        elif n == 3:
            if your_list == []:
                print("theres nothing in your list")
            else:
                asd=len(your_list)
                for i in range(0,asd):
                    print (i,":",your_list[i])
                lk=int(input("select an thing from your list to remove:"))
                print(your_list.pop(lk),"has been removed!")
        elif n == 4:
            lkj=input("are you sure you want to clear your list?(yes or no)")
            if lkj == "yes" :
                your_list.clear()
                print("your list has been cleared!")
        if n != 1 and n != 2 and n!=3 and n!=4:
            print("please try again")
            break
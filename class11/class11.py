#複製List,避免原本的List被更動
L=["hello","world"]
L2=L.copy()#使用copy()複製List
print(L2)#['Hello','World']
L2[0]="phython"#修改複製後List的索引0資料
print(L)#['Hello','World']原本List不受影響
print(L2)#['phython','World']只有複製的List被改變
#這跟變數=賦值不同,一班情況下會開2個記憶體空間,
#在List的況下使用=會讓2個變數名稱指向同一個記憶體空間,
#這導致修改一個List會影響到另一個List
#所以需要複製List時,應改會使用copy()方法
#remove:移除List中指定的元素(只會移除第一個找到的)
L=["hello","world","phython"]
L.remove("world")#移除World
print(L)#['hello','phython']
#不給索引時,pop()會移除最後一個元素
L.pop()#移除最後一個元素
print(L)#['hello','world']
s=L.pop(1)#移除索引1的元素,並回傳該值
print(s)#world
print(L)#['hello']

shopping_list=[]

while True:
    #自動列出目前的購物清單
    print("購物清單:")
    print(shopping_list)#顯示幕前的購物清單
    print("功能選單:")
    print("1.新增東西")
    print("2.修改東西")
    print("3.刪除東西")
    print("4.離開程式")
    choice=input("請輸入您的選擇(1-4):")
    #新增create
    if choice=="1":
        print("新增選單:")
        print("a.加入尾端")
        print("b.加入指定位置")
        add_choice=input("請選擇方法(a/b):")
        if add_choice=="a":
            item=input("請輸入要新增的東西:")
            shopping_list.append(item)
            print(f"{item}已加入清單!")

        elif add_choice=="b":
            item=input("請輸入要新增到清單中的物品:")
            posstion=int(input("請輸入位置(o為第一個)位置:"))
            if 0<=posstion<=len(shopping_list):
                shopping_list.insert(posstion,item)
                
    #更新(update)
    elif choice=="b":
        print("修改選單:")
        index=int(input("請輸入要修改的物品編號:"))
        if 0<=index<=len(shopping_list):
            new_item=input("請輸入要新的物品:")
            shopping_list[index]=new_item
            print("物品已修改!")
        else:
            print("無效的物品編號!")
    #刪除(delete)
    elif choice=="3":
        print("刪除選單:")
        print("a.依名稱刪除")
        print("b.依位置刪除")
        delete_choice=input("請選擇方法(a/b):")
        if delete_choice=="a":
            item=input("請輸入要刪除的物品名稱:")
        shopping_list.remove(item)
        print(f"{item}已從清單中刪除!")
  
    elif delete_choice=="b":
        index  =int(input("請輸入要刪除的物品編號:"))
        if 0<=index<=len(shopping_list):
            removed=shopping_list.pop(index)
            print(f"{removed}已從清單中刪除!")
        else:
            print("無效的物品編號!")
    else:
            print("無效的刪除選項!")
#離開程式
elif choice=="4":  
print("再見")
break  
else:
print("請輸入1到4之間的數字")



            
            
            


        
            


            
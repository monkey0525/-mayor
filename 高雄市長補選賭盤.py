候選人=['','吳益政','陳其邁','李眉蓁']
while True :    
    import random
    A=int(random.randint(1,3))
    print('-------------------------------------------------------------')
    print('1號吳益政')
    print('2號陳其邁')
    print('3號李眉蓁')
    B=int(input('你覺得誰會當選 :'))
    if A==B :
        print('你猜對了，',B,'號',候選人[B],'當選了')
    elif B<1 or B>3:
        print('沒這個人')
    else:
        print(B,'號',候選人[B],'落選了，你猜錯了',A,'號',候選人[A],'當選了')
print()        
        

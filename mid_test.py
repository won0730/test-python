#두수를 공백 기준으로 입력 받아 곱하고 나눈 결과를 출력하는 프로그램

##n1,n2=input('두 정수를 입력하세요').split()
##n1=int(n1)
##n2=int(n2)
##
##gop=n1*n2
##na=n1/n2
##
##print('곱:{} 나눔:{}'.format(gop,na))





#문자열 슬라이싱
a='dream'
##print(a[0:2])
##print(a[0::3])
##print(a[:-1])
##print(a[2::-1])






#홀수 짝수 구분
##n=int(input('숫자입력'))
##if n%2==1:
##    print('홀수')
##elif n%2==0:
##    print('짝수')





#로그인
def login():
    myid=input('아이디를 입력하세요')
    mypw=input('비밀번호를 입력하세요')
    id_list=['상명대','융공대']

    if myid in id_list:
        if myid=='상명대' and mypw=='1234':
            print('{}님 로그인 되었습니다'.format(myid))
        elif myid=='융공대' and mypw=='4321':
            print('{}님 로그인 되었습니다'.format(myid))
        else:
            print('로그인에 실패하였습니다.')
    else:
        print('없는 아이디')
#login()     










#bmi측정 프로그램
def BMI():
    h=int(input('키를 입력하세요'))
    w=int(input('몸무게를 입력하세요'))

    bmi=w/((h/100)**2)

    if 0<bmi<20:
        print('재측정')
    elif 20<=bmi<25:
        print('정상')
    elif 25<=bmi<30:
        print('과체중')
    elif bmi>=30:
        print('비만')
    else:
        print('측정불가')

    print('키:{}cm 몸무게:{}kg BMI:{:.2f}'.format(h,w,bmi))
#BMI()







#숫자 합계1
def num_sum():
    while True:

        n=int(input('정수를 입력하세요'))
        if n==0:
            print('종료')
            break
            
        else:
            if n%2==1:
                odd_hap=0          
                for num in range(1,n+1,2):
                    odd_hap+=num
                print('홀수 합{}'.format(odd_hap))
                
            elif n%2==0:
                even_hap=0
                for num in range(2,n+1,2):
                    even_hap+=num
                print('짝수 합{}'.format(even_hap))

#num_sum()     




#주사위 합 게임
import random
def play_dice():
    user1=random.randint(1,6)
    user2=random.randint(1,6)
    user_hap=user1+user2
    print('사용자 주사위1:{} 주사위2:{} 합:{}'.format(user1,user2,user_hap))

    com1=random.randint(1,6)
    com2=random.randint(1,6)
    com_hap=com1+com2
    print('컴퓨터  주사위1:{} 주사위2:{} 합:{}'.format(com1,com2,com_hap))

    if user_hap==com_hap:
        print('무승부')
    elif user_hap>com_hap:
        print('사용자 우승')
    else:
        print('컴퓨터 우승')

    if user_hap==10:
        print('사용자 보너스')
    if com_hap==10:
        print('컴퓨터 보너스')
    else:
        print('보너스 없음')
#play_dice()











#주사위 프로그램1
import random
def dice():
    num,bounus = input("주사위 던지는 횟수, 보너스 번호 입력").split()
    print("던지는 횟수{}, 보너스번호:{}".format(num,bounus))
    sum=0
    bounus_count =0
    
    for i in range(1,int(num)+1,1):
        rand_dice_num = random.randint(1,6)
        sum= sum + rand_dice_num
        print("{}번째 랜덤주사위 눈{}".format(i,rand_dice_num))

        if rand_dice_num==int(bounus):
            print("보너스 당첨!!")
            bounus_count +=1

        

    print("눈의 합{}".format(sum))
    print("보너스 당첨횟수{}".format(bounus_count))
#dice_play()




#주사위 프로그램2
def dice_play2():
    user_bounus_num = int(input("보너스번호입력"))
    print("사용자 보너스번호:{}".format(user_bounus_num))

    com_bounus_num = random.randint(1,6)
    print("컴퓨터 랜덤 보너스번호:{}".format(com_bounus_num))

    if user_bounus_num==com_bounus_num:
        print("같음")
    
#dice_play2()






#구구단 프로그램
def gugudan():

    start_dan = int(input("시작단을입력"))
    end_dan = int(input("종료단을입력"))
    
    for dan in range(start_dan,end_dan+1,1):
        for num in range(1,10,1):
            print("{} x {} = {}".format(dan,num,dan*num))
    
#gugudan()





#구구단 프로그램2
def gugudan2():

    for i in range(2,10,1):
        print("=={}단==".format(i),end="\t\t")  #\t 는 탭을 나타냄
    print("")
      
    for num in range(1,10,1):
        for dan in range(2,10,1):
            print("{} x {} = {}".format(dan,num,dan*num),end="\t")
        print("")               #먼저 반복되는 for문이 안쪽

    
#gugudan2()







#가위바위보 프로그램
import random
rsp = ["가위","바위","보","종료"]

count=0
win=0
lose=0
same=0


def Game():
    print("게임시작!!")
    global count
    global win
    global lose
    global same

    while True:
        com = random.choice(rsp)  
        user = input("가위 바위 보입력(종료는 종료입력)")
 
        if user==rsp[0] or user==rsp[1] or user==rsp[2]:
            print("사용자:{}".format(user))
            print("컴퓨터:{}".format(com))
            count +=1
            
            if user==com:
                print("비김")
                same +=1
                
            elif user=="가위":
                if com=="바위":
                    print("사용자 패")
                    lose +=1
                    
                else:
                    print("사용자 승")
                    win +=1

            elif user=="바위":
                if com=="보":
                    print("사용자 패")
                    lose +=1
                else:
                    print("사용자 승")
                    win +=1

            elif user=="보":
                if com=="가위":
                    print("사용자 패")
                    lose +=1
                else:
                    print("사용자 승")
                    win +=1

        elif user==rsp[3]:
            print("종료합니다")
            print("{}전 {}승 {}패 {}무".format(count,win,lose,same))            
            break

        else:
            print("난 몰라-게임못함")
        
#Game()








import random
rsp = ["묵","찌","빠"]

count=0
win=0
lose=0
same=0

def rsp_input():
        com = random.choice(rsp)  
        user = input("묵 찌 빠입력(종료는 공백입력)")
 
        if user==rsp[0] or user==rsp[1] or user==rsp[2]:
            print("사용자:{}".format(user))
            print("컴퓨터:{}".format(com))


def Game2():
    print("게임시작!!")
    global count
    global win
    global lose
    global same

    while True:
        rsp_input()
            
            
        if user==com:
                print("다시")
                same +=1

        elif user=='':
            print("종료합니다")
            print("{}전 {}승 {}패 {}무".format(count,win,lose,same))            
            break

        elif user!=rsp[0] or user!=rsp[1] or user!=rsp[2]:
            print("난 몰라-게임못함")  

        else:
                
            if user=="묵":
                if com=="찌":
                    print("공격")
                    rsp_input()
                        if user==com:
                            print('사용자 승')
                elif com=="빠":
                    print("수비")
                    rsp_input():
                        if user==com:
                            print('컴퓨터 승')

            if user=="찌":
                if com=="빠":
                    print("공격")
                    rsp_input():
                        if user==com:
                            print('사용자 승')
                elif com=="묵":
                    print("수비")
                    rsp_input():
                        if user==com:
                            print('컴퓨터 승')
                        
            if user=="빠":
                if com=="묵":
                    print("공격")
                    rsp_input():
                        if user==com:
                            print('사용자 승')
                elif com=="찌":
                    print("수비")
                    rsp_input():
                        if user==com:
                            print('컴퓨터 승')
                

                 
                        
        
Game2()












    
    



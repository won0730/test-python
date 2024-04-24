#이름 나이 입력/출력
def age1():
    name=input('이름')
    birth=int(input('출생연도'))
    age=2024-birth
    print('이름:{} 나이:{}'.format(name, age))
#age1()


def age2(name, birth):
    age=2024-birth
    print('이름:{} 나이:{}'.format(name, age))

#name=input('이름')
#birth=int(input('출생연도'))
#age2(name, birth)


def age3(name,birth):
    age=2024-birth
    return name, age

##name=input('이름')
##birth=int(input('출생연도'))
##name, age=age3(name,birth)
##print('이름:{} 나이:{}'.format(name, age))






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

                


    

def num_quiz():

    w_num = 5

    while True:
        num = int(input("숫자입력"))
        print("입력숫자:{}".format(num))
        
        if num<w_num:
            print("성공!!")
            break
        else:
            print("실패!!")
            
#num_quiz()


import random
def num_quiz2():
    rand_num = random.randint(1,30)
    #print("랜덤숫자:{}".format(rand_num))
    count=0

    while True:
         
        user_num = int(input("숫자입력"))
        print("입력숫자:{}".format(user_num))

        if user_num < rand_num:
            print("↑")
            count += 1
        elif user_num > rand_num:
            print("↓")
            count += 1
            
        else:
            count += 1
            print("정답")
            print("{}회 시도했습니다".format(count))
            break
    
#num_quiz2()

def dice_play():

    num, bounus = input("주사위 던지는 횟수, 보너스 번호 입력").split()

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

def dice_play2():
    user_bounus_num = int(input("보너스번호입력"))
    print("사용자 보너스번호:{}".format(user_bounus_num))

    com_bounus_num = random.randint(1,6)
    print("컴퓨터 랜덤 보너스번호:{}".format(com_bounus_num))

    if user_bounus_num==com_bounus_num:
        print("같음")
    
#dice_play2()

def gugudan():

    start_dan = int(input("시작단을입력"))
    end_dan = int(input("종료단을입력"))
    
    for dan in range(start_dan,end_dan+1,1):
        for num in range(1,10,1):
            print("{} x {} = {}".format(dan,num,dan*num))
    
#gugudan()
            
def gugudan2():

    for i in range(2,10,1):
        print("=={}단==".format(i),end="\t\t")
    print("")
      
    for num in range(1,10,1):
        for dan in range(2,10,1):
            print("{} x {} = {}".format(dan,num,dan*num),end="\t")
        print("")

    
#gugudan2()

def rsp():
    rsp = input("가위 바위 보 중 하나를 입력하세요")

    if rsp=="가위" or rsp=="바위" or rsp=="보":
        print("{}내셨습니다".format(rsp))
    else:
        print("가위 바위 보게임입니다 가위 바위 보 중 하나를 입력하세요 - 종료합니다")

rsp()

        
        
        


'''

가위바위보 프로그램
1) 사용자로부터 “가위”, ”바위“, “보“ 를 입력 받고 컴퓨터가 무작위로 “가위“, ”바위“, ”보” 를 출력하여 승패를 판단하고 결과를 화면에 출력하기
2) 한번 게임이 마치면 다시 사용자에게 게임을 계속할 것인지 물어보고 y를 입력하면 가위바위보 게임이 다시 시작되도록 하기
3) 사용자가 n을 입력하면 가위바위보 게임이 종료됨

묵찌빠 프로그램
1)사용자에게 ‘묵’, ‘찌’, ‘빠’ 문자열을 입력 받고 입력된 문자열이 각 ‘묵’, ‘찌’, ‘빠’ 인 경우에만 각 해당 문자열을 출력하기
2)사용자에게 ‘묵’, ‘찌’, ‘빠’ 문자열을 반복입력 받기
3)다른 문자열을 입력된 경우 “재입력” 메시지를 출력하기
4)사용자가 ‘묵’, ‘찌’, ‘빠’ 각 문자열을 입력 하지 않고 엔터를 누르면 프로그램은 “전 승 패“, ＂실습시간”과 종료 메시지를 출력하고 종료됨
'''



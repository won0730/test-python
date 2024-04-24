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
        
Game()

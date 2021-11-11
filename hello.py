coffe = 10
while True:
    money = int(input("돈을 넣어 주세요"))
    if money == 300:
        print("커피를 줍니다")
        coffe = coffe - 1
    elif money < 300:
        print("금액이 부족합니다")
        print("남은 커피는 %d개 입니다" % coffe)
    else:
        coffe = coffe - 1
        print("거스름돈 %d원과 커피가 나옵니다" % (money-300))
        print("남은 커피는 %d개 입니다 " % coffe)
    if coffe == 0:
        print("커피가 없습니다")
        break
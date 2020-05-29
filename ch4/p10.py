MAXNUM =4
MAXHEiGHT =130

more = True
cnt = 0
while more:
    height = float(input("키는 ? "))
    if height < MAXHEiGHT:
        cnt += 1
        print('들어가세요.', '%d명' %cnt)
    else:
        print('커서 못 들어갑니다.')
        if cnt == MAXNUM:
            more = false
        else:
            print('%d명 모두 찼습니다. 다음 번에 이용하세요.' % cnt)

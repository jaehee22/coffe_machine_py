coffe = list()
coffe_price = list()
coffe_stock = list()
coffe_sales = list()

def coffe_set():
    coffe.append("")
    coffe.append("아메리카노")
    coffe.append("카페라떼")
    coffe.append("바닐라라떼")
    coffe.append("콜드브루")
    coffe.append("허니자몽티")

    coffe_price.append("")
    coffe_price.append(3500)
    coffe_price.append(3800)
    coffe_price.append(4000)
    coffe_price.append(3600)
    coffe_price.append(4500)

    for i in range(0,6):
        coffe_stock.append(10)
        coffe_sales.append(0)

def manu_list():
    print("==================")
    print("     메뉴")
    print("==================")
    print("1. 커피 주문하기")
    print("2. 커피 매출 확인")
    print("3. 커피 입고 하기")
    print("4. 종료하기")
    print("==================")

def coffe_list():
    i=1
    for i in range(1,len(coffe)):
        print("{0}. {1}  가격:{2}   재고:{3}".format(i, coffe[i], coffe_price[i], coffe_stock[i]))

def coffe_order():
    choice = 0

    while(choice != 9):
        coffe_list()
        print("구입하실 커피의 번호를 선택해주세요. (뒤로가려면 9)")
        choice = int(input())
        if (choice == 9):
            break
        elif (coffe[choice] == ""):
            print("해당되는 커피는 없습니다\n")
            continue
        print("몇개를 주문하시겠습니까?")
        coffe_n = int(input())
        while (coffe_stock[choice] < coffe_n):
            print("죄송합니다. 커피의 수량이 부족합니다. 수량을 조정해주세요")
            coffe_n = int(input())
        coffe_stock[choice] -= coffe_n
        coffe_sales[choice] += coffe_price[choice] * coffe_n
        print("더 주문 하시겠습니까?")


def coffe_tosales():
    total_sale = 0
    i = 1

    for i in range(1,len(coffe)):
        print("{0}        매출:{1}".format(coffe[i], coffe_sales[i]))
        total_sale += coffe_sales[i]

    print("총 매출 : {0}".format(total_sale))

def coffe_plus():
    choice = 0

    while (choice != 9):
        coffe_list()
        print("입고하실 커피의 번호를 선택해 주세요. (뒤로가시려면 9")
        choice = int(input())
        if (choice == 9):
            break
        elif (coffe[choice] == ""):
            print("해당되는 커피는 없습니다")
            continue
        print("몇개를 입고하시겠습니까?")
        coffe_n = int(input())
        coffe_stock[choice] += coffe_n
        print("더 입고 하시겠습니까?")

n = 0;
coffe_set()

while (n != 4):
    manu_list()
    n = int(input())

    if (n==1):
        coffe_order()
    elif (n==2):
        coffe_tosales()
    elif (n==3):
        coffe_plus()
    else:
        break

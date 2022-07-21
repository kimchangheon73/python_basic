# 모듈 : 특정 기능이 모여져 있는 부품파일


# 일반 가격
def price(people):
    print("{}명 가격은 {}원 입니다".format(people, people*10000))
    
# 조조 할인 가격
def price_morning(people):
    print("{}명 조조가격은 {}원 입니다".format(people, people*6000))
    
# 군인 할인 가격 
def price_solider(people):
    print("{}명 군인가격은 {}원 입니다".format(people, people*4000))



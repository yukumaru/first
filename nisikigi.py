import random

def judge(x,y):
    kekka = (x - y - 3) % 3
    if kekka == 0 :
        j = "引き分け"
    elif kekka == 1 :
        j ="敗北"
    else :
        j ="勝利"
    print(j)

hand = ["グー","チョキ","パー"]

x = input ("何を出す？\n0:グー,1:チョキ,2:パー\n\n")

x = int(x) 

y = random.randint(0,2)

print("\nこちらの手:{}\n".format(hand[x]))
print("\n相手の手:{}\n".format(hand[y]))

judge(x,y)
# PYTHON_BMI

# BMI関数
# 引数は身長(cm),体重(kg),日本基準適用の是非の順に指定
def bmi(h, w = False, j = False):
    
    # 標準体重を計算
    s_weight = round(22*(h/100)**2, 2)

    # BMI(body mass index)を計算
    x = round(w/((h/100)**2), 2)
    
    # WHO の基準
    if x < 16:
        kekka_a = "痩せすぎ"
        
    elif 16 <= x < 17:
        kekka_a = "痩せ"
        
    elif 17 <= x < 18.5:
        kekka_a = "痩せ気味"
        
    elif 18.5 <= x < 25:
        kekka_a = "普通体重"
        
    elif 25 <= x < 30:
        kekka_a = "前肥満"
        
    elif 30 <= x < 35:
        kekka_a = "肥満（1度）"
        
    elif 35 <= x < 40:
        kekka_a = "肥満（2度）"
        
    else:
        kekka_a = "肥満（3度）"
    
    # 日本の基準
    if x < 18.5:
        kekka_b = "低体重"
        
    elif 18.5 <= x < 25:
        kekka_b = "普通体重"
        
    elif 25 <= x < 30:
        kekka_b = "肥満（１度）"
        
    elif 30 <= x < 35:     
        kekka_b = "肥満（2度）"
        
    elif 35 <= x < 40:
        kekka_b = "肥満（3度）"
        
    elif x > 40:
        kekka_b = "肥満"
    
    # 体重を省略すると標準体重のみを返す
    if w == False:
        return s_weight
    
    # 第3引数をTrueにすると日本基準で返す
    elif j == True:
        return x, s_weight, kekka_b
    
    # 第3引数がTrue以外の値であればWHO基準で返す
    else:
        return x, s_weight, kekka_a

hitotume =  bmi(170, 75)

hutatume = bmi(170, 75, True)

sankome = bmi(183)

print(hitotume)
print(hutatume)
print(sankome)
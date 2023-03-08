import random
import math

def calc_distance(x1,y1,x2,y2) :
 diff_x = x1-x2
 diff_y = y1-y2
 return math.sqrt(diff_x**2 + diff_y**2)

zirai_x = random.randrange(0 , 10)
zirai_y = random.randrange(0 , 10)

zibun_x = random.randrange(0 , 10)
zibun_y = random.randrange(0 , 10)

while(zirai_x != zibun_x ) or (zirai_y != zibun_y) :

 distance = calc_distance(zibun_x,zibun_y,zirai_x,zirai_y)
 print("地雷までの道のり",distance)
 yuku = input("w:上に行く s:下に行く d:右に行く a:左に行く q:左斜め上へ行く e:右斜め上へ行く z:左斜め下へ行く c:右斜め下へ行く")
 if yuku == "w" :
  zibun_y = zibun_y - 1
 elif yuku == "s":
  zibun_y = zibun_y + 1
 elif yuku == "d":
  zibun_x = zibun_x - 1
 elif yuku == "a":
  zibun_x = zibun_x + 1
 elif yuku == "q":
  zibun_y = (zibun_y - 1)+(zibun_x + 1)
 elif yuku == "e":
  zibun_y = (zibun_y - 1)+(zibun_x - 1)
 elif yuku == "z":
  zibun_x = (zibun_y - 1)+(zibun_x + 1)
 elif yuku == "c":
  zibun_x = (zibun_y + 1)+(zibun_x + 1)
print("地雷の破壊に成功") 
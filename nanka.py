import random
import math

def calc_distance(x1,y1,x2,y2) :
 diff_x = x1-x2
 diff_y = y1-y2
 return math.sqrt(diff_x**2 + diff_y**2)

ringo_x = random.randrange(0 , 5)
ringo_y = random.randrange(0 , 5)

zibun_x = random.randrange(0 , 5)
zibun_y = random.randrange(0 , 5)

while(ringo_x != zibun_x ) or (ringo_y != zibun_y) :

 distance = calc_distance(zibun_x,zibun_y,ringo_x,ringo_y)
 print("りんごまでの道のり",distance)
 yuku = input("w:上に行く s:下に行く d:右に行く a:左に行く")
 if yuku == "w" :
  zibun_y = zibun_y - 1
 elif yuku == "s":
  zibun_y = zibun_y + 1
 elif yuku == "d":
  zibun_x = zibun_x - 1
 elif yuku == "a":
  zibun_x = zibun_x + 1
print("りんごの破壊に成功") 
import myMath   

'''
if ---> module/myMath.py
import module.myMath
'''

print("My first module started")
myMath.add(5,6)                             # module.myMath.add()
myMath.sub(18,12)
print("My first module ended")

from myMath import add
add(5,6)

from myMath import add as addition
addition(4,3)

from myMath import add,mul   #for specific importing

from myMath import *   # for all importing






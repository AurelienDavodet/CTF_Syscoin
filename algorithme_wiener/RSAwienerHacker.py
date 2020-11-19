import ContinuedFractions, Arithmetic  
import time  
import sys  
import base64  
import binascii  
import math  
import fractions  
import struct  

sys.setrecursionlimit(100000)  
 # modulus from the RSA public key  
n= 1114821929811691218941109797355910744022063989678890599979059904366325358372268800898454667124757250406254026246704798467176084638682616811800202929755972279349685004112244690905836763410136448373398498091264499041762848437419868904523572389608173111511578039547669154973227807551488240194684088722472922147879 
 # exponent from the RSA public key  
e= 874050971728547171118342551503765991378632841119712878340624357530752020641561805183832271343740302336642320259427038339567601234607281264133581914286147229528825743177071518222743784731334729633154436576772217232240052368991124698347868153936109536432714015894898756203742022788368619329985430499475175966823 
 
def hack_RSA(e,n):  
   print ("Performing Wiener's attack...")  
   time.sleep(1)  
   frac = ContinuedFractions.rational_to_contfrac(e, n)  
   convergents = ContinuedFractions.convergents_from_contfrac(frac)  
   for (k,d) in convergents:  
     #check if d is actually the key  
     if k!=0 and (e*d-1)%k == 0:  
       phi = (e*d-1)//k  
       s = n - phi + 1  
       # check if the equation x^2 - s*x + n = 0  
       # has integer roots  
       discr = s*s - 4*n  
       if(discr>=0):  
         t = Arithmetic.is_perfect_square(discr)  
         if t!=-1 and (s+t)%2==0:  
           return d  

hacked_d = hack_RSA(e, n)  
print ("d=" + str(hacked_d))
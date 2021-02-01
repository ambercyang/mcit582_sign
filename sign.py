#!/usr/bin/env python
# coding: utf-8

# In[73]:


from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

import random
import hashlib
import numpy as np
import string


# In[2]:


#The extended GCD algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Calculate a modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1 and g != -1:
        #print( "gcd = %d"%g )
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# In[ ]:


def order(self, P):
    Q = P
    orderP = 1
    #Add P to Q repeatedly until obtaining the identity (point at infinity).
    while not Q.is_infinite():
        Q = self.add(P,Q)
        orderP += 1
    return orderP


# In[86]:


def sign(m):
    #generate public key & private key
    myCurve = curve.secp256k1
    private_key = keys.gen_private_key(myCurve)
    public_key = keys.get_public_key(private_key, myCurve)
     
    #print("this is the point:", public_key )
    #print("this is th public key:", public_key)
    #print("this is th private key:", private_key)
    
    #generate signature
    k = random. randint(1,100)
    n = myCurve.q
    d = private_key
    print("this is n:",n)
    
    [x1,y1] = np.dot(k , [public_key.x,public_key.y])
    r = pow(x1,1,n)
    z = int.from_bytes((hashlib.sha256(m.encode('utf-8')).digest()),'big')
    s = (modinv(k, n)*pow(z+r*d,1,n))%n
    
    #r = 0
    #s = 0
    return( public_key, [r,s] )


# In[87]:


m = "Hello World"
sign(m)


# In[ ]:





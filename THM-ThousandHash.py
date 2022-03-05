#! /usr/bin/python3

import hashlib

#thm = '61v3_m3_k3y_pl3453'
var = input("Please Enter String >> ")
n = str(var)

var = var.encode('utf-8')

cycle = int(input("How many iterations?\nEnter a number: "))

for i in range(cycle):

    output = hashlib.sha512(var)  # SHA512
    #print(output.hexdigest() + ' SHA512')

    output = output.hexdigest().encode("utf-8") # Encodes SHA512 as UTF-8 for input for hashlib
    output = hashlib.md5(output)  # MD5
    #print(output.hexdigest() + ' MD5')

    output = output.hexdigest().encode("utf-8")  # Encodes MD5 as UTF-8 for input for hashlib
    output = hashlib.sha256(output)  # SHA256
    #print(output.hexdigest() + ' SHA256')

    output = output.hexdigest().encode("utf-8")  # Encodes SHA256 as UTF-8 for input for hashlib
    output = hashlib.sha1(output)  # SHA1
    #print(output.hexdigest() + ' SHA1')

    output = output.hexdigest().encode("utf-8")  # Encodes SHA1 as UTF-8 for input for hashlib
    output = hashlib.sha224(output)  # SHA224
    #print(output.hexdigest() + ' SHA224')

    #print('\n---------------------\n')
    #print(i)

    var = output.hexdigest().encode('utf-8') # Sets var as SHA224 digest so it can be fed back in loop
    finalHash = output.hexdigest()

print('\n[+]== Hashing Complete! ==[+]\n')
print('Given String: ' + n)
print("Number of Cycles: " + str(cycle) + '\n')
print("SHA224: " + finalHash)

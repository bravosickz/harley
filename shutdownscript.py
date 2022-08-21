import time 
starz = time.time()
def counter():
    b = 900
    while b < 100000000:
        b += 1
    return b
counter()
end = time.time()
print("time = ",end-starz)




#Write a program to find the sum of 
# all even numbers from 1 to 100 using a while loop

count = 1
result = 0
while count <= 100:
    
    if count % 2 == 0:
        result +=count
    
    count = count + 1    

print(result)
        
        
    
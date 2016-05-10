"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# ref = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
#        12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
#        20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',
#        1000:'thousand','+':'and'}

ref = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,
       50:5,60:5,70:7,80:6,90:6,100:7,1000:8,'+':3}

sum = 0
for i in range(1,1001):
    # 10 - 19
    if (i//10)%10 == 1:
        sum += ref[i%100]
    # 00 - 09 and 20 - 99
    else:
        sum += ref[10*((i//10)%10)] + ref[i%10]
    # 100-900
    if (i//100)%10:
        sum += ref[i//100]
        sum += ref[100] + ref['+'] if i%100 else ref[100]
    # 1000
    if i == 1000:
        sum += ref[1] + ref[1000]

print(sum)
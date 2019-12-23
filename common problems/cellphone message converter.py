#Python program to convert given message to input for classic button phones
# ----- |----- |----- |
#   1   |   2  |   3  |
#  .,   |  abc |  def |
# ----- |----- |----- |
#   4   |   5  |   6  |
#  ghi  |  jkl |  mno |
# ----- |----- |----- |
#   7   |   8  |   9  |
#  pqrs |  tuv | wxyz |
# ----- |----- |----- |



numbers=[[' '],[".",","],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
message=str(input("Enter Message to be converted:\n"))
if(message=="0"):
    print("exited program")
else:
    phoneMessage=""
    for i in message:                                       #going letter by letter
        for j in range(0,len(numbers)):                     #check phase
            count=0
            for k in numbers[j]:
                count+=1
                if(i==k):
                    phoneMessage+=(str(j)*count)
    print(phoneMessage)                                     #Display message

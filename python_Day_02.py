###Task 1: WAP to create a function which returns the sum of all the element provided to it as an arguement. The arguement list will be dynamic.#####
print ("task 1 started")
def listsum(total, *args):
    for i in range(0, len(args)):
        total = total + args[i]
    print(total)
total = 0
number = input("Enter the number with space")
number = number.split()
for i  in range(len(number)):
    number[i] = float(number[i])

listsum(total, *number)

###TASK DAY 02 ####
def myFun(**kwargs):
    ret =0 
    count =0 
    maximum =0 
    string=""
    failed = ""
    for k , j in kwargs.items():
        count +=1
        ret = ret + j
        if j > maximum:
            maximum =j
            string = k
        if j < 33: 
         failed = k
    print("teh average marks is ",ret/count)
    print ("the failed marks is 33")
    print ("the failed students are", failed)
    print("%s = %s" %(string, maximum))
    #print(stri)
myFun(rahul =80, aman =95, palak=45, anmol =60 , hi= 12) 

#####https://github.com/LetusDevops/LearnPython/tree/main/day2 task3 ###
a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"] 
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"] 
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }
    
]  
# Iterating over keys
for i  in a_dict:
    print(i['name'] , i['power'], i ['powerlevel'], i['frieds'][0]['name'], i['frieds'][0]['friend_points'], i['frieds'][0]['enemies'][0], i['frieds'][0]['name'])







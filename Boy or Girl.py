
def check(string):
    setted=set(string)
    if len(setted)%2==0:
       return "CHAT WITH HER!"
    return "IGNORE HIM!"
# take input 
string=input()
print(check(string))


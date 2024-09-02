def eventOdd(x:int)->int:
    if(x % 2 == 0):
        result = "even"
        return result
    else:
        result = "odd"
        return result
    
def callEventOdd():
    print("Please enter number:", end="")
    x = int(input())
    ans = eventOdd(x)
    print(f"Number = {x} is {ans}")
# welcome to ac's nighttime brain method
# it's called: chuck it all in functions
# I was doing a friend's test problem the one here is easier HAHAHA

def checksum(stuff: int):
    # converts the number into a list of integers
    stuff = [int(x) for x in str(stuff)]
    final = []
    # first we reverse the list
    stuff.reverse() # alt. stuff = stuff[:-1]
    ###### step 1 ######
    # using the enumerate, we'll determine what will be *2
    # the original I did was separated funnily enough
    final = [num*2 if i%2 == 1 else num for i, num in enumerate(stuff)]
    # now we need to, add the digits of the products?
    # I'm going to assume 16 => 1+6 etc.
    total = 0
    for num in final:
        
        if num > 9:
            # since the highest number possible is 18 (9*2), I will only be accounting for two-digit numbers
            # this splits the number in half
            total += num//10 + num%10
        else:
            ####### step 2 ######
            total += num
    
    ###### step 3 ######
    # finally, we check if our value ends with 0
    # divs by 10 MUST end with 0
    return "PASS" if str(total).endswith('0') else "FAIL"

# chuck everything into the range because, kattis, kattis
for _ in range(int(input())):
    card = int(input())
    print(checksum(card))
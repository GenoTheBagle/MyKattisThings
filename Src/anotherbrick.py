h, w, n = list(map(int, input().split()))
bl = list(map(int, input().split())) # n number of bricks, each int in list is length
# all bricks have height 1

# maybe start with vars? like we're gonna build the wall ourselves
ch = 0
cw = 0

for b in bl:
    cw += b # add that brick's width
    
    if cw > w: break
    
    if cw == w:
        cw = 0
        ch += 1 # since all bricks are height 1, just add 1 :)
    
    if ch == h:
        print("YES")
        exit(0) # I wonder if this works here..? I guess we'll find out!

print("NO")
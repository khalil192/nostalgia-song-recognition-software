txt = "apple#banana#cherry#orange"

# setting the max parameter to 1, will return a list with 2 elements!
x = txt.rsplit("#", 1)

print(x)


import random

min_no_matches_to_verify = 90
min_no_to_check = 10
min_no_correct = 5
max_freq_diff = 10
max_time_diff = 5

max_no_of_linear_misses = 10

def min(a,b):
    if a<b:
        return a
    else:
        return b   
def max(a,b):
    if a>b:
        return a
    else:
        return b  



def calc_matches(x,y,i,j):
    allowed_penality =2
    m = len(x)
    n = len(y)
    matches = 1
    penality  = 0
    if(i==0 or j==0):
        return 0,matches
    while(i>0 and j>0):
        if(x[i] == y[j]):
            matches+=1
        else :
            penality+=1
            if penality>allowed_penality:
                break
        i-=1
        j-=1        
    return penality,matches    



#it is meaningful to start with a match rather than a penalty
#look for the first match and then start for the check of matches..

def checkForMatch(list1 , list2 , count1 , count2):
    numX = len(list1) -1
    numY = len(list2)
    i = 0
    j = 0
    allowed_penalty = 10
    yRange = min(5, numY)
    xRange = len(list1) -1
    maxMatches = 0
    for yStart in range(0,yRange):
        for xStart in range(xRange):
            i = xStart
            j = yStart
            xChar = list1[:]
            yChar = list2[:]
            xCount = count1[:]
            yCount = count2[:]
            if(abs(ord(xChar[i]) - ord(yChar[j])) >1):
                continue
            matches = 0
            penalty = 0
            # print('started with ' , xChar[i])
            while(i < numX and j < numY):
                # print(xChar[i] ,xCount[i] ,  yChar[j],yCount[j])
                if(abs(ord(xChar[i]) - ord(yChar[j])) <=1):
                    matches += min(xCount[i] ,yCount[j])
                else :
                    penalty += min(xCount[i] ,yCount[j])
                mini = min(xCount[i] , yCount[j])
                xCount[i] -= mini
                yCount[j] -= mini
                # print('afetr',xChar[i] ,xCount[i] ,  yChar[j],yCount[j])
                
                if(penalty > allowed_penalty):
                    break
                if(matches >= min_no_matches_to_verify):
                    print(matches)
                    return True
                if(xCount[i]  < yCount[j]):
                    i += 1
                elif(yCount[j] < xCount[i]):
                    j += 1
                else :
                    i+=1
                    j+=1
            maxMatches = max(maxMatches , matches)
            # print(maxMatches, penalty)
            if(matches >= min_no_matches_to_verify):
                print(matches)
                return True
    print(maxMatches)
    return False , maxMatches


import random

min_no_matches_to_verify = 70
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


def max_sub_list_with_penality(x,y):
    m = len(x)
    n = len(y)
    matrix = [[0 for k in range(n+1)] for l in range(m+1)] 
    max_matches = 0
    for i in range(m + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                # print("this is done")
                matrix[i][j] = 0
            elif (x[i-1] == y[j-1]):
                # print('no thisa is ') 
                penality,matches= calc_matches(x,y,i-1,j-1)
                matrix[i][j] = matches 
                max_matches = max(max_matches, matrix[i][j]) 
                if(max_matches >min_no_matches_to_verify):
                    # print('matches = ',max_matches)
                    return True
            else: 
                matrix[i][j] = 0    
    # for i in matrix:
    #     print(i)
    # print('matches = ',max_matches)
    if(max_matches < min_no_matches_to_verify):
        return False
    # return max_matches
















  
# def LCSubStr(X, Y, m, n): 
#     LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
#     result = 0 
#     for i in range(m + 1): 
#         for j in range(n + 1): 
#             if (i == 0 or j == 0): 
#                 LCSuff[i][j] = 0
#             elif (X[i-1] == Y[j-1]): 
#                 LCSuff[i][j] = LCSuff[i-1][j-1] + 1
#                 result = max(result, LCSuff[i][j]) 
#             else: 
#                 LCSuff[i][j] = 0
#     for i in LCSuff:
#         print(i)    
#     return result 













# print(LCSubStr("this","this",4,4))

# def max_list(x,y):
#     ans_global = 0
#     m = len(x)
#     n = len(y)
#     for i in range(m):
#         ans_local =0
#         misses_local = 0
#         for j in range(n):
#             if(misses_local > max_no_of_linear_misses):
#                 break
#             if x[j] == y[j]:
#                 ans_local+=1
#             else:
#                 misses_local+=1    
#         if ans_local > ans_global:
#             ans_global = ans_local

#     return ans_global

# ans  = max_list("nothisisert","thisisshit")
# print(ans)






# def LCSubStr(X, Y, m, n): 
      
#     LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
#     result = 0 
#     for i in range(m + 1): 
#         for j in range(n + 1): 
#             if (i == 0 or j == 0): 
#                 LCSuff[i][j] = 0
#             elif (X[i-1] == Y[j-1]): 
#                 LCSuff[i][j] = LCSuff[i-1][j-1] + 1
#                 result = max(result, LCSuff[i][j]) 
#             else: 
#                 LCSuff[i][j] = 0
#     return result 


# x = 'nothisisshitert'
# y = 'thisisshit'
# print(LCSubStr(x,y,len(x),len(y)))




# def max_random_list(x_time,x_freq,y_time,y_freq):
#     ans=0
#     m = len(x_time) #as x_freq and x_time have same size..
#     n = len(y_time) 
#     for num1 in range(min_no_to_check) :
#         i = random.randrange(0,m)   
#         while(x_freq[i])
#         correct_yet = 0
#         for num2 in range(min_no_matches_to_verify):
#             j = random.randrange(0,min(abs(n-i),abs(m-i))
#             if(x[i])


"""def diagonally_past(matrix,m,n,row,col):
    j = col-1
    i = row-1
    # last_i = row-1
    # last_j = col-1
    penality = 0
    matches  = 0
    print('for ',row,col)
    if(i==0 or j==0):
        return 0,1
    while i>0 and j>0:
        print(i,j)
        print('matches :',matches,'penality  = ',penality)
        if(matrix[i][j] ==0 ):
             penality+=1
        if penality >allowed_penality :
            print("returned here ",i,j,matches,penality)
            return penality,matches
        # last_i,last_j 
        else:
            # last_i = i
            # last_j = col
            print('done this')
            matches+=1
        i-=1
        j-=1
    return penality ,matches
    # last_i,last_j
"""
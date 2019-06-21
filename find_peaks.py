from PIL import Image
import numpy  as np
import matplotlib.pyplot as plt
from specgram import max_freqency_limit,max_height,max_width
from max_list import calc_matches,max_sub_list_with_penality
# a = numpy.array([1, 2])

# a = numpy.append(a, [50, 60], axis = 0)
# a = numpy.append(a, [3, 4], axis = 0)

# print(a)
# a.resize(int(a.size/2),2)
# print(a)

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

log2 = 0.30102999566
e =2.71828
def conv_to_freq(m):
    f = 700*(e**(m/1127) - 1)
    return f


def hash(filepath):
    try:
        filepath,filename = filepath.split('/') 
    except:
        filepath = ""
        filename = filepath
    im = Image.open(filepath+'/'+filename)
    rgb_im = im.convert('RGB')
    width, height = im.size
    x_skip = 100
    y_skip = 100
    il = int(width/x_skip)
    jl = int(height/y_skip)
    red_limit = 240
    ans = np.array([0,0])
    ans_x = np.array([])
    ans_y = np.array([])
    # print(width,height)
    # print(il,jl)
    for i in range(0,il):
        for j in range(0,jl):
            i_present = x_skip *i
            j_present = y_skip *j
            i_last = min(width-1,(x_skip)*(i+1))
            j_last = min(height-1,(y_skip)*(j+1))   
            max_yet = red_limit
            max_i = -1
            max_j = -1
            # print(i_present,j_present," - ",i_last,j_last)
            diff_x = i_last - i_present
            diff_y = j_last - j_present
            for x_c in range(diff_x):
                for y_c in range(diff_y):
                    r,g,b = rgb_im.getpixel((x_c+i_present,y_c+j_present))
                    if(r>max_yet):
                        max_yet = r
                        max_i = x_c+i_present
                        max_j = y_c+j_present
            if max_i !=-1 and max_j !=-1:
                ans = np.append(ans,[max_i/width,max_j/height],axis=0)
                ans_x = np.append(ans_x,[max_i/width],axis=0)
                ans_y = np.append(ans_y,[conv_to_freq(max_j)],axis=0)
    ans.resize(int(ans.size/2),2)
    return ans,ans_x,ans_y



# def find_freq(m,):
#     #we get normal height in the form of mel frequency 
#     #convert that height to normal mel frequency then convert it into normal frequency
#     #


def find_peaks(filepath):
    file_rem_path = ""
    filename = ""
    try:
        file_rem_path,filename = filepath.split('/')
    except:
        filename = filepath
    im = Image.open(filepath)
    rgb_im = im.convert('RGB')
    width, height = im.size
    ans_x = np.array([])
    ans_y = np.array([])    
    for i in range(width):
        max_yet = -1
        max_j = -1
        for j in range(height):
            r,g,b = rgb_im.getpixel((i,j))
            if(r>max_yet):
                max_yet = r
                max_j = j
        if(max_j!=-1):
            ans_x = np.append(ans_x,[i],axis=0)
            ans_y = np.append(ans_y,[chr(35 +int(conv_to_freq(max_j)/10))],axis=0)
    return ans_x,ans_y


# ans_x,ans_y = find_peaks('a/a0.png')
# print(ans_y)
# bns_x,bns_y = find_peaks('v/v20.png')
# # print(LCSubStr(ans_y,bns_y,len(ans_y),len(bns_y)))
# print(max_sub_list_with_penality(ans_y,bns_y))
# fig,ax = plt.subplots(1)   
# plt.scatter(ans_x,ans_y)
# fig.savefig('t/ft2.png', bbox_inches='tight')
# # plt.show()



  




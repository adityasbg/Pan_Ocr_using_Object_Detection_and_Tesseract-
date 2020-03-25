import cv2
import matplotlib.pyplot  as plt
import re

def draw_img(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def returnNameAndconfidence(line):
    split_text =re.split(':',line)
    return {'className':split_text[0] , 'confidence':split_text[1][:-2]}

def checkIfLessThanZeroThanMakeZero(val):
    if(val<0):
        val=0
    return val
def returnCoordinates(line):
    coords={}
    splitCoods =re.split("  " ,line)

    try:
        coords['left_x']=checkIfLessThanZeroThanMakeZero(int(splitCoods[1]))
        coords['top_y']=checkIfLessThanZeroThanMakeZero(int(splitCoods[3]))
        coords['width']=checkIfLessThanZeroThanMakeZero(int(splitCoods[5]))
        coords['height']=checkIfLessThanZeroThanMakeZero(int(splitCoods[7][:-2]))
    except TypeError:
        print("Coordinates number coversion error ")
    return coords



def read_result():
    seachKey =['FatherName' ,'pan_no' ,'dob','name']
    result_list=[]
    with open('result.txt') as text:
        for line in text.readlines():
            for key in seachKey:
                if(re.match(key ,line)):
                    result_dict={}
                    split_line =re.split('\(',line)
                    nameAndConfindenceDict =returnNameAndconfidence(split_line[0])
                    coordinatesDict =returnCoordinates(split_line[1])
                    result_dict.update(nameAndConfindenceDict)
                    result_dict.update(coordinatesDict)
                    result_list.append(result_dict)


    return  result_list

                    

def  crop_image(img):
    result_list=read_result()
    result_list=result_list
    for ele in result_list:
        print(ele)
        className =ele['className']
        temp_crop  = img[ele['top_y']:ele['top_y']+ele['height'] ,ele['left_x'] :ele['left_x']+ele['width']]
        cv2.imwrite('./Image/'+className+'.jpg' ,temp_crop)




if __name__ =='__main__':

    img = cv2.imread('a2.jpg')
    img =cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
    crop_image(img)



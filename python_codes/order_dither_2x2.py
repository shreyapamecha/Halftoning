import cv2
import random
import numpy as np
from fidelity_metrics import fidelity_17110150
import matplotlib.pyplot as plt

path1='C:\Shreya\SEM-5\DIP\Assignment3\campus.png';
save1='C:\Shreya\SEM-5\DIP\Assignment3\g3_bayer_2x2.png';

f=cv2.imread(path1,0); #reading the input image (grayscale)
(row,column)=(len(f),len(f[0])) #deciphering rows and columns
print(row,column)
#print(f)

Bayer_2x2=np.array([[96,159],  #96,159,223,37
                    [223,32]]);

g3=np.zeros((row,column));

#checking the threshold values and accordingly assigning values to the output image
#--------------------------------------
for k in range(0,2):
    for i in range(k,row,2):
        for j in range(0,column,2):
            if (f[i][j]<Bayer_2x2[k][0]):
                g3[i][j]=0;
            else:
                g3[i][j]=255;


        for j in range(1,column,2):
            if (f[i][j]<Bayer_2x2[k][1]):
                g3[i][j]=0;
            else:
                g3[i][j]=255;

#--------------------------------------

#Uncomment this to calculate fidelity metrics
#-----------------------------------------------
#Calculating Fidelity Metrics
#(c1,c2,c3,c4,c5,c6)=fidelity_17110150(f,g3)
#print('alpha1_g3',c1,' alpha2_g3',c2,' alpha3_g3',c3,' alpha4_g3',c4,' alpha5_g3',c5,' alpha6_g3',c6)
#----------------------------------------------

#couldn't find the equivalent of 'truesize' used in MATLAB, therefore have used cv2 library

cv2.imwrite(save1,g3)

fig=plt.figure()
plt.title('Please see the saved image')
plt.imshow(g3,cmap='gray')
plt.show()

    

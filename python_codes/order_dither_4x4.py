import cv2
import random
import numpy as np
from fidelity_metrics import fidelity_17110150
import matplotlib.pyplot as plt

path1='C:\Shreya\SEM-5\DIP\Assignment3\campus.png';
save1='C:\Shreya\SEM-5\DIP\Assignment3\g4_bayer_4x4.png';

f=cv2.imread(path1,0); #reading the input image (grayscale)
(row,column)=(len(f),len(f[0])) #deciphering rows and columns
print(row,column)
#print(f)

#Calculate using (255*((I(i,j)+0.5)/N^2))
###8,135,40,167,199,72,231,104,56,183,24,151,247,119,215,88##

Bayer_4x4=np.array([[8,135,40,167],
                    [199,72,231,104],
                    [56,183,24,151],
                    [247,119,215,88]]);

g4=np.zeros((row,column));

#checking the threshold values and accordingly assigning values to the output image
#------------------------------------------
for k in range(0,4):
    for i in range(k,row,4):
        for j in range(0,column,4):
            if (f[i][j]<Bayer_4x4[k][0]):
                g4[i][j]=0;
            else:
                g4[i][j]=255;

        for j in range(1,column,4):
            if (f[i][j]<Bayer_4x4[k][1]):
                g4[i][j]=0;
            else:
                g4[i][j]=255;

        for j in range(2,column,4):
            if (f[i][j]<Bayer_4x4[k][2]):
                g4[i][j]=0;
            else:
                g4[i][j]=255;

        for j in range(3,column,4):
            if (f[i][j]<Bayer_4x4[k][3]):
                g4[i][j]=0;
            else:
                g4[i][j]=255;

        
#--------------------------------------------
#Uncomment this to calculate fidelity metrics
#-----------------------------------------------
#Calculating Fidelity Metrics
#(d1,d2,d3,d4,d5,d6)=fidelity_17110150(f,g4)
#print('alpha1_g4',d1,'alpha2_g4',d2,'alpha3_g4',d3,'alpha4_g4',d4,'alpha5_g4',d5,'alpha6_g4',d6)
#-----------------------------------------------

#couldn't find the equivalent of 'truesize' used in MATLAB, therefore have used cv2 library
cv2.imwrite(save1,g4)

#The image shown using matplotlib may not be visually appealing! You can see the saved iamges
fig=plt.figure()
plt.title('Please see the saved image')
plt.imshow(g4,cmap='gray')
plt.show()

    

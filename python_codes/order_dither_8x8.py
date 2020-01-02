import cv2
import random
import numpy as np
from fidelity_metrics import fidelity_17110150
import matplotlib.pyplot as plt

path1='C:\Shreya\SEM-5\DIP\Assignment3\campus.png';
save1='C:\Shreya\SEM-5\DIP\Assignment3\g5_bayer_8x8.png';

f=cv2.imread(path1,0); #reading the input image (grayscale)
(row,column)=(len(f),len(f[0])) #deciphering rows and columns
print(row,column)
#print(f)

#Calculate using (255*((I(i,j)+0.5)/N^2))
###2,191,50,239,12,203,60,251,129,66,177,114,141,78,189,125,34,225,18,209,46,237,30,221###
###161,98,145,82,173,110,157,94,10,201,58,249,6,197,54,245,137,74,185,121,133,70,181,117###

#Bayer threshold 8x8 matrix
Bayer_8x8=np.array([[2,191,50,239,12,203,60,251],
                    [129,66,177,113,141,78,189,125],
                    [34,225,18,209,46,237,30,221],
                    [161,98,145,82,173,110,157,94],
                    [10,201,58,249,6,197,54,245],
                    [137,74,185,121,133,70,181,117],
                    [42,233,26,217,38,229,22,213],
                    [169,106,153,90,165,102,149,86]]);

g5=np.zeros((row,column));

#checking the threshold values and accordingly assigning values to the output image
#--------------------------------------------
for k in range(0,8):
    for i in range(k,row,8):
        for j in range(0,column,8):
            if (f[i][j]<Bayer_8x8[k][0]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;

        for j in range(1,column,8):
            if (f[i][j]<Bayer_8x8[k][1]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;

        for j in range(2,column,8):
            if (f[i][j]<Bayer_8x8[k][2]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;

        for j in range(3,column,8):
            if (f[i][j]<Bayer_8x8[k][3]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;

        for j in range(4,column,8):
            if (f[i][j]<Bayer_8x8[k][4]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;

        for j in range(5,column,8):
            if (f[i][j]<Bayer_8x8[k][5]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;
            
        for j in range(6,column,8):
            if (f[i][j]<Bayer_8x8[k][6]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;

        for j in range(7,column,8):
            if (f[i][j]<Bayer_8x8[k][7]):
                g5[i][j]=0;
            else:
                g5[i][j]=255;
            
#---------------------------------------------    

#Uncomment this to calculate fidelity metrics
#-----------------------------------------------
#Calculating Fidelity Metrics
#(e1,e2,e3,e4,e5,e6)=fidelity_17110150(f,g5)
#print('alpha1_g5',e1,'alpha2_g5',e2,'alpha3_g5',e3,'alpha4_g5',e4,'alpha5_g5',e5,'alpha6_g5',e6)
#-----------------------------------------------

#couldn't find the equivalent of 'truesize' used in MATLAB, therefore have used cv2 library            
cv2.imwrite(save1,g5)

#The image shown using matplotlib may not be visually appealing! You can see the saved iamges
fig=plt.figure()
plt.title('Please see the saved image')
plt.imshow(g5,cmap='gray')
plt.show()

    

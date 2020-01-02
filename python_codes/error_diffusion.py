import numpy as np
import cv2
from fidelity_metrics import fidelity_17110150
import matplotlib.pyplot as plt

import time

start_time=time.time();

path1='C:\Shreya\SEM-5\DIP\Assignment3\campus.png';
save1='C:\Shreya\SEM-5\DIP\Assignment3\g6_err_diff.png';

f=cv2.imread(path1,0); #reading the input image (grayscale)

(row,column)=(len(f),len(f[0])); #deciphering rows and columns
f_copy=np.zeros((row+1,column+2));
f_copy[0:row,1:column+1]=f;


g6=np.zeros((row,column));

#err_diff_filter=np.array([[0,0,7/16],
#                          [3/16,5/16,1/16]]);

#row_err=len(err_diff_filter);
#column_err=len(err_diff_filter);

#count=0;
#Threshold taken=127
for i in range(row):
    #if count>4:
        #break
    for j in range(column):
        if ((f_copy[i][j+1])<127):
            g6[i][j]=0;
        else:
            g6[i][j]=255;

        error=(g6[i][j]-f_copy[i][j+1]);

        #print('value',f_copy[0][2])
        #print('f_copy',f_copy)
        #print('out_img',out_img)
        #print('error',error)

        f_copy[i][j+2]=(f_copy[i][j+2])-(error*(7/16));
        f_copy[i+1][j]=(f_copy[i+1][j])-(error*(3/16));
        f_copy[i+1][j+1]=(f_copy[i+1][j+1])-(error*(5/16));
        f_copy[i+1][j+2]=(f_copy[i+1][j+2])-(error*(1/16));

        #count+=1;

        #if (count>4):
            #break

    
#print(out_img,len(out_img),len(out_img[0]))

#--------------------------------------------
#Uncomment this to calculate fidelity metrics
#-----------------------------------------------
#Calculating Fidelity Metrics
#(f1,f2,f3,f4,f5,f6)=fidelity_17110150(f,g6)
#print('alpha1_g6',f1,'alpha2_g6',f2,'alpha3_g6',f3,'alpha4_g6',f4,'alpha5_g6',f5,'alpha6_g6',f6)
#-----------------------------------------------

print('%s seconds'%(time.time()-start_time))

#couldn't find the equivalent of 'truesize' used in MATLAB, therefore have used cv2 library
cv2.imwrite(save1,g6)

#The image shown using matplotlib may not be visually appealing! You can see the saved iamges
fig=plt.figure()
plt.title('Please see the saved image')
plt.imshow(g6,cmap='gray')
plt.show()

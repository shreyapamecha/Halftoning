import cv2
import random
import numpy as np
from fidelity_metrics import fidelity_17110150
import matplotlib.pyplot as plt

path1='C:\Shreya\SEM-5\DIP\Assignment3\campus.png';
#i am unable to store the image in '.tiff' image file format, therefore, used '.png'
save1='C:\Shreya\SEM-5\DIP\Assignment3\g1_threshold.png'; 
save2='C:\Shreya\SEM-5\DIP\Assignment3\g2_binary.png';

f=cv2.imread(path1,0); #reading the input image (grayscale)
(row,column)=(len(f),len(f[0])) #deciphering rows and columns
#print(row,column)
#print(f)


f1=np.zeros((row,column)); #the image obtained after adding uniform additive noise to the input image
g1=np.zeros((row,column)); #the output image obtained after thresholding of f(input image)
g2=np.zeros((row,column)); #the output image obtained aftering thresholding of f1

for i in range(row):
    for j in range(column):
        #Thresholding
        if (f[i][j]<127):
            g1[i][j]=0;
        else:
            g1[i][j]=255;

        #Random Noise Binarization
        #noise within the range[-128,128] | hence blurring giving an impression of several grey levels
        #we have noticed that if we decrese this range of random noise, we could get visually appealing pictures 
        noise=random.randrange(-128,128,1);
        f1[i][j]=f[i][j]+noise
        if (f1[i][j]<127):
            g2[i][j]=0;
        else:
            g2[i][j]=255;

print('Thresholding & Random Noise Binarization Done')

#Uncomment this to calculate fidelity metrics
#-----------------------------------------------
#Calculating Fidelity Metrics
#(a1,a2,a3,a4,a5,a6)=fidelity_17110150(f,g1)
#print('alpha1_g1',a1,'alpha2_g1',a2,'alpha3_g1',a3,'alpha4_g1',a4,'alpha5_g1',a5,'alpha6_g1',a6)
#(b1,b2,b3,b4,b5,b6)=fidelity_17110150(f,g2)
#print('alpha1_g2',b1,'alpha2_g2',b2,'alpha3_g2',b3,'alpha4_g2',b4,'alpha5_g2',b5,'alpha6_g2',b6)
#-----------------------------------------------

#couldn't find the equivalent of 'truesize' used in MATLAB, therefore have used cv2 library

#cv2.imwrite(save1,g1)
#cv2.imwrite(save2,g2)

#The image shown using matplotlib may not be visually appealing! You can see the saved iamges
fig=plt.figure()
plt.title('Please see the saved images')
plt.imshow(g2,cmap='gray')
plt.show()


##Uncomment this to see thresholded output and Random noise binarization output
#fig=plt.figure()
#fig.add_subplot(1,2,1)
#plt.imshow(g1,cmap='gray')
#fig.add_subplot(1,2,2)
#plt.imshow(g2,cmap='gray')
#plt.show()

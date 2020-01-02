###Note: Calculating Fidelity metrics take a lot of time!!!#####

import cv2
import random
import numpy as np
import matplotlib.pyplot as plt

#Image Fidelity Metrics
def fidelity_17110150(f,g):
    alpha1=0;
    alpha2=0;
    alpha3=0;
    alpha4=0;
    alpha5=0;
    alpha6=0;

    (row,column)=(len(f),len(f[0]));

    # Gaussian Low Pass Filter (7x7)
    gaussian_LPF=np.array([[1/1115,4/1115,7/1115,10/1115,7/1115,4/1115,1/1115],
                           [4/1115,12/1115,26/1115,33/1115,26/1115,12/1115,4/1115],
                           [7/1115,26/1115,55/1115,71/1115,55/1115,26/1115,7/1115],
                           [10/1115,33/1115,71/1115,91/1115,71/1115,33/1115,10/1115],
                           [7/1115,26/1115,55/1115,71/1115,55/1115,26/1115,7/1115],
                           [4/1115,12/1115,26/1115,33/1115,26/1115,12/1115,4/1115],
                           [1/1115,4/1115,7/1115,10/1115,7/1115,4/1115,1/1115]])

    #inverting the filter matrix for convolution
    row_w=len(gaussian_LPF);
    column_w=len(gaussian_LPF[0]);
    w=np.zeros((row_w,column_w)); 
    for i in range(1,row_w):
        for j in range(1,column_w):
            s=abs(row_w-1-i);
            t=abs(column_w-1-j);
            w[i][j]=gaussian_LPF[s][t];

    #print('1st done')
    
    f1=np.zeros((row,column));
    g1=np.zeros((row,column));
    f1_new=np.zeros((row,column));
    g1_new=np.zeros((row,column));
    f2_pad=np.zeros((row+6,column+6)); #padding with zeroes so as to obatin the output image of the same image as that of 'f'
    g2_pad=np.zeros((row+6,column+6));
    f3=np.zeros((row,column));
    g3=np.zeros((row,column));
    f3_new=np.zeros((row,column));
    g3_new=np.zeros((row,column));

    #print('2nd done')

    for i in range(row):
        for j in range(column):
            #print(f[i][j],i,j,(f[i][j]/255)**2.2)
            f1[i][j]=round(255*((f[i][j]/255)**2.2));
            g1[i][j]=round(255*((g[i][j]/255)**2.2));
            f1_new[i][j]=round(255*((f[i][j]/255)**(1/2.2)));
            g1_new[i][j]=round(255*((g[i][j]/255)**(1/2.2)));

    f2_pad[3:row+3,3:column+3]=f1;
    g2_pad[3:row+3,3:column+3]=g1;

    f2=np.zeros((row,column));
    g2=np.zeros((row,column));
    #print('3rd done')

    #CONVOLUTION (this step takes a lot of time to process. The larger the size of the matrix, more will be its computational time.)
    for i in range(row):
        for j in range(column):
            for k in range(row_w):
                    for l in range(column_w):
                        f2[i][j]+=w[k][l]*f2_pad[i+k][j+l];
                        g2[i][j]+=w[k][l]*g2_pad[i+k][j+l];

            f2[i][j]=round(f2[i][j]);
            g2[i][j]=round(g2[i][j]);

    #print('4th done')

    for i in range(row):
        for j in range(column):
            f3[i][j]=int((255*((f2[i][j]/255)**2.2)));
            g3[i][j]=int((255*((g2[i][j]/255)**2.2)));
            f3_new[i][j]=int((255*((f2[i][j]/255)**(1/2.2))));
            g3_new[i][j]=int((255*((g2[i][j]/255)**(1/2.2))));

    #print('Calculating 6 fidelity metrics')
    
    for i in range(row):
        for j in range(column):
            alpha1=alpha1+(f[i][j]-g[i][j]);
            alpha2=alpha2+abs(f[i][j]-g[i][j]);
            
            alpha3=alpha3+abs(f1[i][j]-g1[i][j]);            
            alpha4=alpha4+abs(f1_new[i][j]-g1_new[i][j]);

            alpha5=alpha5+abs(f3[i][j]-g3[i][j]);
            alpha6=alpha6+abs(f3_new[i][j]-g3_new[i][j]);

    alpha1=alpha1/(row*column);
    alpha2=alpha2/(row*column);
    alpha3=alpha3/(row*column);
    alpha4=alpha4/(row*column);
    alpha5=alpha5/(row*column);
    alpha6=alpha6/(row*column);
                    
    return(alpha1,alpha2,alpha3,alpha4,alpha5,alpha6)

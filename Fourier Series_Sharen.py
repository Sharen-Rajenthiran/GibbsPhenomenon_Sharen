import cmath
import math
import numpy as np
import matplotlib.pyplot as plt


#Assignment Python for SSCP4333
#Sharen Rajenthiran
#Gibbs Phenomenon

#For this assignment, I have used two methods which are the manual method and the loop method.



t_Start = 0   #my starting time, let it be seconds
t_Stop = 3    #my end time
t_Step = 0.01  #my time steps
N = int((t_Stop-t_Start)/t_Step + 1)   #number of points from start to finish
t = np.linspace(t_Start,t_Stop,N)     #my t array in x-axis
x = np.zeros(N)                       #my empty x array for y-axis, let them empty (0) first


# How I want my square wave to be: amplitude = +0.5 and -0.5 for period T = 1
# This will be our reference signal when we try to fit our other signal from Fourier Series


for i in range(len(t)):
    if 0<t[i]<0.5:
        x[i] = 0.5
    elif 0.5<=t[i]<1:
        x[i] = -0.5
    elif 1.0<=t[i]<1.5:
        x[i] = 0.5
    elif 1.5<=t[i]<2.0:
        x[i] = -0.5
    elif 2.0<=t[i]<2.5:
        x[i] = 0.5
    elif 2.5<=t[i]<3.0:
        x[i] = -0.5


# Start with 1st method; the manual method. I have manually set the signal for n = 1 until 10. I did this to see the pattern.

# Start with empty array (0) for y

y = np.zeros(N)
y_1 = np.zeros(N)
y_2 = np.zeros(N)
y_3 = np.zeros(N)
y_4= np.zeros(N)
y_5 = np.zeros(N)
y_6 = np.zeros(N)
y_7 = np.zeros(N)
y_8 = np.zeros(N)
y_9 = np.zeros(N)
y_10 = np.zeros(N)
y_11 = np.zeros(N)
y_12 = np.zeros(N)
y_13 = np.zeros(N)
y_14 = np.zeros(N)
y_15 = np.zeros(N)
y_16 = np.zeros(N)
y_17 = np.zeros(N)
y_18 = np.zeros(N)
y_19 = np.zeros(N)
y_20 = np.zeros(N)



pi_number = np.pi      # just a constant for pi, simplicity sake


constant = (2/pi_number)    # this is the constant that we get from calculating bn, since the square wave is periodic and odd, a0 and an is 0.

# This process is tedious but I did this just to see the pattern first. Later on I will use the second method which is using loop and the python sum function.

y_1 = constant*(np.sin((4*pi_number*1*t) - (2*pi_number*t)))/(2*1 - 1)   # n = 1
y_2 = constant*(np.sin((4*pi_number*2*t) - (2*pi_number*t)))/(2*2 - 1)   # n = 2
y_3 = constant*(np.sin((4*pi_number*3*t) - (2*pi_number*t)))/(2*3 - 1)   # n = 3 and so on
y_4 = constant*(np.sin((4*pi_number*4*t) - (2*pi_number*t)))/(2*4 - 1)
y_5 = constant*(np.sin((4*pi_number*5*t) - (2*pi_number*t)))/(2*5 - 1)
y_6 = constant*(np.sin((4*pi_number*6*t) - (2*pi_number*t)))/(2*6 - 1)
y_7 = constant*(np.sin((4*pi_number*7*t) - (2*pi_number*t)))/(2*7 - 1)
y_8 = constant*(np.sin((4*pi_number*8*t) - (2*pi_number*t)))/(2*8 - 1)
y_9 = constant*(np.sin((4*pi_number*9*t) - (2*pi_number*t)))/(2*9 - 1)
y_10 = constant*(np.sin((4*pi_number*10*t) - (2*pi_number*t)))/(2*10 - 1)




Sum_1 = y_1       # sum y for n = 1
Sum_2 = y_1+y_2   # sum y for n = 2
Sum_3 = y_1+y_2+y_3   # sum y for n = 3
Sum_10 = y_1+y_2+y_3+y_4+y_5+y_6+y_7+y_8+y_9+y_10    # sum y for n = 10


# I have plotted Sum_1, Sum_2, Sum_3 and Sum_10 and have color coded them to see how the signal changes for increasing n.

# ______________________________________________________________________________________________________________________

# Now I use the second method; the loop and sum function method.
n = 25  # I want my n to stop at n = 25

# This is the single line code (line 105) that simplifies all the mess above. Instead of doing it manually, we can do it this way also.
# Have to remember that Python doesn't stop at n = 25. It will stop at n = 24 when using Python range.

y = constant*(sum(((np.sin((4*pi_number*i*t) - (2*pi_number*t)))/(2*i- 1)) for i in range(1,n)))

# Finally plot the y for n = 24. As we can see, for n = 24, the y fits almost perfectly with x with errors at the discontinuties. We can increase n = 50 also by changing the n value.
# This saves us a lot of time.


plt.plot(t,Sum_1,t,Sum_2,t,Sum_10,t,y,t,x)
plt.grid()
plt.xlabel("Time,s")
plt.ylabel("Amplitude")
plt.title("Gibbs Phenomenon")
plt.legend(["n=1 not using loop", "n =2 not using loop", "n=10 not using loop", "n=25 using loop", "Original square wave"], loc = "lower left")
plt.show()





X= [0,3,6,7,9,13,17,19,23,27,30,34]
Y= [6,8,10,13,15,20,22,25,29,32,33,37]

sum_x=0
for i in range(0, len(X)):
    sum_x+=X[i]

sum_x2=0
for i in range(0, len(X)):
    sum_x2+=(X[i]*X[i])

sum_y=0
for i in range(0, len(Y)):
    sum_y+=Y[i]

n=len(X)

sum_xy=0
for i in range(0, n):
    sum_xy+=X[i]*Y[i]

B_y= (n*sum_xy - sum_x*sum_y)/ (n*sum_x2 - sum_x*sum_x)

Y_slash= sum_y/n
a=Y_slash-B_y*(sum_x/n)

def predict(x):
   return a+B_y*x


print(predict(27))

f1 <-expression(3*x^4 - 4*x^3) 
f1 
dif<-D(f1, 'x'); 
dif 
polyroot(c(0,-12,12)) 
x<- -1 
eval(12*x^3 - 12*x^2) 
X<-1/2 
eval(12*x^3 - 12*x^2) 
x<-2 
eval(12*x^3 - 12*x^2) 
fun<-function(x) {3*x^4 - 4*x^3} 
curve(fun,xlim=c(-3,3),ylim=c(-10,20))



f1 <-expression(4*x^4  - 4*x^3) 
f1 
dif<-D(f1, 'x'); 
dif 
polyroot(c(0,-12,16)) 
x<- -1 
eval(16*x^3 - 12*x^2) 
X<-1/2 
eval(16*x^3 - 12*x^2) 
x<-1 
eval(16*x^3 - 12*x^2) 
fun<-function(x) {4*x^4 - 4*x^3} 
curve(fun,xlim=c(-3,4),ylim=c(-10,50)) 


f1 <-expression(4*x^4) 
f1 
dif<-D(f1, 'x'); 
dif 
polyroot(c(0,16)) 
x<- -1 
eval(16*x^3 - 12*x^2) 
x<-1 
eval(16*x^3 - 12*x^2) 
fun<-function(x) {4*x^4} 
curve(fun,xlim=c(-2,4),ylim=c(-10,50)) 


f1<-expression(2*x^3 - 12*x^2 + 4*x-27); 
f1 
dif<-D(f1, 'x'); 
dif 
diff<-D(dif,'x') 
diff 
polyroot(c(0,-24,12)) 
x<- -5 
eval(12*x - 24) 
X<-6 
eval(12*x - 24) 
x<-2 
eval(12*x - 24) 
fun<-function(x) {2*x^3 - 12*x^2 + 4*x-27} 
curve(fun,xlim=c(-10,10),ylim=c(-80,80))



f1<-expression(tan(x)) 
f1 
dif<-D(f1, 'x'); 
dif 
diff<-D(dif, 'x'); 
diff 
x<- -1 
eval(-tan((x))) 
x<-1/2 
eval(-tan((x))) 
x<-1 
eval(-tan((x))) 
fun<-function(x) {tan((x))} 
curve(fun,xlim=c(50,-50),ylim=c(50,-50))


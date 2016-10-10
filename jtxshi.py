
#coding:utf-8
import struct 
import binascii
import numpy as np
import matplotlib.pyplot as plt

##### 
uartfile = open('addata0.txt','r')
channl1 = open ('channl1.txt','w')
i = 1
while i<=16416:
  data = uartfile.read(4)
  #data = struct.unpack('!f',data5)[0]
  if(i>=0 and i%8==1):
  	channl1.write(data)	
  	#print i 
  	#print binascii.b2a_hex(data)
  i+=1
uartfile.close()
channl1.close()
x = list(np.arange(0,2052,1))
y = []
channl1 =open('channl1.txt','r')
while 1:
	data1 = channl1.read(4)
	if not data1:
		break
	data2 = struct.unpack('!f',data1)[0]
	y.append(data2)
#print len(y)
#print len(x)

channl1.close()
plt.figure(figsize=(10,5))
plt.plot(x,y)
plt.title(u'测试程序')
plt.xlabel(u'时间')
plt.ylabel(u'幅值')
plt.grid(True)
plt.show()

#data = np.loadtxt('channl1.txt')
#print data 

#channl1 = open ('channl1.txt','r')
#y = 0
#while 1:
#	data1 = channl1.read(4)
#	if not data1:
#		break
#	data2 = struct.unpack('!f',data1)[0]
#	print data2
#	y+=1
#	print y
#	plt.plot(data2,y)

#channl1.close


##figure show code #############
#x = [1,2,3,4,5,6,7,8] #np.linspace(0,0.04,1024)
#y = []
#for n in x:
#	y.append(-(i*i)+i+3)
#
#
#plt.figure(figsize=(10,5))
#plt.plot(x,y)
#plt.title(u'测试程序')
#plt.xlabel(u'x轴')
#plt.ylabel(u'y轴')
#plt.grid(True)
#plt.show()
#print uartfile.read()
#for line in uartfile:
#	process(line)
#uartfile.close()

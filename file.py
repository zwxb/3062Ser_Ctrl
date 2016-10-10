
#coding:utf-8
import struct 
import binascii
import numpy as np
import matplotlib.pyplot as plt

##### 
uartfile = open('addata0.txt','rb')
channl1 = open ('channl1.txt','wb')
i = 1
while i<=16416:
  data = uartfile.read(4)
  #print i
  #print binascii.b2a_hex(data)
  if(i>=32 and i%16==1): 
  	channl1.write(data)
  i+=1
uartfile.close()
channl1.close()
x = list(np.arange(0,1024,1))
y = []
channl1 =open('channl1.txt','rb')
while 1:
  data1 = channl1.read(4)
  if not data1:
    break
 #print binascii.b2a_hex(data1)#---讲ascii码转为16进制数据 
  data2 = struct.unpack('!f',data1)[0]
  y.append(data2)
print len(y)
print len(x)
#print y
channl1.close()
plt.figure(figsize=(10,5))
plt.plot(x,y)
plt.ylim(-150,150)
plt.title(u'测试程序')
plt.xlabel(u'时间')
plt.ylabel(u'幅值')
plt.grid(True)
plt.show()




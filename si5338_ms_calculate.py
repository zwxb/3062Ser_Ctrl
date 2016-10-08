#coding:utf-8
#si5338 Msx和Msn的寄存器计算部分
#author:liushaopeng
#2016/9/3 

import math
import si5338_base_calculate

#----------------------------------------------------------------------------#
#-----fsou_and_fin需要注意该列表中fsout的值不能为zero ---------------------------#
#----------------------------------------------------------------------------#
fsout_and_fin = [7987859.6,5987859.6,1,1,10000000]

def Msx_and_Msn(finout):
	fvco0 = si5338_base_calculate.Fvco(finout[0])
	fvco1 = si5338_base_calculate.Fvco(finout[1])
	fvco2 = si5338_base_calculate.Fvco(finout[2])
	fvco3 = si5338_base_calculate.Fvco(finout[3])
#----------------------------------------------------------------------------#
#---------------------MSn和MSx的a/b/c计算-------------------------------------#
#----------------------------------------------------------------------------#	
	Ms0_abc = si5338_base_calculate.MSx_abc(fvco0)
	Ms1_abc = si5338_base_calculate.MSx_abc(fvco1)
	Ms2_abc = si5338_base_calculate.MSx_abc(fvco2)
	Ms3_abc = si5338_base_calculate.MSx_abc(fvco3)
	Msn_abc = si5338_base_calculate.MSn_abc(finout[0],fvco0)
#----------------------------------------------------------------------------#
#---------------------MSn和MSx的寄存器计算-------------------------------------#
#----------------------------------------------------------------------------#	
	Ms0_P123 = si5338_base_calculate.Ms_P123(Ms0_abc)
	Ms1_P123 = si5338_base_calculate.Ms_P123(Ms1_abc)
	Ms2_P123 = si5338_base_calculate.Ms_P123(Ms2_abc)
	Ms3_P123 = si5338_base_calculate.Ms_P123(Ms3_abc)
	Msn_P123 = si5338_base_calculate.Ms_P123(Msn_abc)

   	return [Ms0_P123,Ms1_P123,Ms2_P123,Ms3_P123,Msn_P123] [0][1][0]
print Msx_and_Msn(fsout_and_fin)

#coding:utf-8
#author:liushaopeng
#2016/8/20
import math

#----------------------------------------------------------------------------#
#---------------------第2部分 寄存器配置---------------------------------------#
#----------------------------------------------------------------------------#

#-----------------------------------------------------------#
#---------------------参考时钟的选择--------------------------#
#-----------------------------------------------------------#
#-----REG28［1:0］ 选择外部晶振频率----------------------------#
REG28_XTAL_FREQ_8Mto11M 	= 0   #--外部晶振8M<XTAL<=11M
REG28_XTAL_FREQ_11Mto19M	= 1   #--外部晶振11M<XTAL<=19M
REG28_XTAL_FREQ_19Mto26M	= 2   #--外部晶振19M<XTAL<=26M
REG28_XTAL_FREQ_26Mto30M    = 3	  #--外部晶振26M<XTAL<=30M
#-----REG28［4:2］& REG29［4:3］选择P1输入端口IN1 IN2 IN3
REG28_P1DIV_IN_IN12_DIFF = 0<<2  #reg28选择IN1 IN2 差分输入
REG28_P1DIV_IN_IN3_SING  = 2<<2  #reg28选择IN3 单端输入
REG28_P1DIV_IN_IN12_XTAL = 5<<2  #reg28选择IN1 IN2 外部晶振输入

REG29_P1DIV_IN_IN12_DIFF = 0<<3  #reg29选择IN1 IN2 差分输入
REG29_P1DIV_IN_IN3_SING  = 2<<3  #reg29选择IN3 单端输入
REG29_P1DIV_IN_IN12_XTAL = 1<<3  #reg29选择IN1 IN2 外部晶振输入
#-----REG29[7:5] 选择进入PFD的参考时钟 如图12页 图6
REG29_PFD_IN_P1DIV_IN    = 0<<5  #选择进入PFD的参考时钟的方式 p1参考时钟
REG29_PFD_IN_P2DIV_IN    = 1<<5  # p2的反馈时钟
REG29_PFD_IN_P1DIV_OUT   = 2<<5
REG29_PFD_IN_P2DIV_OUT   = 3<<5
REG29_PFD_IN_XOCLK       = 4<<5
REG29_PFD_IN_NOCLK 		 = 5<<5	

REG29_P1DIV_DIV1         = 0  
REG29_P1DIV_DIV2         = 1
REG29_P1DIV_DIV4         = 2
REG29_P1DIV_DIV8		 = 3
REG29_P1DIV_DIV16		 = 4
REG29_P1DIV_DIV32		 = 5

#-----REG30[7:5] 选择进入PFD的反馈时钟 如图12页 图6-------------#
REG30_PFD_IN_P1DIV_IN    = 0<<5  
REG30_PFD_IN_P2DIV_IN    = 1<<5  
REG30_PFD_IN_P1DIV_OUT   = 2<<5
REG30_PFD_IN_P2DIV_OUT   = 3<<5
REG30_PFD_IN_XOCLK       = 4<<5
REG30_PFD_IN_NOCLK 		 = 5<<5	

REG30_P1DIV_DIV1         = 0  
REG30_P1DIV_DIV2         = 1
REG30_P1DIV_DIV4         = 2
REG30_P1DIV_DIV8		 = 3
REG30_P1DIV_DIV16		 = 4
REG30_P1DIV_DIV32		 = 5




#-----------------------------------------------------------#
#---------------------反馈时钟的选择--------------------------#
#-----------------------------------------------------------#
#需要30 和 28 寄存器同时设置，详见si5338-RM手册14页
REG30_P2DIV_IN_IN56_DIFF = 0<<3  #选择IN5 IN6 差分输入
REG30_P2DIV_IN_IN4_SING  = 1<<3  #选择IN4 单端输入
REG30_P2DIV_IN_NOCLK     = 2<<3  #无时钟进入P2
#-----------------------------------------------------------#
REG28_P2DIV_IN_IN56_DIFF = 0<<5  #选择IN5 IN6 差分输入
REG28_P2DIV_IN_IN4_SING  = 1<<5  #选择IN4 单端输入
REG28_P2DIV_IN_NOCLK     = 0<<5  #无时钟进入P2







#----------------MS0_P1[17:0]--55[1:0]，54，53寄存器组成-------------#
# Ms0_P1 = int(round((Na*Nc+Nb)*128/Nc-512))
#MS_P1  = MS_P1(MSx_a,MSx_b,MSx_c)
REG53  = MS_P1 & 0x000FF
REG54  = MS_P1 & 0x0FF00
REG55_1downto0 = MS_P1 & 0x30000 

#--------------MS0_P2[29:0]--由寄存器58，57，56，55[7:2]组成----------#
# Ms0_P2         = Nb*128%Nc
#MS_P2          = MS_P2()
REG55_7downto2 = MS_P2 & 0x0000003F
REG56          = MS_P2 & 0x00003FC0
REG57          = MS_P2 & 0x003FC000
REG58          = MS_P2 & 0x3FC00000

#--------------Ms0_P3[29:0]--由寄存器62[5:0],61,60,59----------------#
# print hex(int (Ms0_P1))
# print Ms0_P2



#-----------------------------------------------------------#
#---------------------配置PLL参数----------------------------#
#-----------------------------------------------------------#

#-------reg49[3:0]选择k值和fpfd的工作频率----------------------#
REG49_K_Fpfd_15M   = 0   # k = 925 同时 Fpfd >= 15MHz
REG49_K_Fpfd_8M15  = 5   # k = 325 同时 8MHz <= Fpfd < 15MHz
REG49_K_Fpfd_5M8   = 14  # k = 185 同时 5MHz <= Fpfd < 8MHz

#-------reg49[6:4]选择fvco和Q值------------------------------#
REG49_VCO_GAIN_Q3  = 0<<4   # vco_gian >2.425G 同时 Q = 3
REG49_VCO_GAIN_Q4  = 1<<4   # vco_gian <2.425G 同时 Q = 4

#--------reg51[2:0]---Multisynth相位错误校正，此三位必须为111---#
REG51_MULTISYNTH_PHERROR_CORREC = 7 



#-----------------------------------------------------------#
#---------------------配置输出驱动----------------------------#
#-----------------------------------------------------------#

#-----------------------------------------------------------#
#---------------------配置4个输出端口电平类型------------------#
#-----------------------------------------------------------#

#---reg36[2:0],reg37[2:0],reg38[2:0],reg39[2:0]--电平类型----#
REG36_7_8_9_DRVx_FMT_RE     = 0 # 保留位
REG36_7_8_9_DRVx_FMT_CMOS1  = 1 # CMOS/SSTL/HSTL A enable B disable
REG36_7_8_9_DRVx_FMT_CMOS2  = 2 # CMOS/SSTL/HSTL A disable B enable
REG36_7_8_9_DRVx_FMT_CMOS3  = 3 # CMOS/SSTL/HSTL A disable B disable
REG36_7_8_9_DRVx_FMT_LVPECL = 4 # LVPECL
REG36_7_8_9_DRVx_FMT_LVDS   = 5 # LVDS
REG36_7_8_9_DRVx_FMT_CML    = 6 # CML
REG36_7_8_9_DRVx_FMT_HCSL   = 7 # HCSL

#-----------------------------------------------------------#
#---------------------配置4个输出端口电压大小------------------#
#-----------------------------------------------------------#

#----reg35[7:0]配置四个端口的电压大小--------------------------#
#----reg35[1:0]：0端口--reg35[3:2]：1端口--reg35[5:4]：2端口--reg35[7:6]：3端口--#
REG35_DRVx_VDDO33 = 0 # 端口输出电压为3.3V 
REG35_DRVx_VDDO25 = 0 # 端口输出电压为2.8V
REG35_DRVx_VDDO18 = 0 # 端口输出电压为1.8V
REG35_DRVx_VDDO15 = 0 # 端口输出电压为1.5V

#-----------------------------------------------------------#
#---------------------配置4个输出端口驱动修整------------------#
#-----------------------------------------------------------#

#---reg42[4:0],reg41[6:0],reg40[7:0]------------------------#
REG40_41_42_DRVx_CMOS33 = 23
REG40_41_42_DRVx_CMOS25 = 19
REG40_41_42_DRVx_CMOS18 = 21

REG40_41_42_DRVx_HSTL15 = 31

REG40_41_42_DRVx_SSTL33 = 4
REG40_41_42_DRVx_SSTL25 = 13
REG40_41_42_DRVx_SSTL18 = 23

REG40_41_42_DRVx_LVPECL33 = 15
REG40_41_42_DRVx_LVPECL25 = 16

REG40_41_42_DRVx_LVDS33     = 3
REG40_41_42_DRVx_LCDS25OR18 = 4

REG40_41_42_DRVx_HCSL33 = 7
REG40_41_42_DRVx_HCSL25 = 7
REG40_41_42_DRVx_HCSL18 = 7

REG40_41_42_DRVx_CML33 = 8
REG40_41_42_DRVx_CML25 = 9

#-----------------------------------------------------------#
#---------------------配置4个输出端口使能---------------------#
#-----------------------------------------------------------#

#------------reg230[4:0]------------------------------------#
REG230_OEBx_ENABLE  = 0
REG230_OEBx_DISABLE = 1

#-----------------------------------------------------------#
#---------------------配置4个输出端口未使能状态----------------#
#-----------------------------------------------------------#

#-----reg110[7:6],114[7:6],118[7:6],122[7:6]----------------#
REG110_114_118_122_CLKx_DISSTHIz = 0
REG110_114_118_122_CLKx_DISSTLOW = 1
REG110_114_118_122_CLKx_DISSTHIG = 2
REG110_114_118_122_CLKx_DISSTAWO = 3

#-----------------------------------------------------------#
#---------------------配置4个时钟端口倒置反转------------------#
#-----------------------------------------------------------#

#---reg36[4:3],reg37[4:3],reg38[4:3],reg39[4:3]-------------#

REG36_7_8_9_DRVx_INV_NO = 0
REG36_7_8_9_DRVx_INV_ONLYA = 1
REG36_7_8_9_DRVx_INV_ONLYB = 2
REG36_7_8_9_DRVx_INV_BOTAB = 3


#-----------------------------------------------------------#
#---------------------配置4个端口输出时钟选择------------------#
#-----------------------------------------------------------#

#---reg31[7:5],reg32[7:5],reg33[7:5],reg34[7:5]------------#

REG31_2_3_4_RxDIV_IN_FBCLK = 0
REG31_2_3_4_RxDIV_IN_REFCLK = 1
REG31_2_3_4_RxDIV_IN_DIVFBCLK = 2
REG31_2_3_4_RxDIV_IN_DIVREFCLK = 3
REG31_2_3_4_RxDIV_IN_XOCLK = 4
REG31_2_3_4_RxDIV_IN_M0CLK = 5
REG31_2_3_4_RxDIV_IN_MNCLK = 6
REG31_2_3_4_RxDIV_IN_NOCLK = 7

#-----------------------------------------------------------#
#---------------------配置4个端口输出时钟分频------------------#
#-----------------------------------------------------------#

#---reg31[4:2],reg32[4:2],reg33[4:2],reg34[4:2]------------#
REG31_2_3_4_RxDIV1      =  0 
REG31_2_3_4_RxDIV2      =  1
REG31_2_3_4_RxDIV4      =  2
REG31_2_3_4_RxDIV8      =  3
REG31_2_3_4_RxDIV16      =  4
REG31_2_3_4_RxDIV32      =  5


IIC_REG_ADDR28      = 28
IIC_REG_ADDR29      = 29
IIC_CONFIG_ADDR28   = REG28_XTAL_FREQ_8Mto11M & REG28_P1DIV_IN_IN3_SING
IIC_CONFIG_ADDR29   = REG29_P1DIV_IN_IN12_DIFF & REG29_PFD_IN_P1DIV_IN & REG29_P1DIV_DIV1
IIC_REG_ADDR_LIST   = [IIC_REG_ADDR28,IIC_REG_ADDR29]
IIC_REG_CONFIG_LIST = [ IIC_CONFIG_ADDR28,IIC_CONFIG_ADDR29]

print IIC_REG_ADDR_LIST[0],IIC_REG_CONFIG_LIST[0]





















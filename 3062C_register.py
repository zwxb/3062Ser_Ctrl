# -*- coding: utf-8 -*- 
####------3062C寄存器命令
####------参照3062C的寄存器分配手册
####------作者：刘少鹏
####------日期：2016/6/20
####------修改原因：
####------修改日期：
#---------该文件对寄存器分为地址和数据两部分 
#---------其中addr部分主要是对寄存器地址进行宏定义
#---------其中data部分主要是对寄存器的命令进行详细说明

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_RESET_REG   = 0x00000010 #------addr部分
ADC_RESET       = 0x00000001 #------data部分：当第0位为1表示进行复位 可以直接赋值
ADC_CLEAR_RESET = 0x00000000 #------data部分：当第0位为0表示进行复位 可以直接赋值


#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_MODE_REG    = 0x00000011 #------addr部分
ADC_START       = 0x10000000 #------data部分：当第31位为1表示进行自测模式
ADC_STOP        = 0x00000000 #------data部分：当第31位为0表示进行采样模式
ADC_MODE        = 0x00000000 #------data部分：第［15:8］为AD工作模式 第［7:0］为FIR滤波器的工作模式 共19种模式
							 #------其中模式需要根据设置的采样率判断后，进行模式设置
#----------使用方式 ADC_MODE_REG ＝ ADC_START ｜ ADC_MODE ----------------------------#

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_TEST_FREQ_REG    = 0x00000012 #------addr部分
ADC_TEST_FREQ_DATA   = 0x10000000 #------data部分:该寄存器作用为自测数据累加的频率控制，根据AD模块工作的时钟频率计算分频参数 
								  #------详细计算方法查看寄存器文档说明,直接赋值

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_CLK_MODE_REG     = 0x00000013 #------addr部分
ADC_INTERNAL_CLK     = 0x00000000 #------data部分:该寄存器作用为选择AD工作时钟，第［1:0］位来控制 00:10M-FPGA内部发送时钟 
ADC_EXTERNAL_CLK	 = 0x00000001 #------data部分:该寄存器作用为选择AD工作时钟，第［1:0］位来控制 01:10M-外部输入时钟
ADC_1588_CLK         = 0x00000010 #------data部分:该寄存器作用为选择AD工作时钟，第［1:0］位来控制 10:10M-1588时钟

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_SYNC_MODE_REG     = 0x00000014 #------addr部分
ADC_NO_SYNC           = 0x00000000 #------data部分:该寄存器作用为选择AD同步设置，第［1:0］位来控制 00:不同步 
ADC_GPS_SYNC	      = 0x00000001 #------data部分:该寄存器作用为选择AD工作时钟，第［1:0］位来控制 01:GPS/BD同步
ADC_1588_SYNC         = 0x00000010 #------data部分:该寄存器作用为选择AD工作时钟，第［1:0］位来控制 10:1588同步

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_SYNC_DELAY_REG    = 0x00000015 #------addr部分
ADC_NO_SYNC           = 0x00000000 #------data部分:该寄存器作用为甩掉同步后AD上数错误点，同时也可以对滤波器的51点进行甩除，该计算详见vhdl代码
								   #该数值和滤波器的工作模式有关，需要根据工作模式不同设置不同参数

#-------------------------------------------------------------#
#--------------addr & data  only R-------------------------------#
#-------------------------------------------------------------#
ADC_STATUS_REG    	  = 0x00000016 #------addr部分 #------data部分:该寄存器为只读寄存器，该数据为数据传输过程中各个节点的状态

#-------------------------------------------------------------#
#--------------addr & data  only R-------------------------------#
#-------------------------------------------------------------#
ADC_DDR_USED_REG      = 0x00000017 #------addr部分 #------data部分:该寄存器为只读寄存器，该数据表示DDR目前内部使用情况

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
ADC_START_REG         = 0x00000018 #------addr部分
ADC_START             = 0x00000001 #------data部分:该寄存器作用为控制AD采样开始和结束 第0位 1:开始 
ADC_START             = 0x00000000 #------data部分:该寄存器作用为控制AD采样开始和结束 第0位 0:停止 


#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
DMA_CTRL_REG          = 0x00000019 #------addr部分
DMA_SINGLE_PACKET     = 0x00000000 #------data部分:该寄存器作用为控制DMA传输方式 第31位 0:连续传输数据包，不停止
DMA_CONTINU_PACKET    = 0x80000000 #------data部分:该寄存器作用为控制DMA传输方式 第31位 0:一个数据包传输完成后将自动停止 
DMA_START             = 0x00000001 #------data部分:该寄存器作用为控制DMA开始停止 第0位  1:DMA开始 
DMA_STOP			  = 0x00000000 #------data部分:该寄存器作用为控制DMA开始停止 第0位  0:DMA停止 

#-------------使用方法 DMA_CTRL_REG = DMA_CONTINU_PACKET | DMA_START--------------------------------------------#

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
DMA_SIZE_REG          = 0x0000001A #------addr部分
DMA_PACKET_SIZE       = 0x00000000 #------data部分:该寄存器作用为设置DMA包的大小，该寄存器根据采样率的不同设置不同

#-------------------------------------------------------------#
#--------------addr & data  R/W-------------------------------#
#-------------------------------------------------------------#
CH_ENABLE_REG         = 0x00000220 #------addr部分
AD_ENABLE             = 0x80000000 #------data部分:该寄存器作用为控制AD工作和静默 第31位 1:AD处于工作模式
AD_DISENABLE          = 0x00000000 #------data部分:该寄存器作用为控制AD工作和静默 第31位 0:AD处于静默模式
AD_EN_CHANEL_NUMBER   = 0x00000000 #------data部分:该寄存器作用为表示通道使能数目





















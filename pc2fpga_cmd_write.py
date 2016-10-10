# -*- coding:utf-8 -*- 
####------地址函数和数据函数上层封装
####------
####------作者：刘少鹏
####------日期：2016/6/20
import cmd_write_adr
import cmd_write_data
def pc2fpga_cmd_write(addr,data):
	print cmd_write_adr.cmd_write_adr(addr)
	print cmd_write_data.cmd_write_data(data)
pc2fpga_cmd_write(0x00000041,0x80000001)


###finish------write----cmd-------------########
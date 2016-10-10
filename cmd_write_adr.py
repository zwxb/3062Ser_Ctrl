# -*- coding: utf-8 -*- 
####------写函数地址解析
####------参照3062A的寄存器分配手册
####------作者：刘少鹏
####------日期：2016/6/20
def cmd_write_adr(reciver_addr):
    Uart_mark = 0xFFFF0000
    reciver_addr = reciver_addr
    cmd_write_mark = 0x00008000
    return hex(Uart_mark | reciver_addr | cmd_write_mark)

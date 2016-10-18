#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import name

'''
格式：\x1b[显示方式;前景色;背景色m
显示方式 0～7
前景色 30～38
背景色 40～48
'''

class colorFore:
    black   = '30'
    red     = '31'
    green   = '32'
    yellow  = '33'
    blue    = '34'
    magenta = '35'
    cyan    = '36'
    white   = '37'
    default = '38'

class colorBack:
    black   = '40'
    red     = '41'
    green   = '42'
    yellow  = '43'
    blue    = '44'
    magenta = '45'
    cyan    = '46'
    white   = '47'
    default = '48'

class style(colorFore):
    def __init__(self):
        self.fg = colorFore()
        self.bg = colorBack()
        self.reset     = '0'
        self.bright    = '1'
        self.dim       = '2'
        self.italic    = '3'
        self.underline = '4'
        self.blink     = '5'

class pyout:
    def __init__(self):
        self.s = style()
        self.fmt = '\x1b[%sm%s\x1b[0m'
    '''例子pyout.example()'''
    def example(self):
        for style in range(8):
            for fg in range(30, 39):
                s1 = ''
                for bg in range(40, 49):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')
    '''消息 格式'''
    def log(self, m, s = '0'):
        if isinstance(s, list):
            s = ';'.join(s)
        print(self.fmt % (s, m))
    def bright(self, m):
        self.log(m, self.s.bright)
    def italic(self, m):
        self.log(m, self.s.italic)
    def underline(self, m):
        self.log(m, self.s.underline)
    def info(self, m):
        self.log('ℹ️  %s' % m, self.s.blue)
    def warn(self, m):
        self.log('⚠️  %s' % m, self.s.yellow)
    def debug(self, m):
        self.log('🌀  %s' % m, self.s.magenta)
    def error(self, m):
        self.log('❌  %s' % m, self.s.red)
    def success(self, m):
        self.log('✅  %s' % m, self.s.green)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyout import *

s = Style()
pyout = Pyout()

# 基本输出
pyout.log('pyout.log()')
pyout.log('pyout.log color', s.red)
pyout.log('pyout.log style color', [s.underline, s.red])
pyout.log('pyout.log style color background', [s.underline, s.red, s.bg.white])

# 内置样式
pyout.bright('Bright')
pyout.italic('Italic')
pyout.underline('Underline')

pyout.info('Info')
pyout.debug('Debug')
pyout.warn('Warn')
pyout.error('Error')
pyout.success('Success')

# 样例输出
pyout.example()
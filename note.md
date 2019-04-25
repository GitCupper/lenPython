# Python 学习笔记

## 简介
## 1.1 Python的历史
Python是荷兰人吉多·范·罗苏姆（Guido van Rossum），1989年圣诞节期间，在阿姆斯特丹，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，作为ABC 语言的一种继承。之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧《蒙提.派森干的飞行马戏团》（Monty Python's Flying Circus）。

![Python logo](https://i.loli.net/2019/04/25/5cc161e1c8845.png)

Python的哲学：人生苦短，我用python，---- Life is short, you need Python

Python是一种解释型语言。当前的主流版本分为Python2与Python3，这是两个代码不相互美容的版本。Python的网址：[https://www.python.org/](https://www.python.org/)

### 1.2 Python的设计目标
* Python 一门简单直观的语言，并与主要竞争者一样强大；
* **开源**，以便任何人都可以为它做贡献；
* 代码像**纯英语**那样容易理解；
* 适用于**短期**开发的日常任务。

### 1.3 Python的设计哲学
* 优雅
* 明确
* 简单

### 1.4 为什么选择Python?
* 代码量少，一般情况下，`Python`是`Java`的1/5。

### 1.5 Python是一门完全面向对象的语言
* 函数、模块、数字、字符串都是对象，在Python中一切皆对象；
* 完全支持继承、重载、多重继承；
* 支持重载运算符，也支持泛型设计

### 1.6 Python社区提供了大量的第三方模块，使用方式与标准库类似
* 它们的功能覆盖**科学计算**、**人工智能**、**机器学习**、**Web开发**、**数据库接口**、**图形系统**等多个领域。

## 2.1 缩进错误

### 2.1.1 IndentationError: unexpected IndentationError
这个是由于代码编写时的缩进错误。

### 2.1.2 将.py成为可以直接运行的程序
要是想要.py文件成为在Linux中可运行的程序，可以在代码中添加注释如下
```Python
#!/usr/bin/python3
```
而后修改.py文件的权限`chmod +x hello.py`，即可实现脚本的可执行，使用`./hello.py`即可以运行这个脚本。

## 2.2 关于代码的规范问题
* Python官方提供有一系列PEP（Python Enhancement Proposals）文档
* 其中第8篇文档专门针对**Python的代码格式**给出了建议，也就是俗称的PEP 8
* 文档地址：[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
* 谷歌有对应的中文文档：[http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/)

# Python语法

## 算数运算符
### 01.算数运算符
* 算数运算符是运算符的一种
* 是完成基本的算术运算使用的符号，用来处理四则运算

|运算符|描述|实例|
|:---:|:---:|:---|
| + | 加 |10 + 20 = 30|
| - | 减 |10 - 20 = -10|
| * | 乘 |10 * 20 = 200|
| / | 除 |10 / 20 = 0.5|
| // | 取整除 |返回除法的整数部分（商） 9 // 2 输出结果为：4|
| ％ | 取余数 |返回除法的余数 9 % 2 = 1|
| ** | 幂 |双称次方、乘方，2 ** 3 = 8|

**技巧**
在Python中可以使用`**`来操作字符串，可以输出多个同样的字符
``` python
print("-" * 80)
```
这段代码可以一次性的输出80个"-"。

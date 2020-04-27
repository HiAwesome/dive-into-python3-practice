# 深入 Python3 代码练习

## P305 控制需求变化

为了获取准确的需求，尽管已经竭力将客户“钉”在原地，并经历了反复剪切、粘贴的痛苦，但需求仍然会变化。\
大多数客户在看到产品之前不知道自己想要什么，而且就算知道，他们也不擅长清晰地表述自己的想法。\
而即便擅长表述，他们在下一个版本中也会提出更多要求。因此，必须随时准备好更新测试实例以应对需求变化。

## P315 全面单元测试

全面单元测试的意思是：无需依赖某个程序员来说"相信我吧。"

## P431 代理服务器

只有当每一个角色都做按协议来做时，HTTP缓存才能发挥作用。\
一方面，服务器需要在响应中发送正确的头。\
另一方面，客户端需要在第二次请求同样的数据前理解并尊重这些响应头。\
代理服务器不是灵丹妙药，它们只会在客户端和服务器允许的情况下尽可能的聪明。

## P490 __init__.py

包含有__init__.py文件的目录总是被看作一个多文件的模块。\
没有__init__.py文件的目录中，那些.py文件是不相关的。

如果你发现自己正在用Python写一个大型的库(或者更可能的情况是，当你意识到你的小模块已经变得很大的时候)，最好花一些时间将它重构为一个多文件模块。\
这是Python所擅长的许多事情之一，那就利用一下这个优势吧。




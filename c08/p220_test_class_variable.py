import c08.p217_plural6 as plural

r1 = plural.LazyRules()
r2 = plural.LazyRules()

# 类的每个实例继承了类变量属性和值
print(r1.rules_filename)
print(r2.rules_filename)
print()

# 修改一个实例的属性值不影响其他实例，也不会修改类的属性
r2.rules_filename = 'r2-override.txt'
print(r2.rules_filename)
print(r1.rules_filename)
print(r2.__class__.rules_filename)
print()

# 如果修改类属性，所有仍然继承该实例的值会受影响，已经覆盖了该属性的值不受影响
r2.__class__.rules_filename = 'papayawhip.txt'
print(r1.rules_filename)
print(r2.rules_filename)

"""
../resource/txt/plural6-rules.txt
../resource/txt/plural6-rules.txt

r2-override.txt
../resource/txt/plural6-rules.txt
../resource/txt/plural6-rules.txt

papayawhip.txt
r2-override.txt

"""

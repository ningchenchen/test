"""
print("你好，世界！")
print(2333)
print(2.333)
print(())
print([])
print({})
print("好好",2333)
print("宁"+"灵淼")
print(1+2)
print(((1+2)*100-100)/2)
print(11)

a=input()
print("input获取的内容",a)

b=input("请您输入：")
print("input获取的内容为：",b)

print(type("你好"))
print(type(2333))
print(type(2.333))
print(type(True))
print(type(()))
print(type([]))
print(type({})) 

a=str(2333)
print(type(a))

a=float(input("请输入一个数字："))
b=float(input("请再输入一个数字："))
print(a+b)

a=len(input("请输入内容："))
b=len(input("请再输入内容："))
print("这两段内容的长度和为：",a+b)

a=(1,2,3,4,"樱桃",True,False)
print(a.index(4))

a=(1,2,3,4,"樱桃","水杯",True,"手机")
print(a[0:4])
print(a[4:])

a=[1,2,3,4]
a.append(5)
print(a)

b=[1,2,3,4]
b.insert(0,5)
print(b)

a=[1,2,3,4]
b=a.pop(0)
c=a.pop(0)
print(b+c)
"""
"""
a=[1,2,3,4]
x=[5,6,7]
a.extend(x)
print(a)
"""
"""
a={"name":"张三",0:"鼠标","age":18}
#print(a["name"])
#b=a.get("name")
#b=a.pop("name")
a.update(name="李四")
print(a)
"""
a=input("请输入您的姓名：")
b=input("请输入您的年龄：")
c=input("请输入您的性别：")
d={"name":a,"age":b,"sex":c}
print(d)
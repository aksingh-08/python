from random import seed


s = "If Comrade Napolean says it, it must be right."
a = [100, 200, 300]
def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass 

# import mod
# mod.s
# mod.a
# mod.foo([1, 2, 3, 4])
# x=mod.Foo()
# 
# from mod import s, foo
# s
# foo('erivb')
# 
# 
# s=23
# a="wgwrv"
# from mod import s as string, a as alist
# s
# string
# a
# alist
# 
# import mod as my_module
# my_module.a
# def bar():
#   from mod import foo
#   foo('corge')
# bar()
# 
# Understanding standalone execution (__name__=='__main__') and import as a module
if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('ervdv')
    x=Foo()
    print(x)


class C(object):

    def getx(self):
        print('getx')

    def setx(self, value):
        print('setx')

    def delx(self):
        print('delx')

    x = property(getx, setx, delx, "I'm the 'x' property.")  #第四个位置是注释


obj = C()

obj.x        #执行property里第一个位置的 函数 getx
obj.x = 123  #执行property里第二个位置的 函数 setx
del obj.x    #执行property里第三个位置的 函数 delx
try: 
    something 
except (NameError,SyntaxError), info: 
    print info


class A:
    class B:
        print 'Hi' 
a = A()

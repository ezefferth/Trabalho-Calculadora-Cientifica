#trabalho Calculadora cientifica
#Ezefferth Fernandes    RGA 201521901022
#Matheus G. Spartalis   RGA 201521901003
print'Menu'
print
print'Adicao              < + >'
print'Subtração           < - >'
print'Divisao             < / >'
print'Multiplicacao       < * >'
print'Exponencial         < ** >'
print'Exponencial narutal < n >'
print'Logaritimo          < l >'
print'Logaritimo natural  < n >'
print'Fatorial            < f >'
print'Raiz                < r >'
print'Seno                < s >'
print'Cosseno             < c >'
print'Tangente            < t >'
print'Pi                  < pi >'
print'Fibonnaci           < phi >'
print'Modulo              < m >'
print'Bascara             < b >'
print
def adicao(): #adicao
    x=input()
    y=input()
    soma=x+y
    print'%.2f'%soma
def sub(): #subtracao
    x=input()
    y=input()
    subtracao=x-y
    print'%.2f'%subtracao

def div(): #divisao
    x=input()
    y=input()
    if y!=0:
        divisao=x/float(y)
        print'%.2f'%divisao
    else:
        print'Erro'

def mult(): #multiplicacao
    x=input()
    y=input()
    multiplicacao=x*y
    print'%.2f'%multiplicacao

def expo(): #exponencial
    x=input()
    y=input()
    expo=x**y
    print'%.2f'%expo


def log(): #logaritimo - chamando outra funcao 'ln'...
    x=input()# ... logaritima natural para execucao
    y=input()
    if x>0 and y>0:
        q=logn(x)
        y=logn(y)
        s=q/y
        print'%.2f'%s
    else:
        print'Erro'

def logn(x):  #logaritima natural
    st=0
    for i in range(0,100):
        q=1/float(2*i+1)
        w=float(x-1)/(x+1)
        e=float(w)**float(2*i+1)
        soma=float(e)*float(q)
        st+=2*soma
    return st

def modulo():  #modulo
    x=input()
    if x<=0:
        x*=-1
        print'%.2f'%x
    else:
        x=x
        print'%.2f'%x

def fatorial(): #fatorial
    x=input()
    if x>=0:
        i=x
        fat=1
        while i>=1:
            fat*=i
            i-=1
        print'%.2f'%fat
    else:
        print'Erro'

def fatorial2(den): #uma funcao para ser usada em outra
    i=den
    fat=1
    while i>=1:
        fat*=i
        i-=1
    return fat

def expon():   #expoencial natural
    x=input()
    s=0
    for i in range(0,20):
        num=float(x**i)
        den=fatorial2(i)
        s+=num/den
    print'%.2f'%s
        

def cos(x):  #cosseno, chamando a funcao fatorial para complemento da equacao
    s=0
    for i in range(0,20):
        num=float(-1)**i * x**(2*i)
        den=fatorial2(2*i)
        c=num/den
        s+=c
    return s

def sen(x): #seno, chamado a funcao fatorial para complemento da equacao
    s=0
    for i in range(0,20):
        num=float(-1)**i * x**(2*i+1)
        den=fatorial2(2*i+1)
        c=num/den
        s+=c
    return s

def tg(): #tangente- chamando a funcao seno e cosseno para equacao da tangente
    x=input()
    if x<=6.28 and x>=-6.28:
        num=sen(x)
        den=cos(x)
        soma=num/den
        print'%.2f'%soma
    else:
        print'Erro'

def eulerr(): #equacao de euler
    s=0
    for i in range(1,20):
        num=i**4
        fat=1
        while i>=1:
            fat*=i
            i-=1
        den=15*float(fat)
        soma=float(num)/float(den)
        s+=soma
    return s

def pih(): #equacao de pi
    soma=0
    for i in range(0,20):
        soma+=(1.0/(16**i))*( (4.0/(8*i+1))-(2.0/(8.0*i+4))-(1.0/(8*i+5))-(1.0/(8*i+6)))
    return soma

def raiz(): #raiz enesima - utilizando o resultado de euler e a equacao...
    x=input() #...logaritima natural para execucao da equacao
    y=input()
    if x<0:
        print'Erro' 
    else:
        e=eulerr()
        ln=logn(x)
        s=e**((1.0/y) * (ln))
        print'%.2f'%s

def fibonacci():
    f1=1
    f2=2
    for i in range(0,20):
        fn=f1+f2
        f2=f1
        f1=fn
    x=fn
    f3=1
    f4=2
    for i in range(0,19):
        fnn=f3+f4
        f4=f3
        f3=fnn
    y=fnn
    soma=x/float(y)
    return soma

def bascara(x,y,z):
    delta=((y**2)-(4*x*z))
    def Raiz(x,y):
        if x<0:
            print'Erro 174'
        else:
            e=eulerr()
            ln=logn(x)
            s=e**((1.0/y) * (ln))
            return s
    soma1=(((-y)+(Raiz(delta,2)))  / 2*x)
    soma2=(((-y) - (Raiz(delta,2))) / 2*x)
    return soma1,soma2

menu=str()
while menu!='q':
    pi=pih()
    phi=fibonacci()
    euler=eulerr()
    menu=raw_input()
    if menu=='+': #adicao
        adicao()
    elif menu=='-':#subtracao
        sub()
    elif menu=='/':#divisao
        div()
    elif menu=='*':#multiplicacao
        mult()
    elif menu=='e':#exponencial
        expo()
    elif menu=='m':#modulo
        modulo()
    elif menu=='r':#raiz
        raiz()
    elif menu=='f':#fatorial
        fatorial()
    elif menu=='l':#logaritimo
        log()
    elif menu=='c':#cosseno
        x=input()
        if x<=6.28 and x>=-6.28:
            s=cos(x)
            print'%.2f'%s
        else:
            print'Erro'
    elif menu=='g':#logaritimo natural
        x=input()
        if x>0:
            r=logn(x)
            print'%.2f'% r
        else:
            print'Erro'
    elif menu=='n':#exponencial natural
        expon()
    elif menu=='euler':#euler
        euler=eulerr()
        print'%.2f'%euler
    elif menu=='pi':#pi
        pi=pih()
        print'%.2f'%pi
    elif menu=='s':#seno
        x=input()
        if x<=6.28 and x>=-6.28:
            s=sen(x)
            print'%.2f'%s
        else:
            print'Erro'
    elif menu=='t':#tangente
        tg()
    elif menu=='phi': #fibonacci
        phi='%.2f'%fibonacci()
        print phi
    elif menu=='b':
        x=input()
        y=input()
        z=input()
        print bascara(x,y,z)



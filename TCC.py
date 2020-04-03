#!/usr/bin/env python
# coding: utf-8

# In[113]:
#Note that variables are named as described in the text or as similar as possible. Some had the letter "a" added to their end
#in order to avoid programming errors.

#First, all modules are imported.

import numpy as np
import math
log = np.log


# In[114]:

#Second, basic data is asked, with while structures in order to avoid mistakes.
Sit = 3000
Acab = "Aleatorio"
carga = "Nulo"
while Sit!= 1 and Sit!= 2 and Sit!=3 and Sit!=4:
    Sit = int(input("Digite 1 para arredondamento no ressalto,\n       2 para sulco no ressalto,\n       ou 3 para canal de fundo plano,\n       4 para assento de chaveta de extremidade fresada r/d = 0.02: "))
cont = 0
while Acab!= "Retificado" and Acab!= "Usinado ou Laminado a frio" and Acab!= "Laminado a quente" and Acab!= "Forjado":
    if cont !=0:
        print("Você não digitou da forma encontrada na Tabela 1. Tente novamente.")
    Acab = str(input("Digite o acabamento superficial conforme Tabela 1: "))
    cont+=1
while carga!= "Flexão pura" and carga!= "Torção pura" and carga!= "Flexão e torção":
    if (carga == "Carga axial"):
        print("Este programa não trabalha com cargas axiais, escolha outro tipo.")
    carga = str(input("Digite o tipo de carga conforme Tabela 2: "))
rel = [50, 90, 95, 99, 99.9, 99.99, 99.999, 99.9999]
conf = float(input("Digite a confiabilidade em % conforme tabela 4: "))
while conf not in rel:
    print("Essa confiabilidade não está na tabela. Tente novamente.")
    conf = float(input("Digite a confiabilidade conforme tabela 4: "))


# In[115]:
#Third, all figures and also functions for both q and qs are implemented.

def reta(x0, y0, x1, y1, x):
    return (y0 + (y1 - y0)*(x - x0)/(x1 -  x0))
def Fig1(rDd, rrd):
    result109 = 0.8299*(rrd**(-0.165))
    result12 = 0.8013*(rrd**(-0.235))
    result133 = 0.8522*(rrd**(-0.232))
    result2 = 0.8148*(rrd**(-0.2688))
    if (rDd <= 1.09):
        result = result109
    elif (rDd <= 1.2):
        result = reta(1.09, result109, 1.2, result12, rDd)
    elif (rDd <= 1.33):
        result = reta(1.2, result12, 1.33, result133, rDd)
    elif (rDd <= 2):
        result = result = reta(1.33, result133, 2, result2, rDd)
    else:
        result = result2
    return result


# In[116]:


def Fig2(rDd, rrd):
    result102 = 0.917*(rrd**(-0.2039))
    result105 = 0.9223*(rrd**(-0.2292))
    result11 = 0.9040*(rrd**(-0.2511))
    result15 = 0.8729*(rrd**(-0.2922))
    result3 = 0.8936*(rrd**(-0.3107))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.1):
        result = reta(1.1, result11, 1.05, result105, rDd)
    elif (rDd <= 1.5):
        result = reta(1.5, result15, 1.1, result11, rDd)
    elif (rDd <= 3):
        result = reta(1.5, result15, 3, result3, rDd)
    else:
        result = result3
    return result


# In[117]:


def Fig3(rDd, rrd):
    result102 = 0.9932*(rrd**(-0.2006))
    result105 = 0.9731*(rrd**(-0.2593))
    result15 = 0.9579*(rrd**(-0.3201))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.5):
        result = reta(1.5, result15, 1.05, result105, rDd)
    else:
        result = result15
    return result


# In[118]:


def Fig4(rDd, rrd):
    result102 = 0.9872*(rrd**(-0.1196))
    result105 = 0.9632*(rrd**(-0.1587))
    result13 = 0.8667*(rrd**(-0.2522))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.3):
        result = reta(1.3, result13, 1.05, result105, rDd)
    else:
        result = result13
    return result


# In[119]:


def Fig5(rrt, rat):
    result003 = -0.8134*log(rat) + 8.6878
    result004 = -0.7040*log(rat) + 7.7962
    result005 = -0.6386*log(rat) + 7.1864
    result007 = -0.5793*log(rat) + 6.3311
    result010 = -0.4445*log(rat) + 5.5212
    result015 = -0.4971*log(rat) + 4.9092
    result020 = -0.4534*log(rat) + 4.5660
    result040 = -0.5045*log(rat) + 3.8376
    result060 = -0.6052*log(rat) + 3.6449
    result1 = -0.7237*log(rat) + 3.5022
    if rrt <= 0.03:
        result = result003
    elif rrt <= 0.04:
        result = reta(0.03,result003,0.04,result004, rrt)
    elif rrt <= 0.05:
        result = reta(0.05,result005,0.04,result004, rrt)
    elif rrt <= 0.07:
        result = reta(0.05,result005,0.07,result007, rrt)
    elif rrt <= 0.10:
        result = reta(0.10,result010,0.07,result007, rrt)
    elif rrt <= 0.15:
        result = reta(0.10,result010,0.15,result015, rrt)
    elif rrt <= 0.2:
        result = reta(0.2,result020,0.15,result015, rrt)
    elif rrt <= 0.4:
        result = reta(0.2,result020,0.4,result040, rrt)
    elif rrt <= 0.6:
        result = reta(0.6,result060,0.4,result040, rrt)
    elif rrt <= 1:
        result = reta(0.6,result060,1,result1, rrt)
    else:
        result = result1
    return result


# In[120]:


def Fig6(rrt, rat):
    result003 = -0.0871*log(rat) + 4.6640
    result004 = -0.1608*log(rat) + 4.2970
    result006 = -0.1608*log(rat) + 3.7970
    result010 = -0.2552*log(rat) + 3.2393
    result020 = -0.2244*log(rat) + 2.6760
    if rrt <= 0.03:
        result = result003
    elif rrt <= 0.04:
        result = reta(0.03,result003,0.04,result004, rrt)
    elif rrt <= 0.06:
        result = reta(0.06,result006,0.04,result004, rrt)
    elif rrt <= 0.1:
        result = reta(0.06,result006,0.1,result010, rrt)
    elif rrt <= 0.2:
        result = reta(0.1,result010,0.20,result020, rrt)
    else:
        result = result020
    return result


# In[121]:


#def q(Sut, r):
#    result04 = 0.1323*log(r) + 0.6335
#    result07 = 0.1067*log(r) + 0.7403
#    result1 = 0.0749*log(r) + 0.8381
#    result14 = 0.0409*log(r) + 0.9189
#    if Sut <= 0.4:
#        result = result04
#    elif Sut <= 0.7:
#        result = reta(0.4,result04,0.7,result07, Sut)
#    elif Sut <= 1:
#        result = reta(1,result1,0.7,result07, Sut)
#    elif Sut <= 1.4:
#        result = reta(1,result1,1.4,result14, Sut)
#    else:
#        result = result14
#    return result


# In[122]:


#def qs(Sut, r):
#    result04 = 0.1231*log(r) + 6772
#    result07 = 0.0971*log(r) + 0.7772
#    result1 = 0.0697*log(r) + 0.8566
#    result14 = 0.0455*log(r) + 0.9192
#    if Sut <= 0.4:
#        result = result04
#    elif Sut <= 0.7:
#        result = reta(0.4,result04,0.7,result07, Sut)
#    elif Sut <= 1:
#        result = reta(1,result1,0.7,result07, Sut)
#    elif Sut <= 1.4:
#        result = reta(1,result1,1.4,result14, Sut)
#    else:
#        result = result14
#    return result


# In[123]:


def q(Sut, r):
    Neuber = 0.246 - 0.308e-2*(Sut/6.89) + 0.151e-4*(Sut/6.89)**2 - 0.267e-7*(Sut/6.89)**3
    Neuber *= 25.4**0.5
    return (1/(1 + Neuber/(r**0.5)))


# In[124]:


def qs(Sut, r):
    Neuber = 0.190 - 2.51e-3*(Sut/6.89) + 1.35e-5*(Sut/6.89)**2 - 2.67e-8*(Sut/6.89)**3
    Neuber*=25.4**0.5
    return (1/(1 + Neuber/(r**0.5)))


# In[125]:


def Kt(in1, in2):
    if Sit == 1:
        Kt = Fig2(in1, in2)
    elif Sit == 2:
        Kt = Fig3(in1, in2)
    elif Sit==3:
        Kt = Fig5(in1, in2)
    else:
        Kt = 2.14
    return Kt
def Kts(in1, in2):
    if Sit == 1:
        Kts = Fig1(in1, in2)
    elif Sit == 2:
        Kts = Fig4(in1, in2)
    elif Sit == 3:
        Kts = Fig6(in1, in2)
    else:
        Kts = 3
    return Kts


# In[126]:


def Kf(Sut, r, in1, in2):
    return (1 + q(Sut,r)*(Kt(in1, in2) - 1))
def Kfs(Sut, r, in1, in2):
    return (1 + qs(Sut,r)*(Kts(in1, in2) - 1))


# In[127]:
#After defining Kf and Kfs, one can calculate all stresses as described in the text.

def σa(Kf, Ma, d):
    return (32*Kf*Ma/(np.pi*((d/10)**3)))
def σm(Kf, Mm, d):
    return (32*Kf*Mm/(np.pi*((d/10)**3)))
def τa(Kfs, Ta, d):
    return (16*Kfs*Ta/(np.pi*((d/10)**3)))
def τm(Kfs, Tm, d):
    return (16*Kfs*Tm/(np.pi*((d/10)**3)))


# In[128]:


def σal(σa, τa):
    return (σa**2 + 3*τa**2)**0.5
def σml(σm, τm):
    return (σm**2 + 3*τm**2)**0.5
def σmax(σa, σm, τa, τm):
    return ((σm + σa)**2 + 3*(τm + τa)**2)**0.5


# In[129]:
#Next, Se can be calculated

def Sel(Sut):
    if Sut<=1400:
        Sel = 0.5*Sut
    else:
        Sel = 700
    return Sel
def ka(Sut, Acab):
    if Acab == "Usinado ou Laminado a frio":
        a = 4.51
        b = -0.265
    elif Acab == "Retificado":
        a = 1.58
        b = -0.085
    elif Acab == "Laminado a quente":
        a = 57.7
        b = -0.718
    elif Acab == "Forjado":
        a = 272
        b = -0.995
    return (a*Sut**b)
def kb(d):
    if d>=2.79 and d<=51:
        kb = 1.24*d**-0.107
    elif d>= 51 and d<= 254:
        kb = 1.51*d**-0.107
    return kb
def kc(carga):
    if carga == "Flexão pura":
        kc = 1
    elif carga == "Torção pura":
        kc = 0.59
    elif carga == "Flexão e torção":
        kc = 1
    return kc

# Definition of kd, avoiding creation of another function.
askTemperature = 1
while askTemperature not in (20, 50, 100, 150, 200, 250, 300, 350, 400, 500, 550, 600):
    askTemperature = float(input("Qual a temperatura em °C? 20, 50, 100, 150, 200, 250, 300, 350, 400, 500, 550 or 600? "))
if askTemperature == 20:
    kd = 1
elif askTemperature == 50:
    kd = 1.01
elif askTemperature == 100:
    kd = 1.02
elif askTemperature == 150:
    kd = 1.025
elif askTemperature == 200:
    kd = 1.02
elif askTemperature == 250:
    kd = 1
elif askTemperature == 300:
    kd = 0.975
elif askTemperature == 350:
    kd = 0.943
elif askTemperature == 400:
    kd = 0.9
elif askTemperature == 450:
    kd = 0.843
elif askTemperature == 500:
    kd = 0.768
elif askTemperature == 550:
    kd = 0.672
elif askTemperature == 600:
    kd = 0.549


def ke(conf):
    if conf == 50:
        ke = 1
    elif conf == 90:
        ke = 0.897
    elif conf == 95:
        ke = 0.868
    elif conf == 99:
        ke = 0.814
    elif conf == 99.9:
        ke = 0.753
    elif conf == 99.99:
        ke = 0.702
    elif conf == 99.999:
        ke = 0.659
    elif conf == 99.9999:
        ke = 0.62
    return ke
kf = 1
def Se(Sut, Acab, d, carga, conf):
    return Sel(Sut)*ka(Sut, Acab)*kb(d)*kc(carga)*ke(conf)*kd


# In[130]:
#Finally, all criteria and their respective diameters can be defined as new functions

def Goodman(σal, σml, Se, Sut):
    return (σal/Se + σml/Sut)**-1
def ηvm(σmax, Sy):
    return Sy/σmax
def Soderberg(σal, σml, Se, Sy):
    return (σal/Se + σml/Sy)**-1
def ASME(d, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy):
    return (1/1000)*((16/(np.pi*d**3))*(4*(Kf*Ma/Se)**2 + 3*(Kfs*Ta/Se)**2 + 4*(Kf*Mm/Sy)**2 + 3*(Kfs*Tm/Sy)**2)**(1/2))**(-1)
def AGerber(Kf, Ma, Kfs, Ta):
    return (4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)**0.5
def BGerber(Kf, Mm, Kfs, Tm):
    return (4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)**0.5
def Gerber(AGerber, BGerber, d, Se, Sut):
    return (1/1000)*((8*AGerber/(np.pi*Se*d**3))*(1 + (1 + (2*BGerber*Se/(AGerber*Sut))**2)**0.5))**(-1)

def fatordeseg(σal, σml, Se, Sut, σmax, Sy):
    nseg = float(input("Digite o fator de segurança mínimo tolerável por você: "))
    if Goodman(σal, σml, Se, Sut) <= ηvm(σmax, Sy):
        η = Goodman(σal, σml, Se, Sut)
        print("O fator de segurança de Goodman foi escolhido, por ser menos conservador. O fator de segurança de falha por escoamento no primeiro ciclo de Von Mises é maior ou igual a este valor.")
        if η < nseg:
            print("Goodman indica a falha por fadiga do material, de acordo com seu mínimo tolerável.")
    else:
        print("O fator de Soderberg foi escolhido, pois Goodman falhou na checagem de falha por escoamento no primeiro ciclo.")
        η = Soderberg(σal, σml, Se, Sy)
        if η < nseg:
            print("Soderberg indica a falha por fadiga do material, de acordo com seu mínimo tolerável.")
    print("O fator de segurança é %.2f!" % round(η, 2))
    return η
def dGoodman(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sut):
    return 10*(((1/Se)*(4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)**0.5 + (1/Sut)*(4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)**(1/2))*(16*η/np.pi))**(1/3)
def dSoderberg(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sy):
    return 10*(((1/Se)*(4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)**0.5 + (1/Sy)*(4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)**(1/2))*(16*η/np.pi))**(1/3)
def dvm(η, Kf, Ma, Kfs, Ta, Mm, Tm, Sy):
    return (((1/((np.pi*(Sy/η))**2))*((32*Kf*(Mm+Ma))**2 + 3*(16*Kfs*(Tm+Ta))**2))**(1/6))*10
def dASME(η, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy):
    return 10*((16*η/np.pi)*(4*(Kf*Ma/Se)**2 + 3*(Kfs*Ta/Se)**2 + 4*(Kf*Mm/Sy)**2 + 3*(Kfs*Tm/Sy)**2)**0.5)**(1/3)
def dGerber(AGerber, BGerber, η, Se, Sut):
    return 10*((8*η*AGerber/(np.pi*Se))*(1 + (1 + (2*BGerber*Se/(AGerber*Sut))**2)**0.5))**(1/3)
def diameter(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sy, Sut):
    if dGoodman(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sut) >= dvm(η, Kf, Ma, Kfs, Ta, Mm, Tm, Sy):
        #print("O diâmetro de Goodman foi escolhido, por ser mais conservador. A falha por escoamento foi checada pelo critério de Von Mises.")
        d= dGoodman(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sut)
    else:
        #print("O diâmetro mais conservador de Soderberg foi escolhido, pois há risco de falha por escoamento no primeiro ciclo com Goodman.")
        d= dSoderberg(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sy)
    return d


# In[131]:
#Create a variable in order to decide what the user wants. Data inputs and calculations are going to be described
#with respect to that choice as follows.

Decide = 0
while Decide != 1 and Decide != 2 and Decide!=3 and Decide!=4:
    Decide = int(input("Pressione 1 para calcular um fator de segurança com dimensões conhecidas ou 2 para achar uma dimensão pelo fator, com decisão de critério automática entre Goodman e Soderberg.\nPara que você tenha uma tabela com os resultados de todos os critérios para fator de segurança, digite 3.\nPara que você tenha uma tabela com os resultados de todos os critérios para diâmetros, digite 4.\nSua escolha: "))


# In[132]:

newvar =29
if Decide == 1:    
    d = float(input("Digite o diâmetro da seção analisada [mm]: "))
    Sut = float(input("Digite a tensão última do material [MPa]: "))
    Sy = float(input("Digite a tensão de escoamento [MPa]: "))
    if Sit !=4:
        r = float(input("Digite o raio desejado para o entalhe [mm]: "))
    else:
        r = 0.02*d
        print("r = %.2f mm" % r)
    eq = "Alea"
    while eq != "y" and eq!= "n":
        eq = str(input("Seu eixo está em equilíbrio? y/n: "))
    
    if eq== "n" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq == "n" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = 0
        Ta = 0
    elif eq == "n" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq== "y" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    elif eq == "y" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = 0
        Ta = 0
    elif eq == "y" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    
    
    if Sit == 1:
        D = float(input("Digite o diâmetro da seção vizinha [mm]: "))
        in1 = D/d
        in2 = r/d
    elif Sit == 2:
        dinside = float(input("Digite a profundidade do sulco no eixo: "))
        in1 = d/(d - 2*dinside)
        in2 = r/(d - 2*dinside)
        D = d
    elif Sit == 3:
        a = float(input("Digite a largura do canal de anel retentor [mm]: "))
        t = float(input("Digite a profundidade do canal de anel retentor [mm]: "))
        in1 = r/t
        in2 = a/t
    else:
        in1 = 3000
        in2 = 3000
    Kf = Kf(Sut, r, in1, in2)
    Kfs = Kfs(Sut, r, in1, in2)
    Kt = Kt(in1, in2)
    Kts = Kts(in1, in2)
    q = q(Sut, r)
    qs = qs(Sut, r)
    σa = σa(Kf, Ma, d)
    σm = σm(Kf, Mm, d)
    τa = τa(Kfs, Ta, d)
    τm = τm(Kfs, Tm, d)
    σal = σal(σa, τa)
    σml = σml(σm, τm)
    σmax = σmax(σa, σm, τa, τm)
    Se = Se(Sut, Acab, d, carga, conf)
    Sel = Sel(Sut)
    ka = ka(Sut, Acab)
    kb = kb(d)
    kc = kc(carga)
    ke = ke(conf)
    n = fatordeseg(σal, σml, Se, Sut, σmax, Sy)
    sair = input("Pressione qualquer tecla + Enter para sair.")
elif Decide ==2:
    d = float(input("Digite uma estimativa inicial para o diâmetro da seção analisada [mm]: "))
    Sut = float(input("Digite a tensão última do material [MPa]: "))
    Sy = float(input("Digite a tensão de escoamento [MPa]: "))
    choice = 1000
    if Sit !=4:
        if Sit == 1:
            
            while(choice!=1 and choice != 2 and choice != 3):
                if choice!=1000:
                    print("Você digitou um valor inválido. Tente novamente!")
                choice = int(input("Digite 1 para arredondamento pontudo, 2 para bem arredondado ou 3 para escolher o raio: "))
            
            if choice == 3:
                r = float(input("Digite o raio desejado para o entalhe [mm]: "))
            elif choice == 2:
                r = 0.1*d
                newvar = 5
            else:
                r = 0.02*d
                newvar = 10
        else:
            r = float(input("Digite o raio desejado para o entalhe [mm]: "))
    else:
        r = 0.02*d
        print("r = %.2f mm" % r)
    eq = "Alea"
    while eq != "y" and eq!= "n":
        eq = str(input("Seu eixo está em equilíbrio? y/n: "))
    
    if eq== "n" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq == "n" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = 0
        Ta = 0
    elif eq == "n" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq== "y" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    elif eq == "y" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = 0
        Ta = 0
    elif eq == "y" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    if Sit == 1:
        D = float(input("Digite o diâmetro da seção vizinha [mm]: "))
        in1 = D/d
        in2 = r/d
    elif Sit == 2:
        dinside = float(input("Digite a profundidade do sulco no eixo: "))
        in1 = d/(d - 2*dinside)
        in2 = r/(d - 2*dinside)
        D = d
    elif Sit == 3:
        a = float(input("Digite a largura do canal de anel retentor [mm]: "))
        t = float(input("Digite a profundidade do canal de anel retentor [mm]: "))
        in1 = r/t
        in2 = a/t
    else:
        in1 = 3000
        in2 = 3000

    η = float(input("Digite o fator de segurança desejado: "))
    diameters = [0, 1]
    while math.fabs(diameters[-1] - diameters[-2]) >= 0.0001:
        if Sit ==1 or Sit ==2:
            Kfa = Kf(Sut, r, D/d, r/d)
            Kfsa = Kfs(Sut, r, D/d, r/d)
        elif Sit == 3:
            Kfa= Kf(Sut, r, r/t, a/t)
            Kfsa= Kfs(Sut, r, r/t, a/t)
        else:
            Kfa= Kf(Sut, r, in1, in2)
            Kfsa= Kfs(Sut, r, in1, in2)
        #Kt = Kt(in1, in2)
        #Kts = Kts(in1, in2)
        #q = q(Sut, r)
        #qs = qs(Sut, r)
        σaa = σa(Kfa, Ma, d)
        σma = σm(Kfa, Mm, d)
        τaa = τa(Kfsa, Ta, d)
        τma = τm(Kfsa, Tm, d)
        σala = σal(σaa, τaa)
        σmla = σml(σma, τma)
        σmaxa = σmax(σaa, σma, τaa, τma)
        Sea = Se(Sut, Acab, d, carga, conf)
        Sela = Sel(Sut)
        kaa = ka(Sut, Acab)
        kba = kb(d)
        kca = kc(carga)
        kea = ke(conf)
        diameters.append(diameter(η, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sea, Sy, Sut))
        d = diameters[-1]
        if newvar == 5:
            r = 0.1*d
        elif newvar == 10:
            r = 0.02*d
    if math.fabs(diameters[-1] - dGoodman(η, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sea, Sut)) <= 0.00001:
        print("O diâmetro de Goodman foi escolhido, por ser menos conservador. A falha por escoamento foi checada pelo critério de Von Mises.")
    elif math.fabs(diameters[-1] - dSoderberg(η, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sea, Sy)) <= 0.00001:
        print("O diâmetro mais conservador de Soderberg foi escolhido, pois há risco de falha por escoamento no primeiro ciclo com Goodman.")
    print("d = ", round(diameters[-1], 2), " mm")
    

elif Decide == 3:    
    d = float(input("Digite o diâmetro da seção analisada [mm]: "))
    Sut = float(input("Digite a tensão última do material [MPa]: "))
    Sy = float(input("Digite a tensão de escoamento [MPa]: "))
    if Sit !=4:
        r = float(input("Digite o raio desejado para o entalhe [mm]: "))
    else:
        r = 0.02*d
        print("r = %.2f mm" % r)
    eq = "Alea"
    while eq != "y" and eq!= "n":
        eq = str(input("Seu eixo está em equilíbrio? y/n: "))
    
    if eq== "n" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq == "n" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = 0
        Ta = 0
    elif eq == "n" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq== "y" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    elif eq == "y" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = 0
        Ta = 0
    elif eq == "y" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    
    
    if Sit == 1:
        D = float(input("Digite o diâmetro da seção vizinha [mm]: "))
        in1 = D/d
        in2 = r/d
    elif Sit == 2:
        dinside = float(input("Digite a profundidade do sulco no eixo: "))
        in1 = d/(d - 2*dinside)
        in2 = r/(d - 2*dinside)
        D = d
    elif Sit == 3:
        a = float(input("Digite a largura do canal de anel retentor [mm]: "))
        t = float(input("Digite a profundidade do canal de anel retentor [mm]: "))
        in1 = r/t
        in2 = a/t
    else:
        in1 = 3000
        in2 = 3000
    Kf = Kf(Sut, r, in1, in2)
    Kfs = Kfs(Sut, r, in1, in2)
    Kt = Kt(in1, in2)
    Kts = Kts(in1, in2)
    q = q(Sut, r)
    qs = qs(Sut, r)
    σa = σa(Kf, Ma, d)
    σm = σm(Kf, Mm, d)
    τa = τa(Kfs, Ta, d)
    τm = τm(Kfs, Tm, d)
    σal = σal(σa, τa)
    σml = σml(σm, τm)
    σmax = σmax(σa, σm, τa, τm)
    Se = Se(Sut, Acab, d, carga, conf)
    Sel = Sel(Sut)
    ka = ka(Sut, Acab)
    kb = kb(d)
    kc = kc(carga)
    ke = ke(conf)
    nGoodman = Goodman(σal, σml, Se, Sut)
    nSoderberg = Soderberg(σal, σml, Se, Sy)
    ηvm = ηvm(σmax, Sy)
    AGerber = AGerber(Kf, Ma, Kfs, Ta)
    BGerber = BGerber(Kf, Mm, Kfs, Tm)
    nGerber = Gerber(AGerber, BGerber, d, Se, Sut)
    nASME = ASME(d, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy)
    print("Seus resultados são: nGoodman = %.2f, nSoderberg = %.2f, ηvm = %.2f, nGerber = %.2f, nASME = %.2f" % (nGoodman, nSoderberg, ηvm, nGerber, nASME))
    sair = input("Pressione qualquer tecla + Enter para sair.")
    
# In[ ]:
elif Decide ==4:
    d = float(input("Digite uma estimativa inicial para o diâmetro da seção analisada [mm]: "))
    Sut = float(input("Digite a tensão última do material [MPa]: "))
    Sy = float(input("Digite a tensão de escoamento [MPa]: "))
    choice = 1000
    if Sit !=4:
        if Sit == 1:
            
            while(choice!=1 and choice != 2 and choice != 3):
                if choice!=1000:
                    print("Você digitou um valor inválido. Tente novamente!")
                choice = int(input("Digite 1 para arredondamento pontudo, 2 para bem arredondado ou 3 para escolher o raio: "))
            
            if choice == 3:
                r = float(input("Digite o raio desejado para o entalhe [mm]: "))
            elif choice == 2:
                r = 0.1*d
                newvar = 5
            else:
                r = 0.02*d
                newvar = 10
        else:
            r = float(input("Digite o raio desejado para o entalhe [mm]: "))
    else:
        r = 0.02*d
        print("r = %.2f mm" % r)
    eq = "Alea"
    while eq != "y" and eq!= "n":
        eq = str(input("Seu eixo está em equilíbrio? y/n: "))
    
    if eq== "n" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq == "n" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = float(input("Digite a componente média do momento fletor [Nm]: "))
        Tm = 0
        Ta = 0
    elif eq == "n" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = float(input("Digite a componente alternada do torque [Nm]: "))
    elif eq== "y" and carga == "Flexão e torção":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    elif eq == "y" and carga == "Flexão pura":
        Ma = float(input("Digite a componente alternada do momento fletor [Nm]: "))
        Mm = 0
        Tm = 0
        Ta = 0
    elif eq == "y" and carga == "Torção pura":
        Ma = 0
        Mm = 0
        Tm = float(input("Digite a componente média do torque [Nm]: "))
        Ta = 0
    if Sit == 1:
        D = float(input("Digite o diâmetro da seção vizinha [mm]: "))
        in1 = D/d
        in2 = r/d
    elif Sit == 2:
        dinside = float(input("Digite a profundidade do sulco no eixo: "))
        in1 = d/(d - 2*dinside)
        in2 = r/(d - 2*dinside)
        D = d
    elif Sit == 3:
        a = float(input("Digite a largura do canal de anel retentor [mm]: "))
        t = float(input("Digite a profundidade do canal de anel retentor [mm]: "))
        in1 = r/t
        in2 = a/t
    else:
        in1 = 3000
        in2 = 3000

    η = float(input("Digite o fator de segurança desejado: "))
    diameters = [0, 1]
    while math.fabs(diameters[-1] - diameters[-2]) >= 0.0001:
        if Sit ==1 or Sit ==2:
            Kfa = Kf(Sut, r, D/d, r/d)
            Kfsa = Kfs(Sut, r, D/d, r/d)
        elif Sit == 3:
            Kfa= Kf(Sut, r, r/t, a/t)
            Kfsa= Kfs(Sut, r, r/t, a/t)
        else:
            Kfa= Kf(Sut, r, in1, in2)
            Kfsa= Kfs(Sut, r, in1, in2)
        #Kt = Kt(in1, in2)
        #Kts = Kts(in1, in2)
        #q = q(Sut, r)
        #qs = qs(Sut, r)
        σaa = σa(Kfa, Ma, d)
        σma = σm(Kfa, Mm, d)
        τaa = τa(Kfsa, Ta, d)
        τma = τm(Kfsa, Tm, d)
        σala = σal(σaa, τaa)
        σmla = σml(σma, τma)
        σmaxa = σmax(σaa, σma, τaa, τma)
        Sea = Se(Sut, Acab, d, carga, conf)
        Sela = Sel(Sut)
        kaa = ka(Sut, Acab)
        kba = kb(d)
        kca = kc(carga)
        kea = ke(conf)
        diameters.append(dGoodman(η, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sea, Sut))
        d = diameters[-1]
        if newvar == 5:
            r = 0.1*d
        elif newvar == 10:
            r = 0.02*d
        dGoodmann = diameters[-1]
    diameters = [0, 1]
    while math.fabs(diameters[-1] - diameters[-2]) >= 0.0001:
        if Sit ==1 or Sit ==2:
            Kfa = Kf(Sut, r, D/d, r/d)
            Kfsa = Kfs(Sut, r, D/d, r/d)
        elif Sit == 3:
            Kfa= Kf(Sut, r, r/t, a/t)
            Kfsa= Kfs(Sut, r, r/t, a/t)
        else:
            Kfa= Kf(Sut, r, in1, in2)
            Kfsa= Kfs(Sut, r, in1, in2)
        #Kt = Kt(in1, in2)
        #Kts = Kts(in1, in2)
        #q = q(Sut, r)
        #qs = qs(Sut, r)
        σaa = σa(Kfa, Ma, d)
        σma = σm(Kfa, Mm, d)
        τaa = τa(Kfsa, Ta, d)
        τma = τm(Kfsa, Tm, d)
        σala = σal(σaa, τaa)
        σmla = σml(σma, τma)
        σmaxa = σmax(σaa, σma, τaa, τma)
        Sea = Se(Sut, Acab, d, carga, conf)
        Sela = Sel(Sut)
        kaa = ka(Sut, Acab)
        kba = kb(d)
        kca = kc(carga)
        kea = ke(conf)
        diameters.append(dSoderberg(η, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sea, Sy))
        d = diameters[-1]
        if newvar == 5:
            r = 0.1*d
        elif newvar == 10:
            r = 0.02*d
        dSoderbergg = diameters[-1]
    diameters = [0, 1]
    while math.fabs(diameters[-1] - diameters[-2]) >= 0.0001:
        if Sit ==1 or Sit ==2:
            Kfa = Kf(Sut, r, D/d, r/d)
            Kfsa = Kfs(Sut, r, D/d, r/d)
        elif Sit == 3:
            Kfa= Kf(Sut, r, r/t, a/t)
            Kfsa= Kfs(Sut, r, r/t, a/t)
        else:
            Kfa= Kf(Sut, r, in1, in2)
            Kfsa= Kfs(Sut, r, in1, in2)
        #Kt = Kt(in1, in2)
        #Kts = Kts(in1, in2)
        #q = q(Sut, r)
        #qs = qs(Sut, r)
        σaa = σa(Kfa, Ma, d)
        σma = σm(Kfa, Mm, d)
        τaa = τa(Kfsa, Ta, d)
        τma = τm(Kfsa, Tm, d)
        σala = σal(σaa, τaa)
        σmla = σml(σma, τma)
        σmaxa = σmax(σaa, σma, τaa, τma)
        Sea = Se(Sut, Acab, d, carga, conf)
        Sela = Sel(Sut)
        kaa = ka(Sut, Acab)
        kba = kb(d)
        kca = kc(carga)
        kea = ke(conf)
        diameters.append(dASME(η, Kfa, Ma, Sea, Kfsa, Ta, Mm, Tm, Sy))
        d = diameters[-1]
        if newvar == 5:
            r = 0.1*d
        elif newvar == 10:
            r = 0.02*d
        dASMEE = diameters[-1]
    diameters = [0, 1]
    while math.fabs(diameters[-1] - diameters[-2]) >= 0.0001:
        if Sit ==1 or Sit ==2:
            Kfa = Kf(Sut, r, D/d, r/d)
            Kfsa = Kfs(Sut, r, D/d, r/d)
        elif Sit == 3:
            Kfa= Kf(Sut, r, r/t, a/t)
            Kfsa= Kfs(Sut, r, r/t, a/t)
        else:
            Kfa= Kf(Sut, r, in1, in2)
            Kfsa= Kfs(Sut, r, in1, in2)
        #Kt = Kt(in1, in2)
        #Kts = Kts(in1, in2)
        #q = q(Sut, r)
        #qs = qs(Sut, r)
        σaa = σa(Kfa, Ma, d)
        σma = σm(Kfa, Mm, d)
        τaa = τa(Kfsa, Ta, d)
        τma = τm(Kfsa, Tm, d)
        σala = σal(σaa, τaa)
        σmla = σml(σma, τma)
        σmaxa = σmax(σaa, σma, τaa, τma)
        Sea = Se(Sut, Acab, d, carga, conf)
        Sela = Sel(Sut)
        kaa = ka(Sut, Acab)
        kba = kb(d)
        kca = kc(carga)
        kea = ke(conf)
        diameters.append(dvm(η, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sy))
        dvmm = diameters[-1]
        if newvar == 5:
            r = 0.1*d
        elif newvar == 10:
            r = 0.02*d
        dGoodman = diameters[-1]
    diameters = [0, 1]
    while math.fabs(diameters[-1] - diameters[-2]) >= 0.0001:
        if Sit ==1 or Sit ==2:
            Kfa = Kf(Sut, r, D/d, r/d)
            Kfsa = Kfs(Sut, r, D/d, r/d)
        elif Sit == 3:
            Kfa= Kf(Sut, r, r/t, a/t)
            Kfsa= Kfs(Sut, r, r/t, a/t)
        else:
            Kfa= Kf(Sut, r, in1, in2)
            Kfsa= Kfs(Sut, r, in1, in2)
        #Kt = Kt(in1, in2)
        #Kts = Kts(in1, in2)
        #q = q(Sut, r)
        #qs = qs(Sut, r)
        σaa = σa(Kfa, Ma, d)
        σma = σm(Kfa, Mm, d)
        τaa = τa(Kfsa, Ta, d)
        τma = τm(Kfsa, Tm, d)
        σala = σal(σaa, τaa)
        σmla = σml(σma, τma)
        σmaxa = σmax(σaa, σma, τaa, τma)
        Sea = Se(Sut, Acab, d, carga, conf)
        Sela = Sel(Sut)
        kaa = ka(Sut, Acab)
        kba = kb(d)
        kca = kc(carga)
        kea = ke(conf)
        AGerbera = AGerber(Kfa, Ma, Kfsa, Ta)
        BGerbera = BGerber(Kfa, Mm, Kfsa, Tm)
        diameters.append(dGerber(AGerbera, BGerbera, η, Sea, Sut))
        d = diameters[-1]
        if newvar == 5:
            r = 0.1*d
        elif newvar == 10:
            r = 0.02*d
        dGerberr = diameters[-1]
    print('dGoodman = %.2f, dSoderberg = %.2f, dVonMises = %.2f, dASME = %.2f, dGerber = %.2f' % (dGoodmann, dSoderbergg, dvmm, dASMEE, dGerberr))






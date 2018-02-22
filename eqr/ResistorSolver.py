import random

def resistorSolve(rVals,desRes, resQuantList, tolerance, isCap): 
    if desRes==0:return 'Possible iff Line Resistance is 0 Ohms'
    if (len(rVals)!=len(resQuantList)): return 'Invalid Specification'
    val = desRes
    L=[]
    for rInd in range(len(rVals)):
        #if type(rVals[rInd])!=type(1) or resQuantList[rInd]<1: 
        #    continue
        L+=[rVals[rInd]]*resQuantList[rInd]
    #print(L)
    N=len(L)
    indexes=[i for i in range(N)]
    combos=2**N
    EQmap={}
    bestprox=10**40
    bestproxcode=(0,0,0,0,0)
    for j in range(combos):
        currnum=random.randint(1,combos)
        while currnum in EQmap.keys():
            currnum=random.randint(1,combos)
        binar=bin(currnum)[2:]
        indList=[]
        for q in range(len(binar)):
            if int(binar[q]):indList=[q]+indList
        resList=[L[indList[i]] for i in range(len(indList))]
        for k in range(2**(len(indList)-1)): #many of these are equivalent
            PSList=[0]*(len(resList)-1)
            currmap={}
            if PSList!=[]:
                for i in range(len(bin(k)[2:])):
                    if bin(k)[i+2]=='1':PSList[i]=1
            for order in range(len(indList)):
                tempRList=resList[order:]+resList[:order]
                EQR=getEQR(tempRList,PSList)
                currmap[order]=EQR
                prox=abs(EQR-val)
                if prox<bestprox:
                    bestprox=prox
                    bestproxcode=(currnum,order,EQR,tempRList,PSList)
                if prox<tolerance:
                    return format(desRes,[prox, EQR,tempRList,PSList], isCap).encode('utf-8').strip()
        EQmap[currnum]=currmap
    s="NO EQUIVALENT RESISTANCE WITHIN TOLERANCE, CLOSEST RESULT: \n"
    return (s+format(desRes,[bestprox,bestproxcode[2],bestproxcode[3],bestproxcode[4]], 
                    isCap)).encode('utf-8').strip()
    
def getEQR(RList,PSList):
    if PSList==[]:return sum(RList)
    temp=None
    N=len(PSList)
    for i in range(N,0,-1):
        if temp==None: 
            if PSList[-1]:temp=RList[-1]+RList[-2]
            else:temp=(RList[-1]*RList[-2])/(RList[-1]+RList[-2])
        elif PSList[i-1]:temp+=RList[i-1]
        else:temp=temp*RList[i-1]/(temp+RList[i-1])
    return temp
    
def format(desR,outputList, isCap):
    if not isCap: 
        formatString = "Series given by (1), Parallel given by (0): "
        s ="Specificed Input Resistance: " +str(desR) + " [Ohms]\n" 
        s+="Equivalent Resistance: "+ str(outputList[1])+ " [Ohms]\n"
        s+="Equivalent Resistance off by: "+ str(outputList[0])+ " [Ohms]\n"
        s+="Resistors Used: "+ str(outputList[2]) + "\n"
    else: 
        formatString = "Series given by (0), Parallel given by (1): "
        s ="Specificed Input Capacitance: " +str(desR) + " [F]\n" 
        s+="Equivalent Capacitance: " + str(outputList[1]) + " [F]\n"
        s+="Equivalent Capacitance off by: " + str(outputList[0]) +" [F]\n"
        s+="Capacitors Used: " + str(outputList[2]) + "\n"
    # print(formatString, outputList[3])
    s+=formatString + str(outputList[3])
    return s
#L=[5e-12, 11e-12]
#resQuantList = [3, 0]
#desiredResistance=2.2e-12
#isCap = False
#resistorSolve(L, desiredResistance, resQuantList, 1e-13, isCap)

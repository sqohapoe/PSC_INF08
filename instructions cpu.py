
#blablabla
#stack
#execution

def nop1(self):
    "I don't know what does it do"
    return None
def nop2(self):
    "I don't know what does it do"
    return None

def pushA(self):
    stack.append(AX)    
    "push A in the stack"
def pushB(self): 
    "push B in the stack"
    stack.append(BX) 
def pushC(self): 
    "push C in the stack"
    stack.append(CX)    
def pushD(self): 
    "push D in the stack"
    stack.append(DX)

def popA(self): 
    AX=stack.pop()
def popB(self):
    BX=stack.pop()
def popC(self):
    CX=stack.pop()
def popD(self):
    DX=stack.pop()

def movcd(self):
    "C takes the value of D"
    CX=DX
def movab(self):
    "B takes the value of  A"
    BX=CX
def movii(self):
    "unknown function"

def subCAB(self):
    CX=AX-BX
def subAAC(self):
    AX=AX-CX
def incA(self):
    AX+=1
def incB(self):
    BX+=1
def incC(self):
    CX+=1
def incD(self):
    DX+=1
def decC(self):
    CX-=1
def zero(self):
    CX=0
def not0(self):
    "inverse the unity number"
    if CX%2==0:
        CX+=1
    else:
        CX-=1
def shl(self):
    "double the value of C"
    CX*=2
        
        
        
    

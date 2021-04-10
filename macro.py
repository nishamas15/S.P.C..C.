# MASCARENHAS NISHA NITIN
# BATCH B   8616
# 1. SYMBOL TABLE

global MNTC,MDTC,index
MNTC = 1
MDTC = 1
index=0
a=0

class START:
    def __init__(self):
        self.head=None
        
    def create(self,c): 
        if self.head is None:
            self.head = c
            return
        else:  
            p = self.head 
            while p.next is not None: 
               p = p.next
            p.next = c 
            return
    
    def check(self, label): 
        p = self.head 
        while p is not None:  
            if p.mname == label: 
                return p.mdtval
            p = p.next
        return 0
    
    def display(self):
        if self.head is None:
            return
        else:
            p = self.head 
            while p is not None:
                print("Index: ", p.index, " | Macro Name: ", p.mname, "| MDT Value: ", p.mdtval,"\n")  
                p = p.next 
            return

 

class MNT:
    def __init__(self, mname):
        global MNTC,MDTC
        self.index= MNTC 
        self.mname = mname
        self.mdtval = MDTC
        self.next = None
        MNTC = MNTC + 1
       
 

if __name__ == "__main__": 
    flag=0
    mdt={}
    ala={}
    start = START()
    f1 = open("mac.txt")
    f2 = open("copy.txt","wt") 
    f3 = open("esc.txt","wt")
    r = f1.read().splitlines()
    i=0
    while i != len(r)-1:
        c=r[i].split() 
        if c[0] == "MACRO":
            s={}
            i=i+1
            c=r[i].split()
            j=0
            mnt = MNT(c[0])
            start.create(mnt)
            mdt[MDTC]=c 
            MDTC = MDTC + 1
            for k in range(1,len(c)):
                if c[k] != ",":
                    s[j] = c[k]
                    j=j+1   
            for j in range(0,len(s)): 
                ala["#"+str(index)] = s[j]
                index = index + 1 
            for j in range(i+1,len(r)): 
                c = r[j].split() 
                for k in range(0,len(c)): 
                    for key,val in ala.items():
                        if c[k] == val: 
                            c[k] = key   
                            break 
                mdt[MDTC]= c
                
                MDTC = MDTC+1
                if r[j].split()[0] == "MEND": 
                    break
            i = j+1
        else: 
            f2.write(r[i])
            f2.write("\n")
            i=i+1
    f2.close()
    f2 = open("copy.txt","r")
    print("PASS 1\n")
    print("Copy File")
    print(f2.read()) 
    print("\n\nMNT")
    start.display()
    print("\n\nALA") 
    for key,val in ala.items():
        print(key,end="   ")
        print(val) 
    print("\n\nMDT")
    for key,val in mdt.items():
        print(key,end="   ")
        for i in val: 
            print(i,end=" ")
        print("\n")
    f1.close()
    f2.seek(0)
    print("\n\n\n") 
    print("PASS 2")
    r = f2.read().splitlines()
    i=0
    while i != len(r):  
        c = r[i].split()
        k=start.check(c[0]) 
        if k!=0:  
            MDTC = k
            k = mdt[MDTC] 
            for j in range(1,len(c)):
                if c[j] != ",":  
                    for key,val in ala.items(): 
                        if k[j] == val: 
                            ala[key] = c[j]  
                            break
            m=i+1
            while m != len(r): 
                MDTC = MDTC + 1
                k = mdt[MDTC] 
                for j in range(0, len(k)):
                    for key,val in ala.items(): 
                        if k[j]==key: 
                            k[j] = val 
                            break
                if k[0] == "MEND":
                    i=m
                    break
                for n in k:
                    f3.write(str(n)+" ")
                f3.write("\n")
        else:
            f3.write(r[i])
            f3.write("\n")
            i=i+1
    print("\n\nALA") 
    for key,val in ala.items():
        print(key,end="   ")
        print(val) 
    print("\n\nMDT")
    for key,val in mdt.items():
        print(key,end="   ")
        for i in val: 
            print(i,end=" ")
        print("\n")
    print("\n")
    f2.close() 
    f3 = open("esc.txt","rt")
    print("Expanded Source Code")
    print(f3.read())
    f3.close()
    

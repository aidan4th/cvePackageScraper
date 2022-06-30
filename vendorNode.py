#This is customn data note set that I made to help with the other part of the program
#Since I really hate Panda


#Practically this stores the links from all the vendors


class venNode:
    def __init__(self, vendor=None, id = None, idP = None, linkToV = None):
        self.version = None 
        self.vendor = vendor
        self.id = id
        self.idP = idP
        self.linkToV = linkToV
        self.next = None

    def __str__(self):
        return self.vendor +", "+ self.id +", " + self.idP + ", "+self.linkToV
#Practically This is a repeating node list, so that any amount of errors can be attachted to it. 
# Hopefully later they will be added to the mian panda program
class versionBugs:
    def __init__(self, version = None, problem = None):
        self.next = None
        self.version = version
        self.problem = problem
    def __str__(self):
        if (self.next != None):
            return self.version +", "+ self.problem +", "+ str(self.next) 
        else:
            return self.version +", "+ self.problem

    #Not related to the data strucutes, just functions used for editing
    #Strings to find out if they are the same version
def purifyVerNum(ver):
    firstLetter = True
    foundDecimal = False
    ver = ver.lower()
    c = 0
    while c < len(ver):
        if ver[c].isalpha() and foundDecimal == False:
            ver = ver[0:c] + ver[c+1:]
            c = c -1
        elif ver[c-1] == "." or ver[c-1].isdigit() == True:
            break
        c = c + 1
    c = 0
    ver = ver.replace(".", "")
    if ver.find('+') != -1:
        ver = ver.split('+')[0]
    while c < len(ver):
        if ver[c].isalpha():
            if firstLetter == True:
                ver = ver[0:c] + "." + str(ord(ver[c]) - 96) + ver[c+1:]
                firstLetter = False
            else:
                ver = ver[0:c] + str(ord(ver[c]) - 96) + ver[c+1:]
        c = c + 1
    return ver
def purifyText(text):
    consider = []
    for t in text.split():
        consid = False
        if any(char.isdigit() for char in t):
            consid = True
        if (consid == True):
            consider.append(purifyVerNum(t))
    return consider

def purifyTest(ver, text):
    ver = str(ver)
    text = str(text)
    ver = purifyVerNum(ver)
    consider = []
    consider = purifyText(text)
    for con in consider:
        try:
            v = float(ver)
            c = float(con)
            if (v > c):
                i = 0
                while v/10 > 1:
                    v = v/10
                    i += 1
                while c/10 > 1:
                    c = c/10
                    i -= 1
                if (i > 0):
                    v = float(ver)
                    c = float(con)
                    c = (c - (c % 1))*(10**i)+(c % 1)
                    if (c >= v):
                        return True
        except ValueError:
            #print("purifyTest: Could not convert '" + con +  "' into a float" )    
            #This will be called a lot
            None
    return False
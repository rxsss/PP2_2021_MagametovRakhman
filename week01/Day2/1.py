def defangIPaddr(self, address: str) -> str:
    s = ''
    for i in range(len(address)):
        if(address[i] == '.'):
           s = s+'[.]'
        else:
            s = s+address[i]
            
    return s
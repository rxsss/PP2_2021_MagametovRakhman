class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip = ''
        for i in range(len(address)):
            if(address[i] == '.'):
               ip = ip + '[.]'
            else:
                ip = ip + address[i]

        return ip

Solution.defangIPaddr(address = str(input()))

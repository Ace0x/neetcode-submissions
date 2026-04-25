class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""    
        for i in strs:
            y = ""
            for j in range(len(i)):
                y += chr(ord(i[j]) * 2)
            x += y + chr(1)
        print(x)
        return x

    def decode(self, s: str) -> List[str]:
        res = []
    
        x = ""
        for i in s:
            if ord(i) % 2 != 0:
                res.append(x)
                x = ""
                continue
            c = chr((ord(i) // 2))
            x += c

        return res
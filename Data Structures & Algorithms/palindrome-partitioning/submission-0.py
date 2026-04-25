class Solution:
    def partition(self, s: str):
        self.res = []
        self.palin(s, "", 0, [])
        return self.res

    def check(self, build):
        i = 0
        j = len(build) - 1

        while i < j:
            if build[i] != build[j]:
                return False
            i += 1
            j -= 1

        return True

    def palin(self, s, build, c, ls):
        if c == len(s):
            if build == "":
                self.res.append(ls.copy())
            return

        build += s[c]

        self.palin(s, build, c + 1, ls.copy())

        if self.check(build):
            temp = ls.copy()
            temp.append(build)
            self.palin(s, "", c + 1, temp)




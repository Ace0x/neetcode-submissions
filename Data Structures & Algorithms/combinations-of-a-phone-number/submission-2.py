class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.base = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.res = []
        self.digits = digits

        if len(digits) == 0:
            return []

        self.dfs(0, "")
        return self.res

    def dfs(self, i, build):
        if i == len(self.digits):
            self.res.append(build)
            return

        curr = self.digits[i]
        letters = self.base[curr]

        for j in range(len(letters)):
            self.dfs(i + 1, build + letters[j])
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in strs:
            word = dict()
            for j in i:
                word[j] = 1 + word.get(j,0)
            s = ()
            word = dict(sorted(word.items()))
            for x in word:
                s += (x,word[x])

            res = dic.get(s)
            if res:
                res.append(i)
            else:
                dic[s] = [i]
        result = []
        for i in dic:
            result.append(dic[i])
        return result
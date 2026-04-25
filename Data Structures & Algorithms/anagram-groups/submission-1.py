class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            word = [0] * 26
            for j in i:
                word[ord(j) - ord("a")] += 1
            dic[tuple(word)].append(i)
        return list(dic.values())
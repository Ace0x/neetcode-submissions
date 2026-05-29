class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        ng = n // groupSize
        gs = n % groupSize

        if gs != 0:
            return False
        
        hand = sorted(hand)

        groups = []
        for i in range(ng):
            groups.append(list())

        for i in range(n):
            cur = hand[i]
            for j in range(ng):
                if len(groups[j]) == 0:
                    groups[j].append(cur)
                    break
                last = groups[j][-1]
                if last != cur and last + 1 == cur and len(groups[j]) != groupSize:
                    groups[j].append(cur)
                    break
                if j == ng - 1:
                    return False
        #print(groups)
        return True


        


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        arr = [[a, 'a'], [b, 'b'], [c, 'c']]

        while True:
            arr.sort(reverse=True)

            added = False

            for i in range(3):
                count, char = arr[i]

                if count == 0:
                    continue

                # Can't make xxx
                if len(s) >= 2 and s[-1] == s[-2] == char:
                    continue

                s += char
                arr[i][0] -= 1
                added = True
                break

            if not added:
                break

        return s


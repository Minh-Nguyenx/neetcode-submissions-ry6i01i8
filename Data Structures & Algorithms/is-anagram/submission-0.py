class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        for c in t:
            if c not in count:
                count[c] = 1
            else:
                count[c] -= 1    

        return all(x == 0 for x in count.values())

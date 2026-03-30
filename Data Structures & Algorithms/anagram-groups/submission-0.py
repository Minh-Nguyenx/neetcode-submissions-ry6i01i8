class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS not in anagram_map:
                anagram_map[sortedS] = []

            anagram_map[sortedS].append(s)
        
        return list(anagram_map.values())
        
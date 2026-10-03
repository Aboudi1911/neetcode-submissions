class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for n in strs:
            key = "".join(sorted(n))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(n)
        return list(anagrams.values())


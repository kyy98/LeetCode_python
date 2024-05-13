class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)   ## 예를들면 "eat"을 sort하면 "aet", "tea"도 동일
        return list(anagrams.values())

        
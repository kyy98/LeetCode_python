class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)  ## 초기값이 list 형태로 []가 주어진다.

        for w in strs:
            anagrams[''.join(sorted(w))].append(w)
        return anagrams.values() 
            

            


        
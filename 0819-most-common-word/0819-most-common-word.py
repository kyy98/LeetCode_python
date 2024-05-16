class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]   ##[0-9a-zA-Z]

        counts = collections.Counter(s)

        return counts.most_common(1)[0][0]       ## [(word: count)] -> (word, count) -> word


        

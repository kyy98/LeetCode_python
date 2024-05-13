class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(s)

        return counts.most_common(1)[0][0]


        
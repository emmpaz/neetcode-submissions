class Solution:

    def encode(self, strs: List[str]) -> str:
        self.hm = dict()
        self.n = len(strs)
        encoded = ""
        for i, x in enumerate(strs):
            self.hm[i] = x
            encoded += x
        return encoded

    def decode(self, s: str) -> List[str]:
        l = []
        for i in range(self.n):
            l.append(self.hm[i])

        return l

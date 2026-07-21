class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "abc"
        if strs==[""]:
            return "def"
        string="😀".join(strs)
        return string[::-1]


    def decode(self, s: str) -> List[str]:
        if s=="abc":
            return []
        if s=="def":
            return [""]
        string=s[::-1]
        return string.split("😀")

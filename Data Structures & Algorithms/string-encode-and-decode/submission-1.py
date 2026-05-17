class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for c in strs:
            s += c
            s += "."
        return s


    def decode(self, s: str) -> List[str]:
        list_str = []
        x = ""
        for c in s:
            if c != ".":
                x += c
            else:
                list_str.append(x)
                x = ""
        return list_str

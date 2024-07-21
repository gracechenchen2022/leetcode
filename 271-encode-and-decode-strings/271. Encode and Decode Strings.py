class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        return "".join(f"{len(s)}#{s}" for s in strs)
#tc: o(n) sc: o(n)
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            strs.append(s[j+1 :j + 1 + length])
            i = j + 1 + length
        return strs
        
#tc: o(m) sc: o(m)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = {}
        for x in s:
            dct[x] = dct.get(x, 0) + 1
        for x in t:
            if x in dct:
                dct[x] = dct.get(x) - 1
            else:
                return False

        return all(x == 0 for x in dct.values())


s = "a"
t = "ab"
anagram = ValidAnagram()
print(anagram.isAnagram(s,t))

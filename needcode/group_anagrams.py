class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}

        for word in strs:
            array_alph = [0] * 26
            for char in word:
                array_alph[ord(char) - ord("a")] += 1
            key = tuple(array_alph)

            result.setdefault(key, []).append(word)

        return list(result.values())


solution = Solution()


strs = ["act", "pots", "tops", "cat", "stop", "hat"]
output = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
print(solution.groupAnagrams(strs))
# print(output)

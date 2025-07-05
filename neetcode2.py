# Valid Anagram


from typing import Dict


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        map1: Dict[str] = {}
        map2: Dict[str] = {}

        for val in s:
            if val in map1:
                map1[val] = map1[val] + 1
            else:
                map1[val] = 1

        for val in t:
            if val in map2:
                map2[val] = map2[val] + 1
            else:
                map2[val] = 1

        if len(map1) is not len(map2):
            return False
        for k, v in map2.items():
            if k not in map1:
                return False
            if map1[k] != v:
                return False

        return True


s = Solution()
s.isAnagram("asdasdsadsadsadsasdaasd", "asdasdsadsadsadsasdaasd")

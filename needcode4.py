# medium groupAnagrams

from collections import defaultdict
from typing import List


class Solution:
    # time complexity will be n *m
    # where m will be number of strs and n will be each chars length
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for item in strs:
            freq_key = [0] * 26
            for c in item:
                # ord a will be at 97 so whatever is greater than a will get subtracted to get the actual position to be placed in the frq_key in the array span
                print(ord(c))
                print(ord("a"))
                freq_key[ord(c) - ord("a")] += 1
            hashed_key = tuple(freq_key)
            freq[hashed_key].append(item)
        return list(freq.values())


s = Solution()

print(s.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))

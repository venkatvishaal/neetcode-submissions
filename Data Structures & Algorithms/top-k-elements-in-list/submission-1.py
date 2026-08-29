from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        most_commons = counts.most_common(k)

        return [key for key, value in most_commons]
        
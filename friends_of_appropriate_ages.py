
class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        counts = Counter(ages)
        ages.sort()

        j = 0
        k = 0
        res = 0

        for i, val in enumerate(ages):
            if ages[i] < 15:
                continue

            min_age = val * 0.5 + 7

            while ages[j] <= min_age:
                j += 1

            res += counts[ages[i]] - 1

            if ages[i] != ages[k]:
                k = i

            res += k - j

        return res

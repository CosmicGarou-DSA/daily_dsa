class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        i , j = 0, (len(people) - 1)
        people = sorted(people)

        while i <= j:
            if people[i] + people[j] <= limit:
                boat += 1
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                boat += 1
                j -= 1

        return boat
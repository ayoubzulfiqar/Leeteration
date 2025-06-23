class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = [0] * num_people
        current_candy_amount = 1
        person_index = 0

        while candies > 0:
            gift = min(current_candy_amount, candies)
            ans[person_index] += gift
            candies -= gift
            current_candy_amount += 1
            person_index = (person_index + 1) % num_people
        
        return ans
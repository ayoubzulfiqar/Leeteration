class Solution:
    def countSeniors(self, details: list[str]) -> int:
        senior_count = 0
        for detail_str in details:
            # The age is represented by characters at indices 11 and 12
            age_str = detail_str[11:13]
            age = int(age_str)
            if age > 60:
                senior_count += 1
        return senior_count
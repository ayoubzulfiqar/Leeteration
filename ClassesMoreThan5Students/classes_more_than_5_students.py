from collections import defaultdict

class Solution:
    def findClasses(self, courses: list[dict]) -> list[dict]:
        class_counts = defaultdict(int)
        for row in courses:
            class_name = row["class"]
            class_counts[class_name] += 1

        result = []
        for class_name, count in class_counts.items():
            if count >= 5:
                result.append({"class": class_name})
        return result
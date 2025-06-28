candidates_data = [
    {"name": "Alice", "skills": ["Python", "SQL", "Machine Learning", "Statistics", "Data Visualization"]},
    {"name": "Bob", "skills": ["Python", "R", "SQL", "Data Analysis"]},
    {"name": "Charlie", "skills": ["Java", "C++", "Algorithms"]},
    {"name": "David", "skills": ["Python", "Machine Learning", "Statistics"]},
    {"name": "Eve", "skills": ["SQL", "Data Visualization", "Business Intelligence"]},
    {"name": "Frank", "skills": ["Python", "Machine Learning", "Statistics", "Deep Learning", "SQL", "Data Visualization", "Communication"]},
    {"name": "Grace", "skills": ["R", "Statistics", "SQL"]},
    {"name": "Heidi", "skills": ["Python", "SQL", "Data Analysis"]},
    {"name": "Ivan", "skills": ["Python", "Machine Learning", "Statistics", "SQL", "Spark", "Cloud"]},
]

def find_data_scientist_candidates(candidates):
    required_skills = {"Python", "Machine Learning", "Statistics", "SQL"}
    
    qualified_candidates = []
    
    for candidate in candidates:
        candidate_skills_set = set(candidate["skills"])
        
        if required_skills.issubset(candidate_skills_set):
            qualified_candidates.append(candidate["name"])
            
    return qualified_candidates

if __name__ == "__main__":
    found_candidates = find_data_scientist_candidates(candidates_data)
    print(found_candidates)
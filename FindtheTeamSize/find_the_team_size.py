import math

def find_team_size(total_tasks: int, tasks_per_member: int) -> int:
    if not isinstance(total_tasks, int) or total_tasks < 0:
        raise ValueError("Total tasks must be a non-negative integer.")
    if not isinstance(tasks_per_member, int) or tasks_per_member <= 0:
        raise ValueError("Tasks per member must be a positive integer.")

    if total_tasks == 0:
        return 0

    return math.ceil(total_tasks / tasks_per_member)

if __name__ == "__main__":
    try:
        num_tasks_str = input()
        tasks_per_person_str = input()
        
        num_tasks = int(num_tasks_str)
        tasks_per_person = int(tasks_per_person_str)
        
        required_team_size = find_team_size(num_tasks, tasks_per_person)
        print(required_team_size)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
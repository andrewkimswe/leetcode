class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """ 
        Time Complexity: O(N) where N is length of tasks
        Space Complexity: O(1) since counter array is fixed size 26
        """
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
            
        max_count = max(task_counts)
        
        max_count_tasks = task_counts.count(max_count)
        
        return max(
            (max_count - 1) * (n + 1) + max_count_tasks,
            len(tasks)
        )
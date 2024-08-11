class Job:
    

    def __init__(self, profit=0, deadline=0, job_id=0):
        self.profit = profit
        self.deadline = deadline
        self.id = job_id

class Solution:

    def find(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        parent[self.find(parent, y)] = self.find(parent, x)
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = max(job.deadline for job in Jobs)
        parent = list(range(max_deadline + 1))
        jobs_done = 0
        max_profit = 0
        for job in Jobs:
            available_slot = self.find(parent, job.deadline)
            if available_slot > 0:
                self.union(parent, available_slot - 1, available_slot)
                jobs_done += 1
                max_profit += job.profit
        
        return jobs_done, max_profit

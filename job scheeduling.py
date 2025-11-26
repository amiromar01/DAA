def job_scheduling(jobs):
    # jobs = [(id, profit, deadline)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_dead = max(j[2] for j in jobs)
    slots = [None] * (max_dead + 1)
    total_profit = 0

    for jid, profit, dead in jobs:
        for t in range(dead, 0, -1):
            if slots[t] is None:
                slots[t] = jid
                total_profit += profit
                break

    return total_profit, [j for j in slots if j]

print(job_scheduling([(1, 100, 2), (2, 19, 1), (3, 27, 2), (4, 25, 1), (5, 15, 3)]))
# Output: (142, [1, 3, 5])
def activity_selection(activities):
    # activities = [(start, end)]
    activities.sort(key=lambda x: x[1])
    res = []
    last_end = -float('inf')

    for s, e in activities:
        if s >= last_end:
            res.append((s, e))
            last_end = e

    return res
print(activity_selection([(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]))
# Output: [(1, 3), (3, 5), (5,
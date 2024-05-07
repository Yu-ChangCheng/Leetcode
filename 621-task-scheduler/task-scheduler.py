class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = Counter(tasks)
        min_heap = [-cnt for cnt in cnt.values()]
        heapq.heapify(min_heap)
        q = deque()
        time = 0

        while q or min_heap:
            time += 1
            if min_heap:
                cnt = 1 + heapq.heappop(min_heap)
                if cnt < 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(min_heap, q.popleft()[0])
        return time
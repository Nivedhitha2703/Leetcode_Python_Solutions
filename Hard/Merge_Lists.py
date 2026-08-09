import heapq

class Solution:
    def mergeKLists(self, lists):

        heap = []

        # Put the first node of every list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # Dummy node simplifies list construction
        dummy = ListNode(0)
        current = dummy

        while heap:

            # Get the smallest node
            value, i, node = heapq.heappop(heap)

            # Add it to the result
            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next

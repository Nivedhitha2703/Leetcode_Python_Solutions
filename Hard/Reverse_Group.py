class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find the kth node
            kth = self.getKth(groupPrev, k)

            # Not enough nodes for another group
            if kth is None:
                break

            groupNext = kth.next

            # Reverse the group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous part to reversed group
            temp = groupPrev.next
            groupPrev.next = kth

            # Move to the next group
            groupPrev = temp

        return dummy.next

    def getKth(self, curr, k):

        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

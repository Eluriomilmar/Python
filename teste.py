# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        vetor = []
        inicio = head
        reverter = []
        final = []
        while head:
            vetor.append(head.val)
            head = head.next
        espelho_tam = 0
        espelho_k = 0
        erro = False
        while espelho_tam < len(vetor):
            while espelho_k < k:
                try:
                    reverter.append(vetor[espelho_tam + espelho_k])
                except IndexError:
                    print(len(reverter))
                    for i in reverter:
                        final.append(i)
                    erro = True
                finally:
                    espelho_k += 1
            espelho_k = 0
            if erro == False:
                reverter.sort(reverse=True)
                for i in reverter:
                    final.append(i)
            espelho_tam += k
            reverter = []
        lista = ListNode(0)
        inicio = lista
        for i in final:
            lista.next = ListNode(i)
            lista = lista.next
        return inicio.next
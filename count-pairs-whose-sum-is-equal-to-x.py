class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        d={}
        res=0
        while n1:
            d[head1.data]=1
            n1-=1
            head1=head1.next
        while n2:
            if x-head2.data in d:
                res+=1
            n2-=1
            head2=head2.next
        return res

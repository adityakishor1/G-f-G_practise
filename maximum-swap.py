class Solution(object):
    def maximumSwap(self, num):
        numList = [int(n) for n in str(num)]
        positions = collections.defaultdict(list)
        for i, n in enumerate(numList): positions[n].append(i) #[1]
        
        i = 0
        for i, n1 in enumerate(numList): #[2]
            n1 = numList[i]
            for n2 in xrange(9, n1, -1): 
                if n2 in positions and len(positions[n2])>0:
                    j = positions[n2][-1] #[3]
                    numList[i], numList[j] = numList[j], numList[i]
                    return int(''.join([str(n) for n in numList]))
            positions[n1].pop(0) #[4]
            
        return num

class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        triplets = set()  
        
        for i in range(n - 2):
            seen = {}
            for j in range(i + 1, n):
                target = -(arr[i] + arr[j])
                if target in seen:
                    triplet = tuple(sorted([i, seen[target], j]))
                    triplets.add(triplet)
                seen[arr[j]] = j 
        return [list(triplet) for triplet in sorted(triplets)]

class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] == arr[k]:
                    return True  
                elif arr[i] + arr[j] < arr[k]:
                    i += 1  
                else:
                    j -= 1 
        
        return False  

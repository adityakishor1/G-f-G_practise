class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []
        smallest = [0] * n
        largest = [0] * n
        smallest[0] = arr[0]
        for i in range(1, n):
            smallest[i] = min(smallest[i-1], arr[i])
        largest[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            largest[i] = max(largest[i+1], arr[i])
        for j in range(1, n-1):
            if smallest[j-1] < arr[j] < largest[j+1]:
                return [smallest[j-1], arr[j], largest[j+1]]
        return []

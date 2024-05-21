class Solution:
    def printKClosest(self, arr, n, k, x):
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        left_closest, right_closest = left - 1, left
        k_closest = []
        while len(k_closest) < k:
            if left_closest < 0:
                k_closest.append(arr[right_closest])
                right_closest += 1
            elif right_closest >= n:
                k_closest.append(arr[left_closest])
                left_closest -= 1
            elif abs(arr[left_closest] - x) <= abs(arr[right_closest] - x):
                k_closest.append(arr[left_closest])
                left_closest -= 1
            else:
                k_closest.append(arr[right_closest])
                right_closest += 1
        
        return k_closest

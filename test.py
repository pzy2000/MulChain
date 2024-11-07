class Solution:

    def pairNumbers(self, a, b):
        def count_inversions(arr):
            # Helper function to use merge sort to count inversions
            if len(arr) < 2:
                return 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            # Count inversions in each half and during the merge
            inversions = count_inversions(left) + count_inversions(right)

            # Merge step
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    arr[k] = left[i]
                    inversions += len(right) - j  # All remaining elements in right are smaller
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

            return inversions

        # Create the transformed array diff
        diff = [a[i] - b[i] for i in range(len(a))]
        detail = [(a[i], b[i]) for i in range(len(a))]
        # Count inversions in the transformed array
        # print("detail", detail)
        return count_inversions(diff)


s = Solution()

# Example usage
a = [1, 2, 2, 3, 5]
b = [3, 1, 5, 2, 4]
print(s.pairNumbers(a, b))  # Output should be 2

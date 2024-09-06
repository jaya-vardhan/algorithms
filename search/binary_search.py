class BinarySearch:
       
    def search(self, array, target):
        target_index = -1
        l = 0
        h = len(array) - 1
        while l <= h:
            m = (l + h) // 2
            if array[m] == target:
                target_index = m
                break
            elif target < array[m]:
                h = m - 1
            else:
                l = m + 1
        return target_index


if __name__ == '__main__':
    b = BinarySearch()
    nums = [1, 3, 4, 54, 78]
    t = 1
    res = b.search(nums, t)
    print(res)
 

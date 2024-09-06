class LinearSearch:

    def search(self, array, target):
        target_index = -1
        if array and target:
            for index, val in enumerate(array):
                if val == target:
                    target_index = index
                    break
        return target_index



if __name__ == '__main__':
    l = LinearSearch()
    nums = [2, 3, 4, 54, 78]
    t = 78
    res = l.search(nums, t)
    print(res)
 

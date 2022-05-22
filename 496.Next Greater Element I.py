def nextGreaterElement(nums1, nums2):
    answer = []
    for i in range(0, len(nums1)):
        target = nums1[i]
        if nums2.index(target) == len(nums2):
            answer.append(-1)
        else:
            for j in range(nums2.index(target),len(nums2)):
                if nums2[j] > target:
                    answer.append(nums2[j])
                    break
                elif nums2[j] < target:
                    pass
                if j == len(nums2) - 1:
                    answer.append(-1)
    print(answer)


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
test = nextGreaterElement(nums1, nums2)
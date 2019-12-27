import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_start_pos = 0
        nums1_end_pos = len(nums1) - 1

        nums2_start_pos = 0
        nums2_end_pos = len(nums2) - 1

        while True:
            # when the two arrays are very short, then down grade to get median with sorted array
            # to avoid code complexity in critical conditions
            if nums1_end_pos - nums1_start_pos < 15 and nums2_end_pos - nums2_start_pos < 15:
                merged = sorted(nums1[nums1_start_pos:nums1_end_pos + 1] + nums2[nums2_start_pos:nums2_end_pos + 1])
                median, length_from_start_to_median = self.getMedianInfo(merged, 0, len(merged) - 1)
                return median

            median1, length_from_start_to_median1 = self.getMedianInfo(nums1, nums1_start_pos, nums1_end_pos)

            median2, length_from_start_to_median2 = self.getMedianInfo(nums2, nums2_start_pos, nums2_end_pos)

            # if median of the two array is the same, then return directly 
            if median1 == median2:
                return median1

            # if nothing can be deleted from one of the array, then most of the other array can be deleted from the both sides
            if length_from_start_to_median1 == 0:
                length_from_start_to_median2 = max(length_from_start_to_median2 - 4, 0)
                nums2_start_pos = nums2_start_pos + length_from_start_to_median2
                nums2_end_pos = nums2_end_pos - length_from_start_to_median2
                continue
            elif length_from_start_to_median2 == 0:
                length_from_start_to_median1 = max(length_from_start_to_median1 - 4, 0)
                nums1_start_pos = nums1_start_pos + length_from_start_to_median1
                nums1_end_pos = nums1_end_pos - length_from_start_to_median1
                continue

            # trim numbers from both array
            if median1 > median2:
                # if median of nums1 is larger than median of nums2
                # then right side numbers of nums1's median and left side numbers of nums2's median can be trimmed
                # the length to trim is the smaller number of length_from_start_to_median1 and length_from_start_to_median2
                nums1_end_pos = nums1_end_pos - min(length_from_start_to_median1, length_from_start_to_median2)
                nums2_start_pos = nums2_start_pos + min(length_from_start_to_median1, length_from_start_to_median2)
            elif median1 < median2:
                nums1_start_pos = nums1_start_pos + min(length_from_start_to_median1, length_from_start_to_median2)
                nums2_end_pos = nums2_end_pos - min(length_from_start_to_median1, length_from_start_to_median2)

    def getMedianInfo(self, nums, start_pos, end_pos):
        """
        get median number and length from start position to left median position
        from a array
        given the start position and end position
        """
        half_position = float(start_pos + end_pos) / 2
        left_position = int(math.floor(half_position))
        if half_position - left_position < 0.1:
            median = nums[left_position]
        else:
            median = float(nums[left_position] + nums[left_position + 1]) / 2

        length_from_start_to_median = left_position - start_pos

        return median, length_from_start_to_median

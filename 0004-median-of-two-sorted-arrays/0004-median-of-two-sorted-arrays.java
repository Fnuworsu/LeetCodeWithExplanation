class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        double[] merge = new double[nums1.length + nums2.length];
        int i = 0, j = 0, k = 0, x = (merge.length+1)/2, y = (merge.length/2)+1, z = (merge.length/2);
        while(i < nums1.length && j < nums2.length){
            if(nums1[i] < nums2[j]){
                merge[k++] = nums1[i++];
            }
            else{
                merge[k++] = nums2[j++];
            }
        }
        while(i < nums1.length){
            merge[k++] = nums1[i++];
        }
        while(j < nums2.length){
            merge[k++] = nums2[j++];
        }
        if(merge.length % 2 == 1){
            return merge[x-1];
        }
        else if(merge.length % 2 == 0){
            return (merge[x-1] + merge[y-1])/2;
        }
        return 2;
        
    }
}
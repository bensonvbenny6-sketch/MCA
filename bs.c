
#include <stdio.h>

int binarySearch(int array[], int target, int low, int high) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (array[mid] == target)
            return mid;

        if (array[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}

int main(void) {
    int array[] = {3, 9, 14, 21, 35, 47, 50, 61}; 
    int size = sizeof(array) / sizeof(array[0]);
    int target = 35;

    int result = binarySearch(array, target, 0, size - 1);

    if (result == -1)
        printf("Element is not present in the array.\n");
    else
        printf("Element found at index: %d\n", result);

    return 0;
}


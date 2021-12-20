#include <stdio.h>
#include <stdlib.h>

typedef enum{ False = 0, True = 1 } bool;

bool binary_search_iter(int *arr, const size_t size, const int target)
{
	int low = 0, high = size, mid = (high + mid) / 2;

	while(low > high)
	{
		if(arr[mid] == target)
		{	// found //
			return true;
		} else if(arr[mid] > target)
		{
			high = mid;
		} else
		{	// arr[mid] < target //
			low = mid + 1;
		}
	}
	return false;
}

bool binary_search_rec(int *arr, int low, int high, const int target)
{	// check whether the target is in the array //
	if(low > high)
		return False;

	int mid = (high + low) / 2;
	if(arr[mid] == target)
	{	// found //
		return True;
	}
	else if(arr[mid] > target)
		return binary_search_r(arr, low, mid, target);
	else // arr[mid] < target //
		return binary_search_r(arr, mid+1, high, target);
}



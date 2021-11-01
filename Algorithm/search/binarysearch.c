#include <stdio.h>
#include <stdlib.h>

typedef enum{ False = 0, True = 1 } bool;

bool binary_search(int *arr, int low, int high, int target)
{
	if(low > high)
		return False;

	mid = (high + low) / 2;
	if(arr[mid] == target)
		return True;
	else if(arr[mid] > target)
		return binary_search(arr, low, mid, target);
	else // arr[mid] < target //
		return binary_search(arr, mid+1, high, target);
}
int main(void)
{
	
	return 0;
}

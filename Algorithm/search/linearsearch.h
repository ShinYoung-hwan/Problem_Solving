#include <stdio.h>
#include <stdlib.h>

typedef enum { false, true } bool;

typedef int Data;

bool linearSearch_iter(Data *arr, const size_t size, const Data target)
{
	for(size_t i = 0; i < size; i++)
	{
		if(arr[i] == target)
		{	// found //
			return true;
		}
	}
	// not found //
	return false;
}

bool linearSearch_rec(Data *arr, const int idx, const size_t size, const Data target)
{
	if(arr[idx] == target)
	{	// found //
		return true;
	} else if(idx == size)
	{	// not found //
		return false;
	} else
	{	// to next //
		linearSearch_rec(arr, idx+1, size, target);
	}

}
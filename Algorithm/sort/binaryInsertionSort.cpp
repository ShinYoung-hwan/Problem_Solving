#include <iostream>
#include <vector>

using namespace std;

int binarySearch(const vector<int> array, const int target, int start, int end)
{   /* the time complexity of binary search is O(logN). */
    int mid = (start + end) / 2;
    while(start < end)
    {
        mid = (start + end) / 2;
        if(target > array[mid])
        {
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }

    return start;
}

vector<int> binaryInsertionSort(vector<int> varray)
{
    /* The time complexith is O(N^2) 
     * Because it should have the shift operation N times
     * whether finding the target index is faster or not */

    int len = varray.size();

    for(int i = 0; i < len; i++)
    {
        int target = varray[i];

        int index = binarySearch(varray, target, 0, i - 1);
        cout << index << endl;
        for(int j = i - 1; j >= index; j--)
        {
            varray[j + 1] = varray[j];
        }
        varray[index] = target;
    }
    return varray;
}

void printElements(vector<int> &array)
{
    for(auto element : array)
    {
        cout << element << ' ';
    }    
    cout << endl;
}

int main(void)
{
    vector<int> before = {1, 5, 3, 7, 9, 6, 5, 4, 5};

    cout << "Before address:\t" << &before << endl;
    cout << "Before:\t";
    printElements(before);

    vector<int> after = before; /* DeepCopy */
    cout << "After address:\t" << &after << endl;
    cout << "After:\t";
    after = binaryInsertionSort(after);
    printElements(after);

    cout << "Answer:\t1 3 4 5 5 5 6 7 9" << endl;

    return 0;
}
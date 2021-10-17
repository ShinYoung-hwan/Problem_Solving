#include <iostream>
#include <vector>

using namespace std;

vector<int> insertionSort(vector<int> array)
{
    /* the time complexity is O(N^2) */
    
    int len = array.size();

    for(int i = 0; i < len; i++)
    {
        int target = array[i];
        for(int j = i - 1; j >= 0; j--)
        {   
            if(target > array[j])
            {
                array[j + 1] = target;
                break;
            }
            else
            {
                array[j + 1] = array[j];
            }
        }
    }

    return array; /* After sort */
}

void printElements(const vector<int> &array)
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
    after = insertionSort(after);
    printElements(after);
    
    cout << "Answer:\t1 3 4 5 5 5 6 7 9" << endl;

    return 0;
}
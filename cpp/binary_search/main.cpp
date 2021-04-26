#include <iostream>
#include <vector>
using namespace std;

int binary_search(vector<int> arr, int start, int end, int x)
{   
    if ( end < start)
        return -1;

    int mid = (start + end) / 2;

    if ( arr[mid] == x)
        return mid;
    if (arr[mid] < x)
        return binary_search(arr, mid+1, end, x);
    if (arr[mid] > x)
        return binary_search(arr, start, mid-1, x);
}

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int start = 0;
    int end = arr.size();
    int find = 11;

    int rv = binary_search(arr, start, end, find);
    if (rv == -1)
        cout << "Not found, exiting" << endl;
        return rv;
    cout << "Value has been found at index: " << rv << endl;
    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;


// 1. Base Class for Sorting Algorithms
template <typename T>
class SortAlgoritm{
    public:
        virtual void sort(vector<T>& data) =0; // pure virtual function
        virtual ~SortAlgoritm() = default; // virtual destructor for cleanup
};

// 2. Bubble Sort Implementation
template <typename T>
class BubbleSort : public SortAlgoritm<T>{
    public:
        void sort(vector<T>& data) override {
            for (size_t i = 0; i < data.size() -1; ++i){
                for (size_t j = 0; j < data.size() -i -1; ++j){
                    if (data[j] > data[j+1]){
                        swap(data[j], data[j+1]);
                    }
                }
            }
        }
};

// 3. Insertion Sort Implementation
template <typename T>
class InsertionSort : public SortAlgoritm<T>{
    public: 
        void sort(vector<T>& data) override{
            for (size_t i = 1; i < data.size(); ++i){
                T key = data[i];
                size_t j = i-1;
                while(j >= 0 && data[j] > key){
                    data[j+1] = data[j];
                    --j;
                }
                data[j+1] = key;
            }
        }
};


// 4. Merge Sort Implementation
template <typename T>
class MergeSort : public SortAlgoritm<T>{
    private:
        void merge(vector<T>& data, int left, int mid, int right){
            /*
The constructor is called with two iterators:
data.begin() + left: This is the starting iterator pointing to the element 
at index left in the data vector.
data.begin() + mid + 1: This is the ending iterator pointing just past
the element at index mid, effectively including the element at index mid 
in the new vector.            
            */
            vector<T> leftvec(data.begin()+left, data.begin()+mid + 1);
            vector<T> rightvec(data.begin()+mid+1, data.begin()+right+1);

            size_t i= 0, j =0, k =left;
            while(i < leftvec.size() && j < rightvec.size()) {
                if (leftvec[i] <= rightvec[j]){
                    data[k++] = leftvec[i++];
                } else {
                    data[k++] = rightvec[j++];
                }
            }
            while (i < leftvec.size()){
                data[k++] = leftvec[i++];
            }
            while (j < rightvec.size()){
                data[k++] = rightvec[j++];
            }
        }

        void mergeSortHelper(vector<T>& data, int left, int right){
            if (left < right){
                int mid = left + (right - left) / 2;
                mergeSortHelper(data, left, mid);
                mergeSortHelper(data, mid+1, right);
                merge(data, left, mid, right);
            }
        }

    public:
        void sort(vector<T>& data) override {
            mergeSortHelper(data, 0, data.size()-1);
        }
};

// 5. Quick Sort Implementation
template <typename T>
class QuickSort : public SortAlgoritm<T>{
    private:
        int partition(vector<T>& data, int low, int high){
            T pivot = data[high];
            int i = low -1;
            for (int j = low; j < high; ++j){
                if (data[j] < pivot){
                    ++i;
                    swap(data[i], data[j]);
                }
            }
            swap(data[i+1], data[high]);
            return i+1;
        }
        void quickSortHelper(vector<T>& data, int low, int high){
            if (low < high){
                int pi = partition(data, low, high);
                quickSortHelper(data, low, pi-1);
                quickSortHelper(data, pi+1, high);
            }
        }
    public:
        void sort(vector<T>& data) override{
            quickSortHelper(data, 0, data.size() -1);
        }
};


int main() {
    // Your code for MergeSort goes here.
    cout << "Running Sort algorithm." << endl;

    std::vector<int> data = {64, 34, 25, 12, 22, 11,23,12,54544,33,33,33, 90};

    SortAlgoritm<int>* sorter = new QuickSort<int>();
    sorter->sort(data);

    std::cout << "Sorted data: ";
    for (const auto& num : data) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    delete sorter; // Clean up
    

    return 0;
}

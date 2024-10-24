#include <iostream>
#include <vector>
#include <algorithm>
#include <optional>

using namespace std;


class BinarySearch{
    private:
        vector<int> data_;
    public:
        BinarySearch(vector<int> data) : data_{move(data)}{
            sort(data_.begin(), data_.end()); // sort the data
        }
        // Method to perform binary search
        optional<int> search(int target) const{
            int left =0;
            int right = static_cast<int>(data_.size() -1);

            while (left <= right)
            {
                /* code */
                int mid = left + (right - left) / 2;
                if(data_[mid] == target ){
                    return mid; //return the index of the target
                } else if (data_[mid] < target){
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            return nullopt; // target not found
        }
        void display() const{
            for (const auto& num : data_){
                cout << num << " ";
            }
            cout << endl;
        }
};

int main() {
    // Your code for BinarySearch goes here.
    cout << "Running BinarySearch algorithm." << endl;

    vector<int> arr{40,63,12,3,76,11,10,0,21,32};
    BinarySearch ourArray(arr); // create binary search obj

    ourArray.display(); //displying sorted data


    int target{10};
    auto result = ourArray.search(target);
    if (result){
        std::cout << "Element is present at index " << *result << std::endl;
    }else {
        std::cout << "Element is not present in the array" << std::endl;
    }
    
    return 0;

}

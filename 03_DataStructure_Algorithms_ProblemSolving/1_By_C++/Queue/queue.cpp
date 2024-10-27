#include <iostream>
#include <stack>
#include <list>
#include <unordered_map>

using namespace std;

/*
In C++, a stack is a data structure that operates on a 
Last-In-First-Out (LIFO) principle, where the last element 
added is the first to be removed. The C++ Standard Library 
provides a stack container in the <stack> header, which is
 part of the Standard Template Library (STL). Here’s an
  overview of how to use it, including key operations 
  like push, pop, top, and empty.
*/

// 5. Implement a Queue using Stacks
class MyQueue{
    private:
        stack<int> s1,s2;
    public:
        void push(int x){
            s1.push(x);
        }

        int pop(){
            if (s2.empty()){ // pushing --> s1
                while(!s1.empty()){
                    /*
By moving each element from s1 to s2, the order of elements is reversed. 
This reversal means the oldest element (the bottom of s1) is now at the 
top of s2, so s2.top() effectively becomes the oldest element in our queue.                    
                    */
                    s2.push(s1.top());
                    s1.pop();
                }
            }
            int res = s2.top();
            s2.pop();
            return res; 
        }
        int peek(){
            if (s2.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.top());
                    s1.pop();
                }
            }
            return s2.top();            
        }
        bool empty(){
            return s1.empty() && s2.empty();
        }
};


/*
The Least Recently Used (LRU) Cache is a popular caching algorithm 
that discards the least recently used items first. The goal of an 
LRU cache is to keep a limited number of items, ensuring that the 
most frequently accessed items remain available while the least 
accessed ones are removed when space is needed. 
*/
// 6. LRU Cache Implementation
class LRUCache{
    list<int> lru;
    unordered_map<int, pair<int, list<int>::iterator>> cache;
    int capacity;
    public:
    LRUCache(int capacity) : capacity(capacity){}
    int get(int key){
        if(cache.find(key) == cache.end()) return -1; // If the key is not found, it returns -1, indicating that the item is not in the cache.
        lru.erase(cache[key].second);
        /*
In your LRUCache implementation, cache[key] is a pair consisting 
of two elements:
    The value associated with the key.
    An iterator pointing to the key's position in the lru list.        
        */
        lru.push_front(key);
        cache[key].second = lru.begin();
        return cache[key].first;
    }
    void put(int key, int value){
        if (cache.find(key) != cache.end()){
            lru.erase(cache[key].second);
        }else if (lru.size() == capacity){
            cache.erase(lru.back());
            lru.pop_back();
        }
        lru.push_front(key);
        cache[key] = {value, lru.begin()};
    }
};




int main() {
    // Your code for QuickSort goes here.
    cout << "Running Queue." << endl;
   MyQueue queue;

    // Performing queue operations
    cout << "Running Queue Operations:" << endl;

    // Push elements into the queue
    queue.push(1);
    queue.push(2);
    queue.push(3);
    
    cout << "Peek: " << queue.peek() << endl; // Should print 1

    cout << "Pop: " << queue.pop() << endl; // Should print 1
    cout << "Pop: " << queue.pop() << endl; // Should print 2

    // Check if queue is empty
    cout << "Is the queue empty? " << (queue.empty() ? "Yes" : "No") << endl; // Should print No

    // Push another element
    queue.push(4);
    cout << "Peek: " << queue.peek() << endl; // Should print 3
    cout << "Pop: " << queue.pop() << endl; // Should print 3
    cout << "Pop: " << queue.pop() << endl; // Should print 4

    // Final check if the queue is empty
    cout << "Is the queue empty? " << (queue.empty() ? "Yes" : "No") << endl; // Should print Yes

///////////////////////////////////////////////////////////////////////////
    cout << "LRU " << endl;
       // Create an LRUCache with a capacity of 3
    LRUCache cache(3);

    // Put some values in the cache
    cache.put(1, 100); // Cache: {1: 100}
    cache.put(2, 200); // Cache: {1: 100, 2: 200}
    cache.put(3, 300); // Cache: {1: 100, 2: 200, 3: 300}

    // Access some values
    cout << "Get 1: " << cache.get(1) << endl; // Returns 100, Cache: {2: 200, 3: 300, 1: 100}
    cout << "Get 2: " << cache.get(2) << endl; // Returns 200, Cache: {3: 300, 1: 100, 2: 200}

    // Add a new key-value pair, which will evict the least recently used key (3)
    cache.put(4, 400); // Cache: {1: 100, 2: 200, 4: 400}

    // Try to access the evicted key
    cout << "Get 3: " << cache.get(3) << endl; // Returns -1 (not found)

    // Access existing key
    cout << "Get 1: " << cache.get(1) << endl; // Returns 100, Cache: {2: 200, 4: 400, 1: 100}

    // Add another key-value pair, which will evict the least recently used key (2)
    cache.put(5, 500); // Cache: {4: 400, 1: 100, 5: 500}

    // Access the evicted key
    cout << "Get 2: " << cache.get(2) << endl; // Returns -1 (not found)
    
    // Access remaining keys
    cout << "Get 4: " << cache.get(4) << endl; // Returns 400
    cout << "Get 5: " << cache.get(5) << endl; // Returns 500



    return 0;
}

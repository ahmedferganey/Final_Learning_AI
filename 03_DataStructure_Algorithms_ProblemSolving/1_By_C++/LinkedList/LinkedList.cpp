#include <iostream>

using namespace std;


/*
1. Reverse a Linked List
Given a singly linked list, reverse it and return the reversed list.

2. Detect a Cycle in a Linked List
Determine if a linked list has a cycle in it. Use Floyd’s Cycle Detection algorithm.

3. Merge Two Sorted Linked Lists
Merge two sorted linked lists and return it as a new sorted list.

4. Find the Middle of a Linked List
Given a linked list, find the middle node. If there are two middle nodes, return the second one.

5. Implement a Queue using Stacks
Use two stacks to implement a queue. Support standard queue operations like enqueue, dequeue, and peek.

*/



struct ListNode{
    int val;
    ListNode *next;
    // constructor to initilize the node
    ListNode(int x) : val(x), next(nullptr){}
    // member function to display the node is value
    void display() const{
        cout << "value: " << val << endl;
    }
};

ListNode* reverseList(ListNode* head){
/*
input  : 1 → 2 → 3 → 4 → nullptr  // 1 is the head of the list,
output : 4 → 3 → 2 → 1 → nullptr
*/    
    ListNode *prev = nullptr, *curr = head;
    while (curr)
    {
        /* code */
        ListNode *nextTemp = curr->next; // Store the next node
        curr->next = prev; // Reverse the current node's pointer
        prev = curr;  // Move prev to current node
        curr = nextTemp; // Move to the next node
    }
    return prev; // prev becomes the new head of the reversed list
}

// helper function to print the linked list
void printList(ListNode* head){
    while (head){
        cout << head->val << " → ";
        head = head->next;
    }
    cout << "nullptr" << endl;
}

// 2. Detect a Cycle in a Linked List
/*
In a linked list, if a cycle exists, it means that there 
is no end to the list because one of the nodes points back 
to a previous node instead of pointing to nullptr.
*/
// Floyd's Cycle Detection Algorithm (Tortoise and Hare).
bool hasCycle(ListNode* head){
    ListNode* slow =head, *fast = head;
    while(fast && fast->next){ //This prevents accessing nullptr and avoids crashes when fast or fast->next reaches the end of a non-cyclic list.
        slow = slow->next;         // Move slow pointer one step
        fast = fast->next->next;   // Move fast pointer two steps
        if (slow == fast) return true;
        /*
        Example 2: Cyclic List 1 → 2 → 3 → 4 → 2 ...
        Iteration 1: slow at 1, fast at 1
        Iteration 2: slow moves to 2, fast moves to 3
        Iteration 3: slow moves to 3, fast moves to 2 (due to the cycle)
        Iteration 4: slow moves to 4, fast moves to 4
        Since slow and fast meet, we return true (cycle detected).
        */

    }
    return false;
}

// 3. Merge Two Sorted Linked Lists
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
    if (!l1) return l2;
    if (!l2) return l1;

    if(l1->val < l2->val){
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    }else{
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }

}


// 4. Find the Middle of a Linked List
ListNode* middleNode(ListNode* head){
    ListNode *slow = head, *fast = head;
    /*
        slow moves one step at a time.
        fast moves two steps at a time.
        When fast reaches the end of the list, slow will be positioned at the middle node.    
     */
    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

int main() {
    // Your code for LinkedList goes here.
    cout << "Running LinkedList algorithm." << endl;
    // Testing all the linked list functions

    // 1. Reverse a Linked List
    ListNode* head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);

    cout << "Original List: ";
    printList(head1);

    ListNode* reversedHead = reverseList(head1);
    cout << "Reversed List: ";
    printList(reversedHead);

    // 2. Detect a Cycle in a Linked List
    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);
    head2->next->next = new ListNode(3);
    head2->next->next->next = new ListNode(4);
    head2->next->next->next->next = head2->next;  // Create a cycle

    cout << "Has Cycle (Expected: 1): " << hasCycle(head2) << endl;

    // 3. Merge Two Sorted Linked Lists
    ListNode* l1 = new ListNode(1);
    l1->next = new ListNode(3);
    l1->next->next = new ListNode(5);

    ListNode* l2 = new ListNode(2);
    l2->next = new ListNode(4);
    l2->next->next = new ListNode(6);

    ListNode* mergedHead = mergeTwoLists(l1, l2);
    cout << "Merged Sorted List: ";
    printList(mergedHead);

    // 4. Find the Middle of a Linked List
    ListNode* head3 = new ListNode(1);
    head3->next = new ListNode(2);
    head3->next->next = new ListNode(3);
    head3->next->next->next = new ListNode(4);
    head3->next->next->next->next = new ListNode(5);

    ListNode* middle = middleNode(head3);
    cout << "Middle Node Value (Expected: 3): " << middle->val << endl;

    // Cleanup (only on non-cyclic lists)
    delete head1;
    delete head3;
    delete mergedHead;
    delete head2;  // head2 contains a cycle, so we can't delete it safely here

    return 0;
}

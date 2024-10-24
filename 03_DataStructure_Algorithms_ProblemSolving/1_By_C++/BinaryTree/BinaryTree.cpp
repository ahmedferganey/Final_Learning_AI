#include <iostream>
#include <memory>

using namespace std;

// 1. Binary Search Tree (BST)
class BSTNode {
public:
    int Key;  // The value stored in the node
    std::unique_ptr<BSTNode> left;  // Pointer to the left child node
    std::unique_ptr<BSTNode> right;  // Pointer to the right child node

    // Constructor to initialize a node with a given value
    BSTNode(int value) : Key(value), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
public:
    std::unique_ptr<BSTNode> root;  // Pointer to the root node of the BST

    // Public method to insert a new key into the BST
    void insert(int key) {
        root = insertRec(std::move(root), key);  // Insert and update root
    }

    // Public method to perform inorder traversal of the BST
    void inorder() const {
        inorderRec(root.get());  // Start traversal from the root
    }

private:
    // Private recursive function to insert a new key into the BST
    std::unique_ptr<BSTNode> insertRec(std::unique_ptr<BSTNode> node, int key) {
        if (!node) {
            return std::make_unique<BSTNode>(key);  // Create a new node if the current position is empty
        }
        // Recursively insert into the left or right subtree based on the key value
        if (key < node->Key) {
            node->left = insertRec(std::move(node->left), key);  // Move ownership of left child
        } else {
            node->right = insertRec(std::move(node->right), key);  // Move ownership of right child
        }
        return node;  // Return the (possibly unchanged) node
    }

    // Private recursive function to perform inorder traversal
    void inorderRec(BSTNode* node) const {
        if (node) {
            inorderRec(node->left.get());  // Visit left subtree
            std::cout << node->Key << " ";  // Visit the current node
            inorderRec(node->right.get());  // Visit right subtree
        }
    }
};


int main() {
    // Your code for BinaryTree goes here.
    cout << "Running Binary Search Tree (BST), a Balanced Binary Search Tree (AVL Tree), and a Binary Tree Map" << endl;
    
        // 1. Binary Search Tree (BST)
     cout << "Running Binary Search Tree (BST)" << endl;
     BinarySearchTree bst;
     bst.insert(10);
    bst.insert(10);
    bst.insert(5);
    bst.insert(15);
    bst.insert(3);
    bst.insert(7);

    std::cout << "Inorder Traversal of BST: ";
    bst.inorder();
    std::cout << std::endl;         

    
    return 0;
}

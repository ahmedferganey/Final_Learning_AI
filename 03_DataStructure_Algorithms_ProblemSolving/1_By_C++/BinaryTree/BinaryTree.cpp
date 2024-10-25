#include <iostream>
#include <memory>
#include <vector>
#include <string>

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

// Method to insert elements from a vector
    void insertFromVector(const vector<int>& values) {
        for (int value : values){
            insert(value);
        }
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



// 2. Balanced Binary Search Tree (AVL Tree)
class AVLNode{
    public:
        int key;
        unique_ptr<AVLNode> left;
        unique_ptr<AVLNode> right;
        int height;
        AVLNode(int value) : key(value), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree{
    public:
        unique_ptr<AVLNode> root;
        void insert(int key){
            root = insertRec(move(root), key);
        }

        void insertFromVector(const std::vector<int>& values) {
            for (int value : values) {
                insert(value);
            }
        }

        void inorder() const {
            inorderRec(root.get());
        }

    private:
        int height(AVLNode* node){
            return node ? node->height: 0;
        }

        int balanceFactor(AVLNode* node){
            return height(node->left.get()) - height(node->right.get());
        }

        unique_ptr<AVLNode> rotateRight(unique_ptr<AVLNode> y){
            // Step 1: Identify the left child of y, which will become the new root (x)
            auto x = std::move(y->left);  // Move y's left child to x

            // Step 2: Temporarily store the right child of x (T2)
            auto T2 = std::move(x->right); // Move x's right child to T2

            // Step 3: Perform the rotation
            x->right = std::move(y);  // Set y as the right child of x

            // Step 4: Attach T2 as the left child of y
            x->right->left = std::move(T2); // Reattach T2 to y as its left child
            
            // Step 5: Update heights
            x->right->height = max(height(x->right->left.get()), height(x->right->right.get())) + 1;
            x->height = max(height(x->left.get()), height(x->right.get())) + 1;

            // Step 6: Return the new root of the subtree (x)
            return x;  // x is the new root after rotation           
        }

        unique_ptr<AVLNode> rotateLeft(unique_ptr<AVLNode> x){
            auto y = move(x->right);
            auto t2 = move(y->left);
            y->left = move(x);
            y->left->right = move(t2);
            y->left->height = max(height(y->left->left.get()), height(y->left->right.get())) +1 ;;
            y->height = max(height(y->left.get()), height(y->right.get())) + 1;;
            return y;
        }
        unique_ptr<AVLNode> insertRec(unique_ptr<AVLNode> node, int key){
            if (!node){
                return make_unique<AVLNode>(key);
            }
            if (key < node->key){
                node->left = insertRec(move(node->left), key);
            } else {
                node->right = insertRec(move(node->right), key);
            }
            node->height = 1 + max(height(node->left.get()), height(node->right.get()));

            int balance = balanceFactor(node.get()); //node->left.get() -node->right.get()
            /*
The balance factor is greater than 1, indicating that the left 
subtree is taller than the right subtree.            
            */
            // left left case
            if (balance > 1 && key < node->left->key){
                return rotateRight(move(node));
                /*
The newly inserted key is less than the key of the left child of 
the current node, which means that the insertion occurred in the 
left subtree of the left child.                
                */
            }
            
            // right right case   
            if (balance < -1 && key > node->right->key){
                return rotateLeft(move(node));
            }

            // right left case 
            if (balance < -1 && key < node->right->key){
                node->right = rotateRight(move(node->right));
                return rotateLeft(move(node));
                /*
First, perform a right rotation on the right child (node->right). 
This reduces the height of the right subtree.
After this, perform a left rotation on the current node (node),
which brings the new root from the first rotation into the place of the current node.                
                */
            }
      
            // Left Right Case
            if (balance > 1 && key > node->left->key) {
                node->left = rotateLeft(std::move(node->left));
                return rotateRight(std::move(node));
            }            
            return node;
        }

        void inorderRec (AVLNode* node) const {
            if (node){
                inorderRec(node->left.get());
                cout << node->key << " ";
                inorderRec(node->right.get());
            }
        }
        
};


// 3. Binary Tree Map
class TreeNode{
    public:
        string key;
        string value;
        unique_ptr<TreeNode> left;
        unique_ptr<TreeNode> right;

        TreeNode(string k , string v) : key(move(k)), value(move(v)), left(nullptr), right(nullptr) {}
};

class BinaryTreeMap{
    public:
        unique_ptr<TreeNode> root;

        void insert(const string& key, const string& value){
            root = insertRec(move(root), key, value);
        }

        void insertFromVector(const vector<pair<string, string>>& values){
            for (const auto& [key, value] : values) {
                insert(key, value);
            }
        }

        string find(const string& key) const {
            return findRec(root.get(), key);
        }

        void inorder() const {
            inorderRec(root.get());
        }

    private:
        unique_ptr<TreeNode> insertRec(unique_ptr<TreeNode> node, const string& key, const string& value){
            if (!node){
                return make_unique<TreeNode>(key, value);
            }  
            if (key < node->key) {
                node->left = insertRec(std::move(node->left), key, value);
            } else {
                node->right = insertRec(std::move(node->right), key, value);
            }
            return node;         
        }

        string findRec(TreeNode* node, const string& key) const {
            if (!node){
                return "not found";
            }
            if (key == node->key){
                return node->value;
            }
            return key < node->key ? findRec(node->left.get(), key) : findRec(node->right.get(), key);
        }

        void inorderRec(TreeNode* node) const{
            if (node){
                inorderRec(node->left.get());
                cout << node->key << ": " << node->value << endl;
                inorderRec(node->right.get());
            }
        }

};





int main() {
    // Your code for BinaryTree goes here.
    cout << "Running Binary Search Tree (BST), a Balanced Binary Search Tree (AVL Tree), and a Binary Tree Map" << endl;
    
////////////////////////////////////////////////////////////////////////////////
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

    // std::vector<int> values = {10, 5, 15, 3, 7};
    // bst.insertFromVector(values);

////////////////////////////////////////////////////////////////////////////////

    // 2. Balanced Binary Search Tree (AVL Tree)
    AVLTree avl;
    std::vector<int> values_AVL = {10, 20, 30, 40, 50, 25};
    
    avl.insertFromVector(values_AVL);

    std::cout << "Inorder Traversal of AVL Tree: ";
    avl.inorder();
    std::cout << std::endl;

////////////////////////////////////////////////////////////////////////////////
// 3. Binary Tree Map
    BinaryTreeMap map;
    vector<pair<string, string>> values = {
        {"ahmed", "mariam"},
        {"ali", "noha"},
        {"mohamed", "kholoud"},
        {"maher", "salwa"},
        {"nor", "ola"}
    };

    map.insertFromVector(values);

    std::cout << "Inorder Traversal of Binary Tree Map: " << std::endl;
    map.inorder();

    
    return 0;
}

#include <iostream>
#include <vector>
using namespace std;

struct Node
{
    int data;
    struct Node *left, *right;
};

bool iterativeSearch(struct Node* root, int key)
{
    cout << "Key is " << key << endl;
    while (root != NULL)
    {
        cout << "\nPassing node " << root->data << endl;
        if (root->right)
            cout << "Node right is " << root->right->data << endl;
        if (root->left)
            cout << "Node left is " << root->left->data << endl;
        
        if (key > root->data)
            root = root->right;
        else if (key < root->data)
            root = root->left;
        else
            return true;
    }
    return false;
}

struct Node* createNode(int data)
{
    struct Node* newNode = new Node;
    newNode->data = data;
    newNode->right = NULL;
    newNode->left = NULL;
    return newNode;
}

struct Node* insertNode(Node* node, int data)
{
    if (node == NULL)
        return createNode(data);
    if (data < node->data)
        node->left = insertNode(node->left, data);
    else if (data > node->data)
        node->right = insertNode(node->right, data);
    
    return node;
}

int main()
{
    /* Basic tree outline
              80
            /    \
          40      90
         /  \       \
       30   50       100
      /  \    \
     10   20   60*/
    struct Node* root = NULL;
    root = insertNode(root, 80);
    insertNode(root, 40);
    insertNode(root, 30);
    insertNode(root, 50);
    insertNode(root, 90);
    insertNode(root, 60);
    insertNode(root, 100);
    insertNode(root, 10);
    insertNode(root, 20);

    vector<int> list;
    if (iterativeSearch(root, 20))
        cout << "Search data found." << endl;
    else
        cout << "Search data not found." << endl;
    return 0;
}
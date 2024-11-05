#include <iostream>
using namespace std;

// Node structure for the linked list
struct Node {
    int data;
    Node* next;
};

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = nullptr;
    return newNode;
}

// Function to insert a node at the beginning of the list
void insertAtBeginning(Node*& head, int data) {
    Node* newNode = createNode(data);
    newNode->next = head;
    head = newNode;
}

// Function to insert a node at the end of the list
void insertAtEnd(Node*& head, int data) {
    Node* newNode = createNode(data);
    if (head == nullptr) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// Function to delete a node with a given key
void deleteNode(Node*& head, int key) {
    Node* temp = head;
    Node* prev = nullptr;

    // If head node itself holds the key to be deleted
    if (temp != nullptr && temp->data == key) {
        head = temp->next; // Change head
        delete temp; // Free old head
        return;
    }

    // Search for the key to be deleted
    while (temp != nullptr && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If key was not found
    if (temp == nullptr) return;

    // Unlink the node from the list
    prev->next = temp->next;
    delete temp; // Free memory
}

// Function to display the linked list
void displayList(Node* head) {
    Node* temp = head;
    cout << "Linked list: ";
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

// Predefined input to initialize the linked list
void initializeList(Node*& head) {
    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);
    insertAtEnd(head, 40);
    insertAtEnd(head, 50);
}

int main() {
    Node* head = nullptr;

    // Initialize the linked list with predefined input
    initializeList(head);

    // Display the initial list
    cout << "Initial ";
    displayList(head);

    // Perform some operations
    cout << "\nInserting 5 at the beginning:\n";
    insertAtBeginning(head, 5);
    displayList(head);

    cout << "\nInserting 60 at the end:\n";
    insertAtEnd(head, 60);
    displayList(head);

    cout << "\nDeleting node with value 30:\n";
    deleteNode(head, 30);
    displayList(head);

    cout << "\nDeleting node with value 5 (beginning):\n";
    deleteNode(head, 5);
    displayList(head);

    cout << "\nDeleting node with value 60 (end):\n";
    deleteNode(head, 60);
    displayList(head);

    return 0;
}

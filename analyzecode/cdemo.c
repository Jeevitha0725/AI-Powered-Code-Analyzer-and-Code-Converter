#include <stdio.h>
#include <stdlib.h>

// Node structure for the linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node with given data
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the beginning of the list
void insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Function to insert a node at the end of the list
void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// Function to delete a node with given key
void deleteNode(struct Node** head, int key) {
    struct Node *temp = *head, *prev = NULL;

    // If head node itself holds the key to be deleted
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }

    // Search for the key to be deleted
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If key was not found
    if (temp == NULL) return;

    // Unlink the node from the list
    prev->next = temp->next;
    free(temp);
}

// Function to display the linked list
void displayList(struct Node* head) {
    struct Node* temp = head;
    printf("Linked list: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Predefined input to initialize the linked list
void initializeList(struct Node** head) {
    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);
    insertAtEnd(head, 40);
    insertAtEnd(head, 50);
}

int main() {
    struct Node* head = NULL;

    // Initialize the linked list with pre-built input
    initializeList(&head);

    // Display the initial list
    printf("Initial ");
    displayList(head);

    // Perform some operations
    printf("\nInserting 5 at the beginning:\n");
    insertAtBeginning(&head, 5);
    displayList(head);

    printf("\nInserting 60 at the end:\n");
    insertAtEnd(&head, 60);
    displayList(head);

    printf("\nDeleting node with value 30:\n");
    deleteNode(&head, 30);
    displayList(head);

    printf("\nDeleting node with value 5 (beginning):\n");
    deleteNode(&head, 5);
    displayList(head);

    printf("\nDeleting node with value 60 (end):\n");
    deleteNode(&head, 60);
    displayList(head);

    return 0;
}

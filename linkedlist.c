#include <stdio.h>
#include <stdio.h>

typedef struct node {
    int data:
    struct node* next;
}Node;

Node* CreateNewNode(int data)
{
    Node* newNode =(Node*) malloc(sizeof(Node));

    if (newNode == NULL)
    {
        printf("Failed to allocate memory!");
        return NULL;
    }

    newNode->data;
    newNode->NULL;
    return newNode;
}

int main()
{
    printf("\n Singly linked list demo!\n");

    Node* newNode = CreateNewNode(1);
}
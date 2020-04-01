#include <stdlib.h>
#include <stdio.h>

// Define a node in the list with a variable for the value and a struct pointer that points to the next node

typedef struct node {

    int value;
    struct node* next;

}node_t;


// function to print out the linked list

void printLinkedList(node_t *head){
    node_t *temporary = head;
    while(temporary != NULL){
        printf("%d - ", temporary -> value);
        temporary = temporary -> next;
    }
    printf("\n");
}

void main(){
    node_t n1, n2, n3;
    node_t *head;

    n1.value = 45;
    n2.value = 8;
    n3.value = 32;

    // link up the nodes

    head = &n3;
    n3.next = &n2;
    n2.next = &n1;
    n1.next = NULL; // so we know when to stop

    printLinkedList(head);
}
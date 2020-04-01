#include <stdlib.h>
#include <stdio.h>

// Define a node in the list with a variable for the value and a struct pointer that points to the next node

typedef struct node {

    int value;
    struct node *next;

}node_t;


// function to print out the linked list

void printLinkedList(node_t *head){
    node_t *temporary = head;
    while(temporary != NULL){
        if(temporary->next != NULL){
            printf("%d -> ", temporary -> value);
            temporary = temporary -> next;
        }
        else{
            printf("%d", temporary -> value);
            temporary = temporary -> next;
        }
    }
    printf("\n");
}

void main(){
    node_t n1, n2, n3, n4;
    node_t *head;

    n1.value = 45;
    n2.value = 8;
    n3.value = 32;
    n4.value = 50;

    // link up the nodes

    head = &n2;
    n3.next = &n4;
    n2.next = &n1;
    n1.next = &n3; // so we know when to stop
    n4.next = NULL;
    printLinkedList(head);
}
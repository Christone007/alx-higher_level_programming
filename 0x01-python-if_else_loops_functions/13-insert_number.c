#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: The head of the list
 * @number: The number to insert
 *
 * Return: The address of the new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *newnode, *ptr;

        ptr = *head;

        if (ptr == NULL)
                return (NULL);

        newnode = malloc(sizeof(listint_t));
        if (newnode == NULL)
                return NULL;
        newnode->n = number;
        newnode->next = NULL;

        if(ptr->n >= number)
        {
                newnode->next = ptr;
                head = &newnode;
                return (newnode);
        }

        while (ptr->next != NULL)
        {
                if (ptr->next->n >= number)
                {
                        newnode->next = ptr->next;
                        ptr->next = newnode;
                        return (newnode);
                }

                ptr = ptr->next;
        }

        ptr->next = newnode;
        return (newnode);
}

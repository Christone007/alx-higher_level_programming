#include <stdlib.h>
#include "lists.h"


/**
 * check_cycle - Checks if a singly linked list contains a cycle
 * @list: - the head of the list
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
    listint_t *hare;
    listint_t *tortoise;

    hare = list;
    tortoise = list;

    if (hare == NULL || hare->next == NULL)
        return (0);

    if (list->next == list || list->next->next == list)
        return (1);
    
    while (hare != NULL && hare->next != NULL)
    {
        hare = hare->next->next;
        tortoise = tortoise->next;

        if (hare == NULL)
            return (0);

        if (hare == tortoise)
            return (1);
    }

    return (0);
}

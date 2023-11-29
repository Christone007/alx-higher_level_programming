#include "lists.h"

/**
 * check_cycle - Checks if a list contains a cycle
 * @list: The head of the list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;

	/* if list has only one item cycling */
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}


	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}

	return (0);
}

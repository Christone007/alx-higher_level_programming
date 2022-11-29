#include "lists.h"

/**
 * check_cycle - Checks if a list has a cycle in it
 * list: The head of a list
 *
 * Return: an integer, 0 (no cycle), 1(cycle found)
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

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
		{
			return (1);
		}
	}

	return (0);
}

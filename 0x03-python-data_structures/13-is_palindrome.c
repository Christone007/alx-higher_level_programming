#include "lists.h"

/**
 * count_listint - Counts the number of nodes in a singly linked list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t count_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}


/**
 * is_palindrome - Checks if a list is a palindrome
 * @head: The head of the list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome or empty
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2;
	size_t counter, i, j;

	i = 0;
	j = 0;

	p1 = p2 = *head;
	counter = count_listint(p1);

	while (i != counter / 2)
	{
		p1 = p2 = *head;
		for (j = 0; j < i; j++)
		{
			p1 = p1->next;
		}
		for (j = 0; j < counter - (i + 1); j++)
		{
			p2 = p2->next;
		}
		if (p1->n != p2->n)
		{
			return 0;
		}
		else
		{
			i++;
		}
	}

	return 1;
}

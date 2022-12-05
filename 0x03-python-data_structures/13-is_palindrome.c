#include "lists.h"

/**
 * count_listint - prints all elements of a listint_t list
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
	size_t count, i;

	p1 = *head;
	p2 = *head;
	count = count_listint(p1);

	if (count == 0)
		return (1);

	while (p1 != NULL)
	{
		for (i = 1; i < count; i++)
		{
			p2 = p2->next;
		}

		if (p1->n == p2->n)
		{
			p1 = p1->next;
			count--;
			p2 = *head;
		}
		else
		{
			return (0);
		}
	}

	return (1);
}

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
	listint_t *newnode, *start;

	start = *head;

	if (start == NULL)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return NULL;

	newnode->n = number;
	newnode->next = NULL;


	if (start->next == NULL)
	{
		start->next = newnode;
		return (newnode);
	}

	while (start->next != NULL)
	{
		if (start->next->n >= number)
		{
			newnode->next = start->next;
			start->next = newnode;
			return (newnode);
		}

		start = start->next;
	}

	start->next = newnode;
	return (newnode);
}

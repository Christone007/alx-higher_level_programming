#include "lists.h"

/**
 * is_palindrome - Checks if a list is a palindrome
 * @head: The head of the list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome or empty
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1); // An empty list or a single node is considered a palindrome

    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

    // Use two pointers to find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list while finding the middle
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // Adjust pointers for odd/even length lists
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
            return (0); // Not a palindrome

        prev = prev->next;
        slow = slow->next;
    }

    return (1); // Palindrome
}

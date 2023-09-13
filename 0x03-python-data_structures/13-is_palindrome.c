#include "lists.h"
/**
 * is_palindrome - a fuction that checks if a list is palindrome
 * @head: the head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j, n;
	listint_t *arr[1024], *list = *head;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (list)
	{
		arr[len] = list;
		len++;
		list = list->next;
	}
	list = *head;
	j = len / 2;
	if ((len % 2) == 0)
		n = 1;
	else
		n = 0;
	while (list)
	{
		if (i >= (len / 2) - n)
		{
			if (list->n != arr[j]->n)
				return (0);
			j--;
		}
		i++;
		list = list->next;
	}
	return (1);
}

#include "lists.h"
#include <stdio.h>
/**
 * insert_node - function in C that inserts a number
 * into a sorted singly linked list.
 * @head: the head
 * @number: the number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new, *prev;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	prev = *head;
	if (number <= prev->n)
	{
		new->next = prev;
		*head = new;
		return (new);
	}
	list = *head;
	prev = *head;
	list = list->next;
	while (list)
	{
		if (number <= list->n)
		{
			prev->next = new;
			new->next = list;
			return (new);
		}
		prev = list;
		list = list->next;
	}
	prev->next = new;
	new->next = NULL;
	return (new);
}

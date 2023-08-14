#include "lists.h"
/**
 * check_cycle - A function that checks if a list is a cycle.
 * @list: Pointer to linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start = list;

	if (!list)
		return (0)
	list = list->next;
	while (list)
	{
		if (list == start)
			return (1);
		list = list->next;
	}
	return (0);
}

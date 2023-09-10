#include "lists.h"
/**
 * check_cycle - A function that checks if a list is a cycle.
 * @list: Pointer to linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *rabbit = list, *turtle = list;

	if (!list)
		return (1);
	while (rabbit != NULL && turtle != NULL && rabbit->next != NULL)
	{
		rabbit = rabbit->next->next;
		turtle = turtle->next;
		if (rabbit == turtle)
			return (1);
	}
	return (0);

}

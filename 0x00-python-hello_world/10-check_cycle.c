#include "lists.h"
/**
 * check_cycle - A function that checks if a list is a cycle.
 * @list: Pointer to linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *arr[1024];
	int i;

	if (list == NULL)
		return (0);
	arr[0] = list;
	arr[1] = NULL;
	list = list->next;
	while (list)
	{
		i = 0;
		while (arr[i])
		{
			if (list == arr[i])
				return (1);
			i++;
		}
		arr[i] = list;
		arr[i + 1] = NULL;
		list = list->next;
	}
	return (0);
}

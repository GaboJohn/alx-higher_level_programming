#include "lists.h"
/**
 * check_cycle - checks if there is a circle
 * @list: pointer to head
 *
 * Return: 0(no cycle) otherwise 1(there is cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list == NULL)
		return (0);

	x = list;
	y = list;

	while (y != NULL && y->next != NULL)
	{
		x = x->next;
		y = y->next->next;

		if (x == y)
			return (1);
	}
	return (0);
}

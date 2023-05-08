#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle int it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *doub = list;
listint_t *reg = list;

if (list == NULL)
	return (0);
while (doub && doub->next)
{
reg = reg->next;
doub = doub->next->next;

if (reg == doub)
	return (1);
}
return (0);
}

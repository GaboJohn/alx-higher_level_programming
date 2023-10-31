#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to a pointer to head
 * @number: number to insert
 * Return: address of new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *curr, *prev = NULL;

	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;
	curr = *head;

	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}
	if (prev == NULL)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		prev->next = node;
		node->next = curr;
	}
	return (node);
}

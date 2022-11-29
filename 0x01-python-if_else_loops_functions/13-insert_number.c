#include "lists.h"

/**
 * insert_node - insert a number into a list
 * @head: a double pointer the head of the linked list
 * @number: the number to insert
 *
 * Description: this function inserts a number into a sorted singly
 * linked list
 *
 * Return: address of the new node, NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *mem;

	mem = malloc(sizeof(listint_t));
	if (mem == NULL)
		return (NULL);

	mem->n = number;

	if (node == NULL || node->n >= number)
	{
		mem->next = node;
		*head = mem;
		return (mem);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	mem->next = node->next;
	node->next = mem;

	return (mem);
}

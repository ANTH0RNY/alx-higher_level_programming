#ifndef LIST_H
#define LIST_H

/**
 * struct listint_t - sll
 * @n: int
 * @next: the next single linked list
 * Description: single list list node
 */
typedef struct listint_t
{
	int n;
	struct listint_t *next;
} listint_t;

int check_cycle(listint_t *list);

#endif

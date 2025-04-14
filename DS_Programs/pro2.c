#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node*next;
	
	
};
struct node*front;
struct node*rear;
void insert();
void delete();
void display();
void main()

{
	int choice;
	while(choice!=4)
	{
		printf("\n Insert:1\n");
		printf("Delete:2\n");
		printf("Display the queue:3\n");
		printf("Exit:4\n");
		printf("Enter your choice:");
		printf("%d",&choice);
		switch(choice)
		{
			case 1:
			    insert();
			    break;
			case 2:
				delete();
				break;
			case 3:
				display();
				break;
			case 4:
				exit(0);
				break;
			default:
				printf("\n Invalid Choice\n");
				
				
		}
	}
}
void insert()
{
	struct node*ptr;
	int item;
	ptr=(struct node*)malloc(sizeof(struct node));
	if(ptr==NULL)
	{
		printf("\n OVERFLOW\n");
		return;
	}
	else
	{
		printf("\Enter the item to be inserted:");
		scanf("%d",&item);
		ptr->data=item;
		if(front==NULL)
		{
			front=ptr;
			rear=ptr;
			front->next=NULL;
			rear->next=NULL;
			
			
		}
		else
		{
			rear->next=ptr;
			rear=ptr;
			rear->next=NULL;
		}
	}
}
void delete()
{
	struct node*ptr;
	if(front==NULL)
	{
		printf("\nUNDERFLOW\n");
		return;
	}
	else
	{
		ptr=front;
		front=front->next;
		free(ptr);
	}
}
void display()
{
	struct node*ptr;
	ptr=front;
	if(front==NULL)
	{
		printf("\nQueueu is Empty\n");
		
	}
	else
	{
		printf("\n Queue:");
		while(ptr!=NULL)
		{
			printf("%d",ptr->data);
			ptr=ptr->next;
		}
		printf("\n");
	}
	getch();
}

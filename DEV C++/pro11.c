#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push(int x) {
    if (top >= MAX - 1) {
        printf("Stack overflow\n");
        exit(EXIT_FAILURE);
    }
    stack[++top] = x;
}

int pop() {
    if (top < 0) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    return stack[top--];
}

int main() {
    char postfix[MAX];
    printf("Enter the postfix expression: ");
    if (fgets(postfix, sizeof(postfix), stdin) == NULL) {
        printf("Error reading input.\n");
        return EXIT_FAILURE;
    }


    size_t len = strlen(postfix);
    if (len > 0 && postfix[len - 1] == '\n') {
        postfix[len - 1] = '\0';
    }

    for (int i = 0; postfix[i] != '\0'; i++) {
        if (isdigit(postfix[i])) {
            push(postfix[i] - '0');
        } else if (postfix[i] == ' ') {
            continue; 
        } else {
            int A = pop();
            int B = pop();
            int RES;
            switch (postfix[i]) {
                case '+': RES = B + A; break;
                case '-': RES = B - A; break;
                case '*': RES = B * A; break;
                case '/':
                    if (A == 0) {
                        printf("Division by zero error\n");
                        return EXIT_FAILURE;
                    }
                    RES = B / A;
                    break;
                default:
                    printf("Invalid operator: %c\n", postfix[i]);
                    return EXIT_FAILURE;
            }
            push(RES);
        }
    }

    if (top != 0) {
        printf("Invalid postfix expression\n");
        return EXIT_FAILURE;
    }

    printf("The result of the expression = %d\n", pop());
    return EXIT_SUCCESS;
}


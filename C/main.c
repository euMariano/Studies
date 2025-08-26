#include <stdio.h>

int main(void) {
  int a;
  int b;
  int i = 0;
  printf("Enter two integers: ");
  scanf("%d %d", &a, &b);
  int sum = a + b;
  int product = a * b;
  printf("the sum is %d and the product is %d\n", sum, product);
  if (sum > 5) {
    printf("The sum is greater than 5\n");
  } else {
    printf("The sum is less than 5\n");
  }
  while (i <= 10) {
    printf("%d\n", i);
    i++;
  }
  return 0;
}

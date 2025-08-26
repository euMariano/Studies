#include <stdio.h>

int main() {
  int farh, celcius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  farh = lower;
  while (farh <= upper) {
    celcius = 5 * (farh - 32) / 9;
    printf("%d\t%d\n", farh, celcius);
    farh = farh + step;
  };
}

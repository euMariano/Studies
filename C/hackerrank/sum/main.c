#include <stdio.h>
// 1.1f

int main(void) {
  int a;
  int b;
  float c;
  float d;

  scanf("%d %d", &a, &b);
  scanf("%f %f", &c, &d);

  int si = a + b;
  int di = a - b;
  float sf = c + d;
  float df = c - d;

  printf("%d %d\n", si, di);
  printf("%1.1f %1.1f", sf, df);
  return 0;
}

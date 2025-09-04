#include <stdio.h>

void display(int var, int *ptr);
void update(int *ptr);

int main() {

  int var = 15;
  int *ptr;
  // *ptr = conteudo do endereço apontado pelo ponteiro;
  // ptr = endereço da variável apontada pelo ponteiro;
  // &ptr = endereço do ponteiro(onde ele se localiza, não à que se liga);

  ptr = &var;

  display(var, ptr);

  update(&var);

  display(var, ptr);

  printf("\n\nEnd.");
  while (1)
    ;
  return 0;
};

void display(int var, int *ptr) {
  printf("conteudo de var = %d\n", var);
  printf("endereço de var = %p\n", &var);
  printf("conteudo apontado por ptr = %d\n", *ptr);
  printf("endereço apontado por ptr = %p\n", ptr);
  printf("endereço de ptr = %p\n", &ptr);
};

void update(int *ptr) { *ptr = *ptr + 2; }

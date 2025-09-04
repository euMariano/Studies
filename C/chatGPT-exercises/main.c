#include <stddef.h>
#include <stdio.h>

int main() {
  char item[50];
  int quant;
  float price;
  printf("Digite o que você deseja comprar:\n");
  fgets(item, sizeof(item), stdin);
  printf("qual o preço do produto?\n");
  scanf("%f", &price);
  printf("Digite uma quantidade\n");
  scanf("%d", &quant);
  float fprice = quant * price;
  printf("você comprou %d unidades de %s\nValor total: R$%0.2f\n", quant, item,
         fprice);
  return 0;
}

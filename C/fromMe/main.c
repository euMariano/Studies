#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ITEMS 100

typedef struct {
  char *key;
  char *value;
} Pair;

typedef struct {
  Pair items[MAX_ITEMS];
  int size;
} Dictionary;

void dictionary_init(Dictionary *dict) { dict->size = 0; }

void dictionary_add(Dictionary *dict, const char *key, const char *value) {
  for (int i = 0; i < dict->size; i++) {
    if (strcmp(dict->items[i].key, key) == 0) {
      dict->items[i].value = strdup(value);
      return;
    }
  }
  if (dict->size < MAX_ITEMS) {
    dict->items[dict->size].key = strdup(key);
    dict->items[dict->size].value = strdup(value);
    dict->size++;
  }
}

char *dict_get(Dictionary *dict, const char *key) {
  for (int i = 0; i < dict->size; i++) {
    if (strcmp(dict->items[i].key, key) == 0) {
      return dict->items[i].value;
    }
  }
  return NULL;
}

int main() {
  Dictionary dict;
  dictionary_init(&dict);

  dictionary_add(&dict, "name", "mariano");
  dictionary_add(&dict, "age", "18");
  dictionary_add(&dict, "country", "Brazil");
  dictionary_add(&dict, "Language", "Python");
  dictionary_add(&dict, "Language", "C");
  dictionary_add(&dict, "Distro", "Arch Linux");

  printf("Name: %s\n", dict_get(&dict, "name"));
  printf("Age: %s\n", dict_get(&dict, "age"));
  printf("City: %s\n", dict_get(&dict, "city"));
  printf("Language: %s\n", dict_get(&dict, "Language"));
  printf("Distro: %s\n", dict_get(&dict, "Distro"));
  return 0;
}

/* An attempt to rewrite from Python to C
 * Additional changes need to be discussed
 * Until now everything will be this way
 * - OpposedDeception
*/
#ifndef LANG_HEADER
#define LANG_HEADER

#include <yaml.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_PATH_LENGTH 256

/*! TODO: Implement merge_document function to merge language fike
 *
 * @todo merge_document()
 * @todo better flexibility
 */

// We created an error function for painless usage
void error(const char* err) {
  printf("%s\n", err);
}

// yaml_document_t data structure is used
yaml_document_t* load_yaml(const char* path, void(*err)(const char*)) {
  FILE *file = fopen(path, "r");

  if (file == NULL) {
    err("Failed to open then yaml file");
    return NULL;
  }

  // Initializing the parser
  yaml_parser_t parser;
  yaml_document_t document = malloc(sizeof(yaml_document_t));

  if (document == NULL) {
    err("The document is null");
    fclose(file);
    return NULL
  }

  // We actually do it here lol
  yaml_parser_initialize(&parser, document);
  yaml_parser_set_input_file(&parser, file);

  if (!yaml_parser_load(&parser, document)) {
    err("An issue occurred, couldn't load yaml file");
    yaml_parser_delete(&parser);
    free(document);
    fclose(file);
    return NULL;
  }

  yaml_parser_delete(&parser);
  fclose(file);
  return document;

}

yaml_document_t* init_language(const char* lang_path, const char* fallback_path, void(*err)(const char*)) {
  yaml_document_t document = load_yaml_file(lang_path);

  // If it's empty then we throws an errkr
  if (document == NULL) {
    err("The language file is empty or does not exist");
    return NULL;
  }

  // Initializing the fallback document
  yaml_document_t* fallback_document = load_yaml_file(fallback_path);

  if (fallback_document == NULL) {
    err("Path is not found or is not correct");
    yaml_parser_delete(fallback_document);
    return NULL;
  }

  // Ending the task
  yaml_parser_delete(fallback_document);
  return document;

}
#endif

// File: characters.c
// Description: for random universe generation
//
// @author: nodoby else is looking at this
////////////////////////////////////////////////////////////////////////////////

//TODO: everything

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdio.h>

void help_print(){
   printf("  Usage:\n  help: print usage information\n");
   printf("  quit: exit program\n");
}

int main(){

   char buf[64];
   char* names[32][32];
   char* mode = "r+";
   FILE* file;   

   while(1){
      printf("> ");
      fgets(buf, 64, stdin);
      buf[strlen(buf)-1] = NULL;
      file = fopen("characters.txt", mode);
      // If user entered "quit", do so
      if(strcmp(buf, "quit") == 0){
         return EXIT_SUCCESS;
      }
      else if(strcmp(buf, "help") == 0){
         help_print();
      }
   }
}

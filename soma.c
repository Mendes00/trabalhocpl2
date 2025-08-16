#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Erro: Forneça exatamente dois números\n");
        return 1;
    }
    
    int num1 = atoi(argv[1]);
    int num2 = atoi(argv[2]);
    int resultado = num1 + num2;
    
    printf("%d", resultado);
    return 0;
}

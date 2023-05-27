#include <stdio.h>
#include <multiplicador.hpp>   // <-- declares public interface of "libfoo" library

int main(){
    int a = multiplicar_por_100(2);
    printf("%d\n", a);
    return 0;
}

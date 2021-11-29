#include <stdio.h>

// int main(){
//     printf("hello world\n");
//     return 0;
// }


main()
{
    printf("##########温度转化程序#############\n");
    float fahr,celsius;
    int lower,upper,step;
    
    lower = 0;
    upper = 300;
    step = 20;
    fahr = lower;
    while(fahr <=upper){
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f\t%6.1f\n", fahr,celsius);
        fahr = fahr + step;
    }
}
# C程序设计语言

# 第一章导言

```c
//入门
#include <stdio.h>
int main(){
    printf("hello world\n");
    return 0;
}

//变量与算术表达式
#include <stdio.h>
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


//for语句
#include <stdio.h>
/* 打印华氏温度-摄氏温度对照表 */
main()
{
    int fahr;

    for (fahr = 0; fahr <= 300; fahr = fahr + 20)
        printf("%3d %6.1f\n", fahr,(5.0/9.0)*(fahr-32));

}

// 符号常量
#include <stdio.h>

#define LOWER  0    /* 温度表的下限 */ 
#define UPPER  300  /* 温度表的上限 */
#define STEP   20   /* 步长 */
/* 打印华氏温度-摄氏温度对照表 */
main()
{
    int fahr;

    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr,(5.0/9.0)*(fahr-32));

}

// 字符输入输出。文件复制
#include <stdio.h>
main()
{
    int c;
    while((c = getchar()) != EOF)
        putchar(c);
}





```


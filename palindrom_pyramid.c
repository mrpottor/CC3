#include<stdio.h>
int main()
{
int n, i, j, space, count = 1, num = 0, star = 8;
scanf(“%d”, &n);
space = n;
for (i = 1; i <= n; i++)
{
for (j = 1; j <= star; j++)
if(i + j <= star + 1)
printf(“*”);
num++;
for (j = 1; j <= i; j++)
{
printf(“%d”, num);
if (i > 1 && count < i)
{
printf(“*”);
count++;
}
}
for (j = 1; j <= star; j++)
if(i + n <= j + n)
printf(“*”);
printf(“\n”);
space–;
count = 1;
}
return 0;
}
#include<stdio.h>
int main()
{
    char a1100],i,d=0;
    scanf("%[^\n]",a1);
    for(i=0;a1[i]!='\0';++i)
    {
        if(a1[i]==' ')
        {
        d=i;}
    }
     for(i=d+1;a1[i]!='\0';++i)
     {
         printf("%c",a1[i]);
     }
     printf(" ");
     for(i=0;a1[i]!=' ';++i)
     {
         printf("%c",a1[i]);
     }
}

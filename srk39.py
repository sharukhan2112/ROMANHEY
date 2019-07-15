#include<stdio.h>
int main()
{
    int a1[100],i,d=0,h;
    for(i=0;i<10;++i)
    {
        
        scanf("%d",&a1[i]);}
 for(i=0;i<10;++i)
    {
        
        if(a1[i]>d)
        {
            d=a1[i];
        }
        
    }

    printf("%d",d);
}    

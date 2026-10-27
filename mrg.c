#include<stdio.h>
int main()
{
int a[10],b[10],c[20];
int n,m,i;
printf("enter the 1st array size:");
scanf("%d",&n);

printf("enter the elements of 1st array:\n");
for(i=0;i<n;i++){
scanf("%d",&a[i]);
}
printf("enter the 2nd array size:");
scanf("%d",&m);

printf("enter the elements of 2nd array:\n");
for(i=0;i<m;i++){
scanf("%d",&b[i]);
}

int k=0;
for(i=0;i<n;i++){
c[k++]=a[i];
}
for(i=0;i<m;i++){
c[k++]=b[i];
}
printf("merged array;");
for(i=0;i<n+m;i++){
printf("%d",c[i]);
}
printf("/n");
return 0;
}

#include <stdio.h>

int main(){
    double weight,length;
    double standard;

    printf("体重(kg)を入力してください ==> " );
    scanf("%lf", &weight);
    printf("身長(cm)を入力してください ==> ");
    scanf("%lf", &length);


    printf("BMI = %.1f \n", weight/((length/100)*(length/100)) );
    printf("標準体重 = %.1f kg \n", standard=22.0*(length/100)*(length/100));
    printf("肥満率 = %.1f %% \n",  (weight-standard)/standard*100);

    return 0;
}

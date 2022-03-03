#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>// to control whether file exists or not
#include <string.h>
#include <time.h>
#include <locale.h>


///////////// DATALAR
typedef struct ogrenci_data{
    char id[15];
    char name[30];
    char sure_name[20];
    int max_course_amount;
    int max_credit_amount;
    int alinan_dersler;
    int alinan_krediler;
    struct ogrenci_data *next;
    struct ogrenci_data *previous;
}Data_Student;

typedef struct ders_kayit{
    char course_code[10];
    char course_name[50];
    int course_credit;
    int course_limit;
    int alinan_kontenjan;
    struct ders_kayit *next;
    int *student_list;
}Data_Courses;


////////FONKSIYONLAR
//Giris Fonksiyonlari
void Menu(Data_Courses **first, Data_Student **second);
void Ders_Islemleri(Data_Courses **main_head_course);
void Ogrenci_Islemleri(Data_Student **main_head_student, Data_Courses **main_head_course);
void Ogrenciyi_Derse_Ekleme_Islemleri();

//Temel Is Fonksiyonlari
int Dosya_Kontrol(char File_Name[30]);
void Tarih_Al(char **gelen_pointer); // otomatik istenmiyor, kullanicidan alinacak
Data_Courses *Sort_Courses(Data_Courses *head);
Data_Student *Sort_Student(Data_Student *head);

//Veri Yazdirma Fonksiyonlari
void Course_Veri_Yazdir(Data_Courses *head);
void Course_Veri_Yazdir_Dersi_Alanlar(Data_Courses *head);
void Student_Veri_Yazdir(Data_Student *head);

//Dosya Okuma Fonksiyonlari
Data_Courses *Course_Read_File(char File_Name[255], char delim[2]);
Data_Student *Student_Read_File(char File_Name[255], char delim[2]);

//Dosyaya Yazdirma ve Guncelleme Fonksiyonlari
void Ogrenci_Ders_Programi_Kaydet(Data_Courses *head, char student_id[15]);
void Ders_Koduna_Gore_Kaydet(Data_Courses **head, char ders_kodu[10]);
void Kayitlari_Guncelle();
void dosyayaKaydet(Data_Courses *head); // dersler dosyasina kayit
void dosyayaKaydet_Ogrenciler(Data_Student **head);

// Dosyadan Veri Alma Fonksiyonlari
void Split_Datas_Course(Data_Courses *head, char buffer[255], char delim[2]);
void Split_Datas_Student(Data_Student *head, char buffer[255], char delim[2]);

//Ders Ile Ilgili Fonksiyonlar
int Ders_Acikmi_Kontrol(Data_Courses *head, char aranan[10]);
Data_Courses *Ders_Ac(Data_Courses *head);
Data_Courses *Ders_Kapa(Data_Courses *head);
int Derse_Ogrenci_Ekle(Data_Courses **head_course, char ders_kodu[10], char ogrenci_id[15]);

//Ogrenci Ile Ilgili Fonksiyonlar
int Ogrencinin_Hakki_Varmi(Data_Courses **head_courses, Data_Student **head_student, char ders_kodu[10], char wanted_id[15]);
int Ogrenci_Varmi_Kontrol(Data_Student *head, char aranan[15]);
void Ogrenci_Ekle(Data_Student **head_real);
int Ogrenci_Sil(Data_Student **head_, char student_id[15]);

//Son Eklenen Fonksiyonlar
// Data_Courses *Ogrenciye_Ders_Ekle(Data_Courses*head_course, char wanted_id[15]);
int Ogrenci_ve_Ders_Ortak_Islemler(Data_Courses **head_courses);
void Ogrenciden_Ders_Birak(Data_Courses **head_course, Data_Student **head_student, char ders_kodu[10], char wanted_id[15]);
void Baslangic_Dosyalardan_Oku(Data_Courses **head_courses, Data_Student **head_student); 
void Ogrenci_Ders_Kayit_Ekleme_Yap(char ders_kodu[10], char ogrenci_id[15]);
void Ogrenci_Ders_Kayit_Kapatma_Yap(char ders_kodu[10]);
void Ogrenci_Silindi_Ders_Sil(char ogrenci_id[15]);
void Cikarken_Yazdir(Data_Student **student);

/////////////MAIN
int main(){
    Data_Courses *main_course_head = NULL; // NULL versem olur mu?
    Data_Student *main_student_head = NULL; // NULL versem olur mu?
    Baslangic_Dosyalardan_Oku(&main_course_head, &main_student_head);

    Menu(&main_course_head, &main_student_head);

    // char *given;
    // Tarih_Al(&given);
    // puts(given);
    return 0;
}
/////////////MAIN


//////////////////////Fonksiyonlar
/////giris fonksiyonlari
void Menu(Data_Courses **first, Data_Student **second){
    int choice = 0;
    while (choice != 4){
    printf("\n1-Ders Islemleri");
    printf("\n2-Ogrenci Islemleri");
    printf("\n4-Cik\n: ");
    fflush(stdin);
    scanf("%d", &choice);
    
    Data_Courses *main_course_head=*first;
    Data_Student *main_student_head=*second;

    switch (choice){
        case 1:
            Ders_Islemleri(&main_course_head);
            break;
        case 2:
            Ogrenci_Islemleri(&main_student_head, &main_course_head); // course headi dondurmeyecegim
            break;
        case 4:
            printf("\nCikiliyor...");
            break;
        default:
            printf("\nDogru Bir Secenek Giriniz.");
        }
    *first = main_course_head;
    *second = main_student_head;
    }
}

void Ders_Islemleri(Data_Courses **main_head_course){
    Data_Courses *head_course = *main_head_course;
    int choice = 0;
    // int okundu = 0;
    printf("\nDers Verileri\n");
    Course_Veri_Yazdir(head_course);
    while (choice != 4){       
        printf("\n\n1-Ders Ac");
        printf("\n2-Ders Kapa");
        printf("\n3-Dersin Koduna Gore Alanlari Kaydet");
        printf("\n4-Ana Menuye Don\n: ");
        fflush(stdin);
        scanf("%d", &choice);
        

        if(choice == 1){
            // Ders Ac
            // control et, ekle
            head_course = Ders_Ac(head_course);
            printf("\nEkleme Sonrasi");
            Course_Veri_Yazdir(head_course);
        }
        else if (choice == 2){
            // Ders Kapa
            // control et, sil
            // kayit dosyasinda ders kapandi olarak isaretle
            fflush(stdin);
            head_course = Ders_Kapa(head_course);
            printf("\nSilme Sonrasi Veriler");
            Course_Veri_Yazdir(head_course);
            //OgrenciDersKayit yapildi
        }   
        else if (choice == 3){
            // Dersi Alanlari disari kaydet
            // kayit dosyasinda ders kapandi olarak isaretle
            char ders_kodu[10];
            printf("\nVerilmesini istediginiz dersin kodunu girin: ");
            fflush(stdin);
            scanf("%[^\n]s", &ders_kodu);
            if(Ders_Acikmi_Kontrol(head_course, ders_kodu)){
                Ders_Koduna_Gore_Kaydet(&head_course, ders_kodu);

            }else{
                printf("\nDers Yok");
            }

        }
        else if(choice == 4){
            printf("\nAna Menuye Donuluyor ve Yapilan Degisiklikler Kaydediliyor...");
            dosyayaKaydet(head_course);
        }
        else{
            printf("\nSeceneklerden birini giriniz!");
        }

    }
    *main_head_course = head_course;
}

void Ogrenci_Islemleri(Data_Student **main_head_student, Data_Courses **main_head_course){
    // Data_Student *head_student = *main_head_student;
    Data_Student *head_student = *main_head_student;
    Data_Courses *head_courses = *main_head_course;

    int choice = 0;
    // int okundu = 0;

    printf("\nOgrenci Verileri:\n");
    Student_Veri_Yazdir(head_student);
    while (choice != 6){

        printf("\n\n1-Ogrenci Ekle");
        printf("\n2-Ogrenci Sil");
        printf("\n3-Ogrenciye Ders Ekle");
        printf("\n4-Ogrencinin Dersini Birak");
        printf("\n5-Ogrenciye Gore Ders Programi Al");
        printf("\n6-Ana Menuye Don\n: ");
        fflush(stdin);
        scanf("%d", &choice);

        if(choice == 1){
            // Ogrenci Ekle
            // control et, evet ise bir tane ekle
            fflush(stdin);
            Ogrenci_Ekle(&head_student);
            printf("\nDegisiklikler Sonrasi Veri:");
            Student_Veri_Yazdir(head_student);

        }
        else if (choice == 2){
            // Ogrenci Sil
            // control et, evet ise bir tane sil
            fflush(stdin);
            char student_id[15];
            printf("\nOgrenci Silmek Icin Giriniz\nOgrenci Id: ");
            fflush(stdin);
            scanf("%[^\n]s", &student_id);
            
            if(Ogrenci_Sil(&head_student, student_id)==1){
                Ogrenci_Silindi_Ders_Sil(student_id);
                printf("\nDegisiklikler Sonrasi Veri:");
                Student_Veri_Yazdir(head_student);
            }else{
                printf("\nSilinme islemi yapilamadi");
            }
            
        
        }
        else if(choice == 3){
            // Ogrenciye Ders Ekle
            // control et, evet ise ekle
            //Guncellemeyi yapsin
            char wanted_id[15];
            printf("\nDers Eklenme yapilmasini istediginiz ogrencinin nosunu yazin: ");
            fflush(stdin);
            scanf("%[^\n]s", &wanted_id);
            if(Ogrenci_Varmi_Kontrol(head_student, wanted_id)==1){
                char ders_kodu[10];
                printf("\nEklenmek istenen dersin kodunu yazin: ");
                fflush(stdin);
                scanf("%[^\n]s", &ders_kodu);
                if(Ders_Acikmi_Kontrol(head_courses, ders_kodu)==1){
                    printf("\nDers Ekleniyor...");
                    //
                    if(Ogrencinin_Hakki_Varmi(&head_courses, &head_student, ders_kodu, wanted_id)){
                        if(Derse_Ogrenci_Ekle(&head_courses, ders_kodu, wanted_id)==1){
                            Ogrenci_Ders_Kayit_Ekleme_Yap(ders_kodu, wanted_id);
                        }
                    }else{
                        printf("\nOgrenci Derse Kaydolamaz");
                    }
                    

                }
                else{
                    printf("\nBoyle bir ders yok...");
                }
            }
            else{
                printf("\nOgrenci Yok..");
            }  
            printf("\nDegisiklikler Sonrasi Veri:");
            Student_Veri_Yazdir(head_student);
        }
        else if(choice == 4){
            // Ogrencinin Dersini Birak
            // control et, evet ise sil
            // fflush(stdin);
            char wanted_id[15];
            printf("\nDersini Birakmak Istediginiz Ogrencinin IDsini yazin: ");
            fflush(stdin);
            scanf("%[^\n]s", &wanted_id);
            if(Ogrenci_Varmi_Kontrol(head_student, wanted_id)==1){
                char ders_kodu[10];
                printf("\nBirakilmasini istediginiz Dersin kodunu yazin: ");
                fflush(stdin);
                scanf("%[^\n]s", &ders_kodu);
                if(Ders_Acikmi_Kontrol(head_courses, ders_kodu)==1){
                    printf("\nDers Siliniyor...");
                    Ogrenciden_Ders_Birak(&head_courses, &head_student, ders_kodu, wanted_id);
                    // Ogrenci_Degerler_Degistir(head_student, wanted_id, -1);//burada azalacak
                }
                else{
                    printf("\nBoyle bir ders yok...");
                }
            }
            else{
                printf("\nOgrenci Yok..");
            }  
            printf("\nDegisiklikler Sonrasi Veri:");
            Student_Veri_Yazdir(head_student);
        }
        else if(choice == 5){
            // ders programi al
            char wanted_id[15];
            printf("\nDers Programini Almak Istediginiz Ogrencinin Numarai: ");
            fflush(stdin);
            scanf("%[^\n]s", &wanted_id);
            if(Ogrenci_Varmi_Kontrol(head_student, wanted_id)==1){
                printf("\nDers Programi veriliyor...");
                Ogrenci_Ders_Programi_Kaydet(head_courses, wanted_id);
            }
            else{
                printf("\nOgrenci Yok..");
            }            
        }
        else if(choice == 6){

            Student_Veri_Yazdir(head_student);
            printf("\nAna Menuye Donuluyor...");
            Cikarken_Yazdir(&head_student);
            // dosyayaKaydet_Ogrenciler(&head_student);
            // Data_Student *head = head_student;
            // printf("\n%s", head->id);


        }
        else{
            printf("Dogru bir secenek giriniz");
        }

    }
    *main_head_student = head_student;
    *main_head_course = head_courses;
}

////Temel Is Fonksiyonlari
int Dosya_Kontrol(char File_Name[30]){
    if (access( File_Name, F_OK ) == 0 )
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
}

void Tarih_Al(char **gelen_pointer){
    char *tarih;
    tarih = (char*)malloc(10*sizeof(char));
    if(tarih == NULL){
        printf("\nPointer hatasi, tarih al icinde");
    }
    else{
        time_t t = time(NULL);
        struct tm tm = *localtime(&t);
        sprintf(tarih, "%d.%d.%d", tm.tm_mday, tm.tm_mon+1, tm.tm_year+1900);
        // puts(tarihler);
        *gelen_pointer = tarih;
        
    }
    return;
}

Data_Courses *Sort_Courses(Data_Courses *head){
    // ascending olarak siralanacak
    if (head == NULL || head->next == NULL){
        return head;
    }

    char current_course_CODE[10];
    strcpy(current_course_CODE, head->course_code);

    Data_Courses *prev = head;
    Data_Courses *to_move = NULL;
    Data_Courses *tmp = head->next;

    while (tmp != NULL){
        // string compare ilk > ikinci ise >0
        // esit ise 0
        // kucuk ise <0, ben <0 ariyorum
        if(strcmp(tmp->course_code, current_course_CODE) < 0){ // tam tersi olacak, bir sey olursa ters cevir
            strcpy(current_course_CODE, tmp->course_code);
            to_move = prev;
        }
        prev = tmp;
        tmp = tmp -> next;
    } 
    if(to_move == NULL){
        head->next = Sort_Courses(head->next);
        return head;
    }
    prev = to_move;
    to_move = prev->next;
    prev->next = prev->next->next;
    to_move->next = Sort_Courses(head);
    return to_move;
}

Data_Student *Sort_Student(Data_Student *head){
    if (head == NULL || head->next == NULL){
        return head;
    }

    char current_student_ID[15];
    strcpy(current_student_ID, head->id);

    Data_Student *prev = head;
    Data_Student *to_move = NULL;
    Data_Student *tmp = head->next;

    while (tmp != NULL){
        if(strcmp(tmp->id, current_student_ID)<0){// olmazsa tam tersini al
            strcpy(current_student_ID, tmp -> id);
            to_move = prev;
        }
        prev = tmp;
        tmp = tmp -> next;
    } 
    if(to_move == NULL){
        head->next = Sort_Student(head->next);
        return head;
    }
    prev = to_move;
    to_move = prev->next;
    prev->next = prev->next->next;
    to_move->next = Sort_Student(head);
    return to_move;
}


//Veri Yazdirma Fonksiyonlari
void Course_Veri_Yazdir(Data_Courses *head){
    Data_Courses *temp;
    temp = head;
    
    while(temp!=NULL){
        printf("\n%s %s %d %d", temp->course_code, temp->course_name, temp->course_credit, temp->course_limit);
        temp = temp->next;
    }
    return;
}

void Student_Veri_Yazdir(Data_Student *head){
    Data_Student *temp;
    temp = head;
    int i =0;
    while(temp!=NULL){
        i++;
        // printf("\n%d", i);
        printf("\n%s %s %s aldigi_dersler:%d aldigi_krediler:%d", temp->id, temp->name, temp->sure_name, temp->alinan_dersler, temp->alinan_krediler);
        temp = temp->next;
    }
    return;
}


//Dosyayi Okuma Fonksiyonlari
Data_Courses *Course_Read_File(char File_Name[255], char delim[2]){
    FILE *fp = fopen(File_Name, "r");
    char buffer[255];
    Data_Courses *head = (Data_Courses*)malloc(sizeof(Data_Courses));
    Data_Courses *current_data;
    Data_Courses *prev_data;

    if(fgets(buffer, 255, fp) != NULL){
        Split_Datas_Course(head, buffer, delim);
    }
    prev_data = head;
    while(fgets(buffer, 255, fp) != NULL){
        current_data = (Data_Courses*)malloc(sizeof(Data_Courses));
        prev_data -> next = current_data;
        Split_Datas_Course(current_data, buffer, delim);
        prev_data = current_data;
    }
    prev_data -> next = NULL;
    fclose(fp);
    return head;
}

Data_Student *Student_Read_File(char File_Name[255], char delim[2]){
    FILE *fp = fopen(File_Name, "r");
    char buffer[255];
    Data_Student *head = (Data_Student*)malloc(sizeof(Data_Student));
    Data_Student *current_data;
    Data_Student *prev_data;

    if (fgets(buffer, 255, fp) != NULL){
        Split_Datas_Student(head, buffer, delim);
    }
    head -> previous = NULL;
    prev_data = head;

    while(fgets(buffer, 255, fp) != NULL){
        current_data = (Data_Student*)malloc(sizeof(Data_Student));
        prev_data -> next = current_data;
        Split_Datas_Student(current_data, buffer, delim);
        current_data -> previous = prev_data;
        prev_data = current_data;
    }
    prev_data -> next = NULL;
    fclose(fp);
    return head;
}


//Dosyaya Yazdirma ve Guncelleme Fonksiyonlari
void Ogrenci_Ders_Programi_Kaydet(Data_Courses *head, char student_id[15]){
    char data[20];
    strcpy(data, student_id);
    strcat(data, "_DERSPROGRAMI.txt");
    FILE *fp = fopen(data, "w");
    
    Data_Courses *temp = head;
    int *dersi_alanlar;
    int alanlar;
    int i;
    while(temp!=NULL){
        alanlar = temp->alinan_kontenjan;
        dersi_alanlar = temp->student_list;
        for(i=0; i<alanlar;i++){
            if(atoi(student_id)==dersi_alanlar[i]){
                printf("%s,%s\n", temp->course_code, temp->course_name);
                fprintf(fp, "%s,%s\n", temp->course_code, temp->course_name);
            }
        }
        temp = temp -> next;
    }
    fclose(fp);
}

void Ders_Koduna_Gore_Kaydet(Data_Courses **head, char ders_kodu[10]){
    char temporary[15];
    strcpy(temporary, ders_kodu);
    strcat(temporary, ".txt");
    FILE *fp = fopen(temporary, "a");
    Data_Courses *temp;
    int *ogrenci_id_ler;
    temp = *head;
    int i;
    char kaydet[20];
    while(temp!=NULL){
        if (strcmp(ders_kodu, temp->course_code)==0){
            if (temp->alinan_kontenjan > 0){
                ogrenci_id_ler = temp->student_list;
                for(i=0;i<temp->alinan_kontenjan;i++){
                    printf("\n%d", ogrenci_id_ler[i]);
                    itoa(ogrenci_id_ler[i], kaydet, 10);
                    fprintf(fp, " %d\n", *(ogrenci_id_ler+i));
                }  
                printf("\n%s.txt olarak kaydedildi", temp->course_code);
            }
            else{
                printf("\nKimse Dersi almiyor");
            }

            break;
        }
        temp = temp->next;
    }
    fpclose(fp);
}

void Kayitlari_Guncelle(){

}

void dosyayaKaydet(Data_Courses *head){ //dersler icin
    FILE *fp = fopen("dersler.txt", "w");
    char tmp[20];

    while(head != NULL){
        //str str int int
        // printf("\n%s",head->course_code);
        fputs(head->course_code, fp);
        fputc(',', fp);

        fputs(head->course_name, fp);
        fputc(',', fp);

        itoa(head->course_credit, tmp, 10);
        fputs(tmp, fp);
        fputc(',', fp);

        itoa(head->course_limit, tmp, 10);
        fputs(tmp, fp);
        fputc('\n', fp);

        head = head -> next;
    }
    fclose(fp);
    return;
}

void dosyayaKaydet_Ogrenciler(Data_Student **head2){
    Data_Student *head = *head2;
    printf("\n%s", head->id);

    FILE *fp = fopen("ogrenciler.txt", "w");
    // printf("\nNasil NULL olabilir1.2");

    char tmp[50];
    // FILE *fp = fopen("ogrenciler.txt", "w");
    // printf("\nNasil NULL olabilir1.5");

    if(fp==NULL){
        // printf("\nNasil NULL olabilir2");
    }
    // fputs("123", fp);
    // printf("1");
    while(head!=NULL){
        //22011001,Eddard,Stark,8,2
        //str,str,str,int,int

        printf("\n%s",head->id);
        fputs(head->id, fp);
        fputc(',', fp);

        fputs(head->name, fp);
        fputc(',', fp);

        fputs(head->sure_name, fp);
        fputc(',', fp);

        itoa(head->alinan_dersler, tmp, 10);
        fputs(tmp, fp);
        fputc(',', fp);

        itoa(head->alinan_krediler, tmp, 10);
        fputs(tmp, fp);
        fputc('\n', fp);

        head = head -> next;
    }
    printf("kapatildi");
    fclose(fp);
    return;
}


// Dosyadan Veri Alma Fonksiyonlari
void Split_Datas_Course(Data_Courses *head, char buffer[25], char delim[2]){
    // okunan veriler head olarak dondurulmeli
    char *token;
    token = strtok(buffer, delim);
    strcpy(head->course_code, token);
    
    token = strtok(NULL, delim);
    strcpy(head->course_name, token);
    
    token = strtok(NULL, delim);
    head->course_credit = atoi(token);
    
    token = strtok(NULL, delim);
    head->course_limit = atoi(token);

    // en basta 0 olarak atadim
    head->alinan_kontenjan = 0;
    return;
}

void Split_Datas_Student(Data_Student *head, char buffer[25], char delim[2]){
    char *token;
    token = strtok(buffer, delim);
    strcpy(head->id, token);

    token = strtok(NULL, delim);
    strcpy(head->name, token);

    token = strtok(NULL, delim);
    strcpy(head->sure_name, token);

    token = strtok(NULL, delim);
    head->alinan_dersler = atoi(token);

    token = strtok(NULL, delim);
    head->alinan_krediler = atoi(token);
    //bu degerler dosyada yok, o yuzden ilk basta 0 olarak verdim
    head->max_course_amount = 100;
    head->max_credit_amount = 100;
    return;
}


//Ders Ile Ilgili Fonksiyonlar
int Ders_Acikmi_Kontrol(Data_Courses *head, char Ders_Id[10]){
    //tek tarafli kontrol
    Data_Courses *temp_next;
    if (head == NULL){
        printf("\nHerhangi bir ders yok...");
        return 0;
    }
    else{
        temp_next = head;
    }

    while(temp_next != NULL){
        if (strcmp(Ders_Id, temp_next -> course_code)==0){
            return 1;
        }
        temp_next = temp_next -> next;
    }
    // eger bulamazsa saga dogru, 0 dondur
    return 0;
}


Data_Courses *Ders_Ac(Data_Courses *head){
    char course_code[10];

    printf("\nDers Eklemek Icin sirayla giriniz\nKurs Kodu: ");
    fflush(stdin);
    scanf("%[^\n]s",&course_code);
    // 0 is ders acik degildir
    if(Ders_Acikmi_Kontrol(head, course_code) == 0){
        
        char course_name[50];
        int course_credit;
        int course_limit;
        printf("\nKurs Adi: ");
        fflush(stdin);
        scanf("%[^\n]s",&course_name);
        printf("\nKurs Kredisi: ");
        fflush(stdin);
        scanf("%d", &course_credit);
        printf("\nKurs Kontenjani: ");
        fflush(stdin);
        scanf("%d", &course_limit);

        // burada dersi sona mi eklemek lazim? yoksa basa ekleyip siralamak mi?
        if(head == NULL){
            // gonderilen ilk ve acilmamis eleman oldugunu gosteriyor, degerleri ona ver
            head = (Data_Courses*)malloc(sizeof(Data_Courses));

            strcpy(head->course_code, course_code);
            strcpy(head->course_name, course_name);
            head->course_credit = course_credit;
            head->course_limit = course_limit;
            head->alinan_kontenjan = 0;
            head->next = NULL;
        }
        else{
            // linked list zaten var, bu da onun headi
            // koymak istedigim derste yokmus zaten, o zaman yeni deger olusturayim. Bunu head'e baglayayim.
            // head'in de yerini en basa alayim.
            // sonrasinda da siralayalim, burada yada baska bir yerde;
            // printf("nerede");
            Data_Courses *new_value;
            new_value = (Data_Courses *)malloc(sizeof(Data_Courses));
            strcpy(new_value->course_code, course_code);
            strcpy(new_value->course_name, course_name);
            new_value->course_credit = course_credit;
            new_value->course_limit = course_limit;
            new_value->alinan_kontenjan=0; // alan kisiyi ekledik
            new_value->next = NULL;
            // new_value->next = head;
            Data_Courses *temp = head;
            while(temp->next!=NULL){
                temp = temp->next;
            }
            // head her zaman en basta olacak
            temp->next = new_value;
        }
        //TODO: Yeni acilan dersten dolayi guncellenmesi gereken herhangi bir sey bulunmuyor
        //Dersleri Sirala;

        // printf("\nIslemler yapildi, donduruluyor");
        // Course_Veri_Yazdir(head);
        // printf("\nSonrasi");
        head = Sort_Courses(head);
        // Course_Veri_Yazdir(head);

        //TODO: Dersleri dersler.txt icine yazdir
        // bunu cikinca yap
        return head;
    }
    // 1 ise ders aciktir
    else{
        printf("\nDers halihazirda aciktir!!!");
        return head;
    }
}

Data_Courses *Ders_Kapa(Data_Courses *head){
    char course_code[10];
    
    printf("\nDers Silmek Icin giriniz\nKurs Kodu: ");
    fflush(stdin);
    scanf("%[^\n]s",&course_code);

    if(Ders_Acikmi_Kontrol(head, course_code) == 1){
        // ders varmis, silebilirsin
        //TODO: ders silinince guncellenmesi gereken seyler olacak;
        int found=0;
        Data_Courses *tmp;
        tmp = head;
        Data_Courses *prev=NULL;
        while(tmp!=NULL && !found){
            if (strcmp(tmp->course_code, course_code)==0){
                found = 1;
                if(prev==NULL){
                    head = tmp->next;
                    }
                else{
                    prev->next = tmp->next;
                        }
                    free(tmp);// belki burada icindeki linkled listi de silmek gerekir
                    }
            prev = tmp;
            tmp = tmp->next;
            }
        //TODO: dersin kapandigina dair guncelleme yap
        // Sort_Courses(head);bir dersin silinmesi, siralamayi bozmamali
        
        // course code a gore silme islemleri yapilsin
        Ogrenci_Ders_Kayit_Kapatma_Yap(course_code);
        return head;
    }
    else{
        // ders acik degil silemezsin
        printf("\nDers acik degil, acik olmayan bir dersi silemezsiniz!");
        return head;
    }
}

int Derse_Ogrenci_Ekle(Data_Courses **head_course, char ders_kodu[10], char ogrenci_id[15]){
    Data_Courses *head = *head_course;
    Data_Courses *first_position = head;
    int foo;
    // student_list = head_course -> student_list;
    Data_Courses *temp = head;
    if (head == NULL){
        printf("\nEklenmis Ders Yok, Ders Ekleyin");
        return 0;
    }
    int *ogrenci_listesi;
    int i, j;

    while(temp!=NULL){
        if(strcmp(temp->course_code, ders_kodu)==0){
            if(temp->alinan_kontenjan != temp->course_limit){
                for(i=0;i<temp->alinan_kontenjan;i++){
                    if(atoi(ogrenci_id) == temp->student_list[i]){
                        printf("\nOgrenci zaten derse kayitli, ekleme olmaz.\n");
                        return 0;
                    }
                }
                
                printf("\nOgrenci suan ekleniyor...");
                // ogrenci_listesi = temp->student_list;
                

                if(temp->alinan_kontenjan==0){
                    temp->student_list = (int*)malloc(sizeof(int)*1);
                    temp->student_list[0] = atoi(ogrenci_id);
                    // if(ogrenci_listesi==NULL){
                    if(ogrenci_listesi==NULL){
                        printf("\nStringi olustururken sorun");
                        return -1;
                    }
                    // ogrenci_listesi[0] = (int)malloc(sizeof(char)*10);
                    temp->alinan_kontenjan = temp->alinan_kontenjan + 1;
                }
                else{
                    temp->alinan_kontenjan = temp->alinan_kontenjan + 1;
                    foo=temp->alinan_kontenjan;

                    temp->student_list = realloc(temp->student_list, sizeof(int)*foo);
                    
                    if(temp->student_list==NULL){
                        printf("\nBuyuk stringi olustururken sorun");
                        return -1;
                    }
                    // string[temp->alinan_kontenjan-1] = (char**)malloc(sizeof(char*));
                    // for(i=0;i<10;i++){
                    temp->student_list[temp->alinan_kontenjan - 1] = atoi(ogrenci_id);
                    // }
                }
                // strcpy(string[temp->alinan_kontenjan-1], ders_kodu);
                *head_course = first_position;
                return 1;

            }else{
                printf("\nKursun limiti dolmus, kisi eklenemez");
                return 0;
            }

        }
        temp = temp->next;
    }    
}


//Ogrenci Ile Ilgili Fonksiyonlar
int Ogrencinin_Hakki_Varmi(Data_Courses **head_courses, Data_Student **head_student, char ders_kodu[10], char wanted_id[15]){
    Data_Student *head_s = *head_student;
    Data_Student *first_position = head_s;
    Data_Courses *head_c = *head_courses;

    int kursun_kredi_miktari;
    int ogrencinin_aldigi_krediler;

    while(head_s!=NULL){
        if(strcmp(head_s->id, wanted_id)==0){
            while(head_c!=NULL){
                if(strcmp(head_c->course_code, ders_kodu)==0){
                    if(head_s->max_course_amount == head_s->alinan_dersler){
                        printf("\nOgrencinin ders hakki yok");
                        return 0;
                    }
                    else{
                        kursun_kredi_miktari = head_c -> course_credit;
                        kursun_kredi_miktari += head_s->alinan_krediler;

                        if(kursun_kredi_miktari>head_s->max_credit_amount){
                            printf("\nOgrencinin kredileri asiyor, dersi alamaz");
                            return 0;
                        }
                        else{
                            head_s->alinan_krediler = head_s -> alinan_krediler + head_c ->course_credit;
                            head_s->alinan_dersler++;
                            *head_student = first_position;
                            printf("\nOgrenci dersi alabilir");
                            return 1;
                        }
                    }
                    //tmm bu ogrencinin bilgilerine ulastim,
                    // dersin bilgilerine de ulastim

                }
                head_c = head_c -> next;
            }
        }
        head_s = head_s -> next;
    }
    return 0;
}
int Ogrenci_Varmi_Kontrol(Data_Student *head, char Ogrenci_Id[15]){
    Data_Student* temp_next, *temp_previous;

    if(head == NULL){
        printf("Herhangi bir ogrenci girisi yapilmamis...");
        return 0;
    } 
    else{
        temp_next = head;
        temp_previous = head;
    }
    // bir saga kontrol   
    while(temp_next != NULL){
        if (strcmp(Ogrenci_Id, temp_next->id)==0){
            return 1;
        }
        temp_next = temp_next -> next; // son kisimdaki node -> next is NULL
    }
    
    while(temp_previous != NULL){
        if (strcmp(Ogrenci_Id, temp_previous->id)==0){
            return 1;
        }
        temp_previous = temp_previous -> previous; // son kisimdaki node -> next is NULL
    }
    // bulunamadi
    return 0;
        // bir de sola kontrol

}

void Ogrenci_Ekle(Data_Student **head_real){
    char ogrenci_id[15];
    printf("\nOgrenci Eklemek Icin Sirayla Giriniz\nOgrenci Numarasi: ");
    fflush(stdin);
    scanf("%s", &ogrenci_id);
    // puts(ogrenci_id);
    Data_Student *head = *head_real;
    if(Ogrenci_Varmi_Kontrol(head, ogrenci_id) == 0){
        // puts(ogrenci_id);
        char name[30];
        char sur_name[20];
        int course_amount;
        int credit_amount;

        printf("\nAdi: ");
        fflush(stdin);
        scanf("%[^\n]s",&name);

        printf("\nSoy Adi: ");
        fflush(stdin);
        scanf("%[^\n]s",&sur_name);    

        printf("\nAlacagi Maximum Kurs Miktari: ");
        fflush(stdin);
        scanf("%d", &course_amount);
        printf("\nAlacagi Maximum Kredi Miktari: ");
        fflush(stdin);
        scanf("%d", &credit_amount);
        
        if(head == NULL){
            head = (Data_Student *)malloc(sizeof(Data_Student));
            // veriyi kullanicidan alirken
            /// maximum ders ve kredi sayisini aliyoruz
            // dosyadan okurken alinan ders ve kredi sayisini aliyoruz.
            strcpy(head->id, ogrenci_id);
            // puts(head->id);
            strcpy(head->name, name);
            strcpy(head->sure_name, sur_name);
            head->max_course_amount = course_amount;
            head->max_credit_amount = credit_amount;
            head->alinan_dersler = 0; // nur topu gibi tertemiz, hic bir sey almamis
            head->alinan_krediler = 0;
            head->previous = NULL;
            head->next = NULL;
        }
        else{
            Data_Student *new_value;
            new_value = (Data_Student*)malloc(sizeof(Data_Courses));
            strcpy(new_value->id, ogrenci_id);
            strcpy(new_value->name, name);
            strcpy(new_value->sure_name, sur_name);
            new_value->max_course_amount = course_amount;
            new_value->max_credit_amount = credit_amount;
            new_value->alinan_dersler = 0; // nur topu gibi tertemiz, hic bir sey almamis
            new_value->alinan_krediler = 0;
            new_value->next = NULL;

            Data_Student *temp = head;
            while(temp->next!=NULL){
                temp = temp->next;
            }
            temp->next = new_value;
            new_value -> previous = temp;
            // new_value->previous = head;
            // head->next = new_value;
        }
        // printf("ne oldu");
        Student_Veri_Yazdir(head);
        // printf("\n1kisim");
        head = Sort_Student(head);
        // printf("\n2kisim");
        *head_real = head;
        return;
    }
    else{
        printf("\nOgrenci zaten var!!!");
        
        return;
    }
}

int Ogrenci_Sil(Data_Student **head_, char student_id[15]){
    // char student_id[15];
    Data_Student *head = *head_;
    // printf("\nOgrenci Silmek Icin Giriniz\nOgrenci Id: ");
    // fflush(stdin);
    // scanf("%[^\n]s", &student_id);

    // printf("\n1.kisim");
    if(Ogrenci_Varmi_Kontrol(head, student_id) == 1){
        int found=0;
        Data_Student *tmp;
        tmp = head;
        Data_Student *prev=NULL;
        // printf("\n2.kisim");

        while(tmp!=NULL && !found){
            if(strcmp(tmp->id, student_id)==0){
                found = 1;
                if(prev==NULL){
                    head = tmp->next;
                }
                else{
                    prev->next = tmp->next;
                }
                free(tmp);
            }
            prev = tmp;
            tmp = tmp-> next;
        }
        // printf("\n3.kisim");
        *head_ = head;
        return 1;
    }
    else{
        printf("\nOgrenci yok, olmayan bir ogrenciyi silemezsiniz!");
        *head_ = head;
        return 0;
    }
}


// Data_Courses *Ogrenciye_Ders_Ekle(Data_Courses *head_student, char wanted_id[15]){

// }
void Ogrenciden_Ders_Birak(Data_Courses **head_course, Data_Student **head_student, char ders_kodu[10], char wanted_id[15]){
    
    Data_Student *head_s = *head_student;
    Data_Student *first_position = head_s;
    Data_Courses *head_c = *head_course;
    Data_Courses *first_course = head_c;
    int kursun_kredi_miktari;
    int ogrencinin_aldigi_krediler;
    int i,j;
    int kontrol = 0;
    int *new_list;

    while(head_s!=NULL){
        if(strcmp(head_s->id, wanted_id)==0){
            while(head_c!=NULL){
                if(strcmp(head_c->course_code, ders_kodu)==0){
                    // ogrenci ve kurs bilgileri elimde, kurstan silmem lazim ogrenciyi

                    for(i=0;i<head_c->alinan_kontenjan;i++){
                        if(atoi(wanted_id)==head_c->student_list[i]){
                            kontrol = 1;
                            head_c -> alinan_kontenjan--;
                            new_list = malloc(sizeof(int)*head_c->alinan_kontenjan);
                            i=0;
                            j=0;
                            while(i<=head_c->alinan_kontenjan){
                                if(head_c->student_list[i] != atoi(wanted_id)){
                                    new_list[i] = head_c->student_list[j];
                                    i++;
                                    j++;
                                }else{
                                    j++;
                                }
                            }
                            break;
                        }
                        free(head_c->student_list);
                        head_c->student_list = new_list;
                    }
                    if(kontrol==1){
                        kursun_kredi_miktari = head_c -> course_credit;
                        head_s -> alinan_dersler--;
                        head_s -> alinan_krediler = head_s->alinan_krediler - kursun_kredi_miktari;
                    }
                    else{
                        printf("\nOgnrenci bu dersi almiyor, silme yapilamaz!");
                    }

                }
                head_c = head_c -> next;
            }
        }
        head_s = head_s -> next;
    }
    *head_student = first_position;
    *head_course = first_course;
    return;

}

void Baslangic_Dosyalardan_Oku(Data_Courses **head_courses, Data_Student **head_student){
    Data_Student *student = *head_student;
    Data_Courses *courses = *head_courses;
    
    if(Dosya_Kontrol("dersler.txt")){
        printf("\nDersler aliniyor...\n");
        courses = Course_Read_File("dersler.txt",",\0");
        printf("\nVeriler:\n");
        Course_Veri_Yazdir(courses);
        //  *head_courses = courses;
    }
    else{
        courses = NULL;
        //  *head_courses = courses;

    }
    if(Dosya_Kontrol("ogrenciler.txt")){
        printf("\nOgrenciler aliniyor...");
        student=Student_Read_File("ogrenciler.txt", ",\0");
        printf("\nVeriler:\n");
        Student_Veri_Yazdir(student);
        // *head_student = student;
    }else{
        student = NULL; 
        // *head_student = student;

    }

    if(Dosya_Kontrol("OgrenciDersKayit.txt")){
        if(Ogrenci_ve_Ders_Ortak_Islemler(&courses)==1){
            printf("\n\nDerslere Ogrencilerin Atanmasi Bitti..");
            // Course_Veri_Yazdir_Dersi_Alanlar(courses);
        }
        else{
            printf("\n Herhangi bir derse kayit yapilmamis");
        }
    }


    *head_courses = courses;
    *head_student = student;
}

int Ogrenci_ve_Ders_Ortak_Islemler(Data_Courses **head_courses){
    Data_Courses *head = *head_courses;
    FILE *fp = fopen("OgrenciDersKayit.txt", "r");
    int noluyor;
    int kontrol;
    char ders_kodu[10];
    char ogrenci_id[15];
    char ogrenci_ders_durum[15];

    char buffer[255];
    char delim[2] = ",\0";
    char *token;
    char kompare[15] = "kayitli";
    
    while(fgets(buffer, 255, fp) != NULL){
        token = strtok(buffer, delim);//normal kod_onemli degil

        token = strtok(NULL, delim);//Ders kodu
        strcpy(ders_kodu, token);

        token = strtok(NULL, delim);//ogrenci_id
        strcpy(ogrenci_id, token);

        token = strtok(NULL, delim);// tarih onemli degil
        token = strtok(NULL, delim);
        token[strlen(token)-1]='\0';
        strcpy(ogrenci_ders_durum, token);
        
        // noluyor = strcmp(ogrenci_ders_durum, kompare);
        if(strcmp(ogrenci_ders_durum, kompare)==0){
            Derse_Ogrenci_Ekle(&head, ders_kodu, ogrenci_id);
            kontrol = 1;
        }
        
    }
    // Derse_Ogrenci_Listesi_Ekle(&head);

    *head_courses = head;
    if(kontrol==1){
        Course_Veri_Yazdir_Dersi_Alanlar(head);
        return 1;
    }
    else{
        return 0;
    }
    
}

// void Derse_Ogrenci_Listesi_Ekle(Data_Courses **head_courses){

// }
void Course_Veri_Yazdir_Dersi_Alanlar(Data_Courses *head){
    Data_Courses *temp;
    int *ogrenci_listesi;
    temp = head;
    int i;
    while(temp!=NULL){
        if(temp->alinan_kontenjan>0){
          printf("\nDers: %s",temp->course_code);
          ogrenci_listesi = temp->student_list;
          for(i=0;i<temp->alinan_kontenjan;i++){
            printf("\n%d", ogrenci_listesi[i]);

            }  
        }
        
        temp = temp->next;
    }
    return;
}
void Ogrenci_Ders_Kayit_Ekleme_Yap(char ders_kodu[10], char ogrenci_id[15]){
    printf("\nOgrenciDersKayit Dosyasina Ogrenci Ekleniyor");
    FILE *fp = fopen("OgrenciDersKayit.txt", "a+");
    
    int day;
    int month;
    int year;
    printf("\nTarihleri verin:");
    fflush(stdin);
    scanf("%d.%d.%d", &day, &month, &year);
    char tmp[50];
    char buffer[255];
    char *token;
    int son_kod=1;

    while(fgets(buffer, 255, fp) != NULL){
        son_kod++;
    }
    
    fprintf(fp, "%d,%s,%s,%d.%d.%d,kayitli", son_kod, ders_kodu, ogrenci_id,day,month,year);
    fclose(fp);

}

void Ogrenci_Ders_Kayit_Kapatma_Yap(char ders_kodu[10]){
    printf("\nOgrenciDersKayit Dosyasindan Ders Kapatiliyor");
    FILE *fp = fopen("OgrenciDersKayit.txt", "r");
    FILE *fp2 = fopen("OgrenciDersKayit2.txt", "w");
    int kontrol;
    char buffer[255];
    char *token;
    char delim[2] = ",\0";

    while(fgets(buffer, 255, fp) != NULL){
        kontrol = 0;
        token = strtok(buffer, delim);
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        if(strcmp(token, ders_kodu)==0){
            kontrol = 1;
        }
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        if(kontrol == 1){
            fputs("ders kapandi\n", fp2);
        }
        else{
            fputs(token, fp2);
        }
        // fputc('\n', fp2);
    }
    fclose(fp);fclose(fp2);
    FILE *fp3 = fopen("OgrenciDersKayit.txt", "w");
    FILE *fp4 = fopen("OgrenciDersKayit2.txt", "r");

    while(fgets(buffer, 255, fp4) != NULL){
        fprintf(fp3, "%s", buffer);
    }
    fclose(fp3);fclose(fp4);
}

void Ogrenci_Silindi_Ders_Sil(char ogrenci_id[15]){   
    printf("\nOgrenciDersKayit Dosyasindan Ogrenci Siliniyor");
    FILE *fp = fopen("OgrenciDersKayit.txt", "r");
    FILE *fp2 = fopen("temp.txt", "w");
    int kontrol;
    char buffer[255];
    char *token;
    char delim[2] = ",\0";

    while(fgets(buffer, 255, fp) != NULL){
        kontrol = 0;
        token = strtok(buffer, delim);
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        if(strcmp(token, ogrenci_id)==0){
            kontrol = 1;
        }
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        fputs(token, fp2);
        fputc(',', fp2);

        token = strtok(NULL, delim);
        if(kontrol == 1){
            fputs("silindi\n", fp2);
        }
        else{
            fputs(token, fp2);
        }
        // fputc('\n', fp2);
    }
    fclose(fp);fclose(fp2);
    FILE *fp3 = fopen("OgrenciDersKayit.txt", "w");
    FILE *fp4 = fopen("temp.txt", "r");

    while(fgets(buffer, 255, fp4) != NULL){
        fprintf(fp3, "%s", buffer);
    }
    fclose(fp3);fclose(fp4);
}

void Cikarken_Yazdir(Data_Student **student){

            FILE *fp = fopen("ogrenciler.txt", "w");

            char tmp[50];
            // FILE *fp = fopen("ogrenciler.txt", "w");
            // printf("\nNasil NULL olabilir1.5");

            // fputs("123", fp);
            // printf("1");
            printf("1");

            Data_Student *head_student = *student;
            printf("1");

            while(head_student!=NULL && head_student->id != NULL){
                //22011001,Eddard,Stark,8,2
                //str,str,str,int,int
                printf("1");
                fprintf(fp, "%s,%s,%s,%d,%d\n", head_student->id, head_student->name, head_student->sure_name, head_student->alinan_dersler, head_student->alinan_krediler);
                printf("1");
                
                head_student = head_student->next;
            }
            printf("kapatildi");
            fclose(fp);   
}
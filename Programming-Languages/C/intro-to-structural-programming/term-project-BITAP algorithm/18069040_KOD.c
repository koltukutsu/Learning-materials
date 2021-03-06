#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <time.h>

#define SINIR 100000

int Bitap(const char *text, const char *pattern);
/*	Bitap fonksiyonu, BITAP Algoritmasi kullanarak
	verilen -text- icinde, aranan -pattern- in olup olmadigini
	kontrol eder.
*/

void IndexYazdirici(const char *text, const int max, const char *aranan, const int index);
/*	IndexYazdirici fonksiyonu, -text- icerisindeki
	her bir kelimenin baslangic indexini yazdirir,
	boylece kullanici bulunan index degeriyle
	metinde bulunan kelimelerin baslangic indexlerini
	karsilastirabilir.
*/

void GrafikCizici(const float miktar);
/*	GrafikCizici fonksiyonu, -miktar_dizi- icerisinde 3 * 4 = 12
	farkli kosulu icinde tutar.	Rowlarda 3 tane farkli text, 
	ve her bir column icinde de metnin 4 farkli varyasyonunun
	Bitap fonksiyonu ile yapilan islemlerin yapilma suresini tutar.
*/

int main(){
	int i, j;
	clock_t start, end;
	// 3 * 4 = 12 tane durum icin sure degeleri, -sureler- icine atilir.
	double sureler[12];
	// 3 * 4 = 12 tane durum icin index degeleri, -indexler- icine atilir.
	int indexler[12];
	/* 3 tane text sirasiyla 4 farkli sekilde olusturulmustur
		1. text ->> 125 karakterden olusmaktadir.
		2. text ->> 75 karakterden olusmaktadir
		3. text ->> 30 karakterden olusmaktadir.
	3 farkli text, her biri icin 4 tane varyansi ile birlikte
	12 elemanlik textler dizisinin icerisine alinmistir
	*/
	char *textler[12];
	// 1. kisim /// ->> aranacak kelime 'Yildiz' 6 karakterden olusmaktadir
	// 125 karakterlik buyuk boyda text
	printf("\t~~~1. KISIM~~~");
	textler[0] = "Yildiz Teknik Universitesi Yapisal Programlamaya Giris dersi Ahmet ELbir tarafindan 2. Gruba 2020-2021 doneminde verilmistir.";
	textler[1] = "Yapisal Programlamaya Giris dersi Ahmet ELbir Yildiz Teknik Universitesi tarafindan 2. Gruba 2020-2021 doneminde verilmistir.";
	textler[2] = "Yapisal Programlamaya Giris dersi Ahmet ELbir tarafindan 2. Gruba 2020-2021 doneminde verilmistir. Teknik Universitesi Yildiz";
	textler[3] = "Yildim Teknik Universitesi Yapisal Programlamaya Giris dersi Ahmet ELbir tarafindan 2. Gruba 2020-2021 doneminde verilmistir.";
	// 75 karakterlik orta boyda text
	textler[4] = "Yildiz Teknik Universitesi Alternatif Enerjili Sistemler Kulubu calisiyor..";
	textler[5] = "Teknik Universitesi Alternatif Enerjili Yildiz Sistemler Kulubu calisiyor..";
	textler[6] = "Teknik Universitesi Alternatif Enerjili Sistemler Kulubu calisiyor. Yildiz.";
	textler[7] = "Yildim Teknik Universitesi Alternatif Enerjili Sistemler Kulubu calisiyor..";
	// 30 karakterlik kucuk boyda text
	textler[8] = "Yildiz Teknik A kapisi girisi.";
	textler[9] = "Teknik A Yildiz kapisi girisi.";
	textler[10] = "Teknik A kapisi girisi. Yildiz";
	textler[11] = "Yildim Teknik A kapisi girisi.";
	/*	text icerisinde aranilmasi istenilen kisim aynidir,
		4 tane aranacak metin icin ortak durumlar sirasiyla aranan:
		
		1) basta (ilk kelime olarak)
		2) neredeyse ortada (kelime baslangici olarak, 3 kelimenin 2.si gibi)
		3) sonda (son kelime olarak)
		4) metnin icinde yok
		
		olacak sekilde ayarlanmistir.
	*/
	// aranacak ibare word degiskeni icerisindedir icerisindedir.
	char *word = "Yildiz";
	
/// buradan sonra algoritma calisacak
	for (i = 0; i < 12; i++){
		// hesaplanan sureler, -sureler-in icerisine
		// hesaplanan indexler, -indexler-in icerisine atiliyor
		start = clock();
		/* kodun burada SINIR=100000 kere calismasinin sebebi
		   kodun cok hizli calismasi ve gozle gorulur bir deger elde
		   edilememesidir. Dongu sonucu bir deger elde edilebilmektedir.
		*/
		for (j = 0; j < SINIR; j++){
			indexler[i] = Bitap(textler[i], word);	
		}
		end = clock();
		sureler[i] = (float)(end - start);
	}
	int value;
	for (i = 0; i < 12; i++){
		if (i == 0){
			printf("\n\n\n\t~~~125 karakterlik buyuk metin icin sirasiyla BASTA, ORTADA, SONDA, METINDE YOK~~~");
			value = 125;
		}

		if (i == 4){
			printf("\n\n\n\t~~~75 karakterlik buyuk metin BASTA, ORTADA, SONDA, METINDE YOK~~~");
			value = 75;
		}
			
		if (i == 8){
			printf("\n\n\n\t~~~30 karakterlik buyuk metin BASTA, ORTADA, SONDA, METINDE YOK~~~");
			value = 30;
		}
		IndexYazdirici(textler[i], value, word, indexler[i]);
		GrafikCizici(sureler[i]);
	}
	
	printf("\n\n\n\t~~~1.KISIM her bir metin icin CALISMA SURELERI karsilastirmasi~~~");
	for(i = 0; i < 12; i++){
		printf("\n\t%d. metin icin", i + 1);
		GrafikCizici(sureler[i]);
	}
	
	// 2. kisim /// ->> aranacak kelime 'Yildizteknikuniversitesi' 24 karakterden olusmaktadir
	char *textler2[12];
	int sureler2[12];
	int indexler2[12];
	
	printf("\n\n\n\t~~~2. KISIM~~~");
	/* 3 tane text sirasiyla 4 farkli sekilde olusturulmustur
		1. text ->> 150 karakterden olusmaktadir.  
		2. text ->> 100 karakterden olusmaktadir  
		3. text ->> 50 karakterden olusmaktadir. 
	3 farkli text, her biri icin 4 tane varyansi ile birlikte
	12 elemanlik textler dizisinin icerisine alinmistir
	*/
	// 150 karakterlik buyuk boyda text
	textler2[0] = "Yildizteknikuniversitesi Teknik Universitesi Yapisal Programlamaya Giris dersi ARS.GOVAhmet ELbir tarafindan 2. Gruba 2020-2021 doneminde verilmistir.";
	textler2[1] = "Yapisal Programlamaya Giris dersi ARS.GOVAhmet ELbir Yildizteknikuniversitesi Teknik Universitesi tarafindan 2. Gruba 2020-2021 doneminde verilmistir.";
	textler2[2] = "Yapisal Programlamaya Giris dersi ARS.GOVAhmet ELbir tarafindan 2. Gruba 2020-2021 doneminde verilmistir. Teknik Universitesi Yildizteknikuniversitesi";
	textler2[3] = "Yildimteknikuniversitesi Teknik Universitesi Yapisal Programlamaya Giris dersi ARS.GOVAhmet ELbir tarafindan 2. Gruba 2020-2021 doneminde verilmistir.";
	// 100 karakterlik orta boyda text
	textler2[4] = "Yildizteknikuniversitesi Teknik Universitesi Alternatif Enerjili Sistemler Kulubu surekli calisiyor.";
	textler2[5] = "Teknik Universitesi Alternatif Enerjili Yildizteknikuniversitesi Sistemler Kulubu surekli calisiyor.";
	textler2[6] = "Teknik Universitesi Alternatif Enerjili Sistemler Kulubu surekli calisiyor. Yildizteknikuniversitesi";
	textler2[7] = "Yildimteknikuniversitesi Teknik Universitesi Alternatif Enerjili Sistemler Kulubu surekli calisiyor.";
	// 50 karakterlik kucuk boyda text
	textler2[8] = "Yildizteknikuniversitesi Teknik A kapisinin girisi";
	textler2[9] = "Teknik A Yildizteknikuniversitesi kapisinin girisi";
	textler2[10] = "Teknik A kapisinin girisi Yildizteknikuniversitesi";
	textler2[11] = "Yildimteknikuniversitesi Teknik A kapisinin girisi";
	/*	text icerisinde aranilmasi istenilen kisim aynidir,
		4 tane aranacak metin icin ortak durumlar sirasiyla aranan:
		
		1) basta (ilk kelime olarak)
		2) neredeyse ortada (kelime baslangici olarak, 3 kelimenin 2.si gibi)
		3) sonda (son kelime olarak)
		4) metnin icinde yok
		
		olacak sekilde ayarlanmistir.
	*/
	// aranacak ibare word degiskeni icerisindedir icerisindedir.
	char *word2 = "Yildizteknikuniversitesi";
	
/// buradan sonra algoritma calisacak
	for (i = 0; i < 12; i++){
		// hesaplanan sureler, -sureler-in icerisine
		// hesaplanan indexler, -indexler-in icerisine atiliyor
		start = clock();
		/* kodun burada SINIR=100000 kere calismasinin sebebi
		   kodun cok hizli calismasi ve gozle gorulur bir deger elde
		   edilememesidir. Dongu sonucu bir deger elde edilebilmektedir.
		*/
		for (j = 0; j < SINIR; j++){
			indexler2[i] = Bitap(textler2[i], word2);	
		}
		end = clock();
		sureler2[i] = (float)(end - start);
	}
	
	for (i = 0; i < 12; i++){
		if (i == 0){
			printf("\n\n\n\t~~~150 karakterlik buyuk metin icin sirasiyla BASTA, ORTADA, SONDA, METINDE YOK~~~");
			value = 125;
		}

		if (i == 4){
			printf("\n\n\n\t~~~100 karakterlik buyuk metin BASTA, ORTADA, SONDA, METINDE YOK~~~");
			value = 75;
		}
			
		if (i == 8){
			printf("\n\n\n\t~~~50 karakterlik buyuk metin BASTA, ORTADA, SONDA, METINDE YOK~~~");
			value = 30;
		}
		IndexYazdirici(textler2[i], value, word2, indexler2[i]);
		GrafikCizici(sureler[i]);
	}
	
	printf("\n\n\n\t~~~2.KISIM her bir metin icin CALISMA SURELERI karsilastirmasi~~~");
	for(i = 0; i < 12; i++){
		printf("\n\t%d. metin icin", i + 1);
		GrafikCizici(sureler2[i]);
	}
	
	printf("\n\n\n\t~~~1. ve 2.KISIM her bir metin icin CALISMA SURELERI karsilastirmasi~~~");
	
	for(i = 0; i < 2; i++){
		if (i == 0){
			printf("\n\n\t1.KISIM");
			for (j = 0; j < 12; j++){
			printf("\n\t%d. metin icin", j + 1);
			GrafikCizici(sureler[j]);
			}
		}
		else{
			printf("\n\n\n\t2.KISIM");
			for (j = 0; j < 12; j++){
			printf("\n\t%d. metin icin", j + 1);
			GrafikCizici(sureler2[j]);
			}
		}
	}
	return 0;
}

int Bitap(const char *text, const char *pattern)
{
	/*
	return degeri bir -index- ise, aranan bulundu anlamina gelir
	return degeri -1 ise aranan bulunmadi anlamina gelir
	*/
	int n = strlen(pattern);
	unsigned long R;
	unsigned long patternMask[CHAR_MAX + 1]; // 128 e kadar olan ascii karakterler dahil
	int i;

	if (pattern[0] == '\0')
		return 0;
	
	//HATA: aranan pattern'in boyu 32 bitten fazla olamaz, yani 0 ile 31!
	if (n > 31)
		return -1;
		
	
	// sayinin eslenigini alir ve isaret degistirir
	// unsigned icin ilk bit haric diger tum bitler
	// 1 olmus olur, deger ->> 4,294,967,294 (2^32 - 2)
	R = ~1;
	
	/* tum degerler eslenikleri alinakarak
		unsigned long icin max degere esitlendi
		4,294,967,295 (2^32 - 1)
	*/
	for (i = 0; i <= CHAR_MAX; ++i)
		patternMask[i] = ~0;
	/*
		1UL    -> yalnizca ilk biti 1 olan unsigned long ifade eder
		x << y -> bitwise left shift, yani x * (2^y) islemi yapilir
		&= 	   -> bitwise and, x &= y isleminde bit seviyesinde -and- yapilir
		|= 	   -> bitwise or, x |= y isleminde bit seviyesinde -or- yapilir
	*/
	for (i = 0; i < n; ++i)
		patternMask[pattern[i]] &= ~(1UL << i);
		// i kadar 1UL sola oteleniyor
		// her seferinde 1 oteleme miktari artiyor, 2 kere 3 kere gibi
		// her bir karakter icin kaydedilen ve tekrar hesaplanirsa guncellenen -pattern- yapisi patternMask'a atiliyor

	for (i = 0; text[i] != '\0'; ++i){
		//R hala ~1'e esit
		// her seferinde R'in degeri guncelleniyor bitwise or islemi ile
		R |= patternMask[text[i]];
		// ve bir sola shift-left ile kaydiriliyor, yani en anlamsiz bite bir 0 ekleniyor
		R <<= 1;
	
		if (0 == (R & (1UL << n))) // her seferinde n kadar bitin eklendigi 1UL ile mathch yani 0 larin uyusup uyusmadigi kontrol ediliyor.
		// uyustugu vakit bu degerimizi return edebiliriz anlamina geliyor ve indexi bulmus oluyoruz.
			return (i - n) + 1;
	}
	//pattern bulunmaz ise -1 return ediliyor, bu da arananin bulunmadigi anlamina geliyor
	return -1;
}


void IndexYazdirici(const char *text, const int max, const char *aranan, const int index){
	/*
		verilen indexe gore, -aranan- in bulunup bulunmadigini soyler
		-aranan- bulundu ise her bir kelimeyi baslangic indexi
		ile birlikte yazdirir.
	*/
    int i;
    printf("\n\t%c %c %c", 18, 18, 18);
    if (index != -1){
    	printf("\n\n\t'%s' kelimesi %d.indexte bulundu", aranan, index);
    	printf("\n\tVerilen metin, her bir kelimenin baslangic indexiyle birlikte: ");
    	printf("\n\t\t-0- ");
    	for (i = 0; i < max; i++){
    		
        if (text[i] == ' ')
            printf(" -%d- ", i);    
        else
            printf("%c", text[i]);
        }      
	}
	else{
		printf("\n\n\t%s metnin icinde bulunamamistir!", aranan);
	}
}

void GrafikCizici(const float miktar){
	/*
		verilen miktar kadar 219 kodlu karakteri yazdirir ve bir bar-plotting yapar.
	*/
	int i;
	int int_miktar = miktar;
	printf("\n\t SURE\n");
	printf("\t> %d || ", int_miktar);
	for (i = 0; i < int_miktar; i++){
		printf("%c", 219);
	}
}

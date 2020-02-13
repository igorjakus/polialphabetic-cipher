/* 
* SZYFR POLIALFABETYCZNY
* JÊZYK: C++
* AUTOR: IGOR JAKUS
*/

#include <iostream>
#include <string>

std::string encrypt(std::string text, std::string keyWord)
{
	//Zaszyfrowany tekst
	std::string result = "";

	//Przesuniecie
	int key = 0;

	for (unsigned int i = 0, k = 0; i < text.length(); i++, k++)
	{
		//Pomija spacje
		while (text[i] == char(32)) i++;

		//Cofa wskaznik na poczatek gdy skonczy sie klucz
		if (k >= keyWord.length())
			k = 0;

		//Ustawia przesuniecie
		if (isupper(keyWord[k])) 
			key = int(keyWord[k]) - 64;
		else 
			key = int(keyWord[k]) - 96;

		//Szyfruje tekst
		if (isupper(text[i]))
			result += char(int(text[i] + key - 65) % 26 + 65);
		else
			result += char(int(text[i] + key - 97) % 26 + 97);
	}

	//Zwraca zaszyfrowany tekst
	return result;
}

int main()
{
	//Wpisanie tekstu do zaszyfrowania
	std::string text;
	std::cout << "Podaj tekst do zaszyfrowania: ";
	std::getline(std::cin, text);

	//Wpisanie klucza
	std::string key;
	std::cout << "Podaj klucz: ";
	std::cin >> key;

	//Wyswietlenie zaszyfrowanego tekstu
	std::cout << "Zaszyfrowany tekst: " << encrypt(text, key) << std::endl;

	//Wyswietlenie odszyfrowanego tekstu
	//std::cout << "Odszyfrowany tekst: " << decrypt(encrypt(text, key), key) << std::endl;

	return 0;
}

/*
std::string decrypt(std::string text, std::string keyWord)
{
	//Zaszyfrowany tekst
	std::string result = "";

	//Przesuniecie
	int key = 0;

	for (unsigned int i = 0, k = 0; i < text.length(); i++, k++)
	{
		//Pomija spacje
		while (text[i] == char(32)) i++;

		//Cofa wskaznik na poczatek gdy skonczy sie klucz
		if (k >= keyWord.length())
			k = 0;
		key = int(keyWord[k]) - 96;
		//Szyfruje tekst
		if (isupper(text[i]))
			result += char(int(text[i] - key - 65) % 26 + 65);
		else
			result += char(int(text[i] - key - 97) % 26 + 97);
	}

	//Zwraca zaszyfrowany tekst
	return result;
}
*/
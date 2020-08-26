#include <iostream>
#include <string>

std::string encrypt(std::string text, std::string keyWord)
{
	std::string result = "";
	int key = 0;

	for (unsigned int i = 0, k = 0; i < text.length(); i++, k++)
	{
		while (text[i] == char(32)) i++;

		if (k >= keyWord.length())
			k = 0;

		if (isupper(keyWord[k])) 
			key = int(keyWord[k]) - 64;
		else 
			key = int(keyWord[k]) - 96;

		if (isupper(text[i]))
			result += char(int(text[i] + key - 65) % 26 + 65);
		else
			result += char(int(text[i] + key - 97) % 26 + 97);
	}
	
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

	return 0;
}
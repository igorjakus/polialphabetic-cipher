#include <iostream>
#include <string>

std::string encrypt(std::string plaintext, std::string keyWord)
{
	std::string encrypted = "";
	int shift { 0 };

	for (unsigned int i { 0 }, k { 0 }; i < plaintext.length(); i++, k++)
	{
		// Skipping spaces
		while (plaintext[i] == char(32)) i++;

		// Going to the start of the key when it ends
		if (k >= keyWord.length())
			k = 0;

		// Converting key into shift numbers
		if (isupper(keyWord[k])) 
			shift = int(keyWord[k]) - 64;
		else 
			shift = int(keyWord[k]) - 96;

		// Encrypting plaintext
		if (isupper(plaintext[i]))
			encrypted += char(int(plaintext[i] + shift - 65) % 26 + 65);
		else
			encrypted += char(int(plaintext[i] + shift - 97) % 26 + 97);
	}
	
	return encrypted;
}

int main()
{
	// Enter text
	std::string text = "";
	std::cout << "Enter the text to be encrypted: ";
	std::getline(std::cin, text);

	// Enter key
	std::string key = "";
	std::cout << "Enter the encryption key: ";
	std::cin >> key;

	// Display encrypted text
	std::cout << "Encrypted text: " << encrypt(text, key);

	return 0;
}
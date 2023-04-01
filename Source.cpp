
#include <iostream>
#include <random>
#include <ctime>
#include <fstream>
int main()
{
	std::vector<bool>res(128);
	std::cout << res.size();
	std::mt19937 mersenne{ static_cast<std::mt19937::result_type>(std::time(nullptr)) };
	std::uniform_int_distribution<> die{ 0, 1 };
	for (int i = 0; i < 128; i++)
		res.push_back(die(mersenne));
	std::ofstream myfile; 
	myfile.open("sequence.txt");
	for (int i = 0; i < res.size(); i++)
	{
		myfile << res[i] << " ";
	}
	myfile << "\n";
	myfile.close();
    return 1;
}
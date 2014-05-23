#include <iostream>
#include <string>
#include "search_strategies.cu"
using namespace std;

int main(int argc, char const *argv[])
{
	// TODO make comand line version
	string file;
	cout << "Enter a file: ";
	cin >> file;
	start_search(file);
	return 0;
}
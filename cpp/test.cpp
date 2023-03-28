#include <iostream>
#include <string>

using std::clog;
using namespace std; // This line enables us to use the 

int main(){

	std::clog << "This is a log message.\n";
	clog << "This is an error log, but with the use of a using deleclaration\n";
	std::cerr << "This is an error log message. \n"; 
	std::cout << "This is a console output.\n";

	std::cout <<"\n\n";

	// get a name and age and then print the required output for it.
	// unsigned will use all the 31bits to form an int
	unsigned int age;

	// the string variable 
	std::string name;

	std::cout << "the name entered is " << name << std::endl;	

	// getting a data with space in it
	std::string full_name;
	std::getline(std::cin, full_name);

	std::cout << "Your full name is " << full_name << '\n' ;


	// you need not necessarily return for the main function. Even if you don't type it out, it'll work.
	// return 0;
}
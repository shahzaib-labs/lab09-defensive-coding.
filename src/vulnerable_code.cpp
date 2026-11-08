
#include <iostream>
#include <cstdio>
using namespace std;

int main() {

    // Fixed-size character array
    char username[10];

    cout << "Enter your username: ";

    // Vulnerable: No input length restriction
    scanf("%s", username);

    cout << "Welcome, " << username << endl;

    return 0;
}

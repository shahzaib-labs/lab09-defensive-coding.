
#include <iostream>
#include <string>
using namespace std;

int main() {

    string username;

    cout << "Enter your username: ";

    // Read the complete input safely
    getline(cin, username);

    // Explicit input length validation
    if (username.empty() || username.length() > 9) {

        cout << "Error: Invalid username." << endl;
        return 1;
    }

    // Display validated input
    cout << "Welcome, " << username << endl;

    return 0;
}

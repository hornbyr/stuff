#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void readGPXFile(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Error: Unable to open file " << filename << endl;
        return;
    }

    string line;
    while (getline(file, line)) {
        // For simplicity, just print each line of the file
        cout << line << endl;
    }

    file.close();
}

int main() {
    string filename;
    cout << "Enter the name of the GPX file to read: ";
    cin >> filename;

    readGPXFile(filename);

    return 0;
}
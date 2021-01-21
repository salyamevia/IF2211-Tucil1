#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

int main(int argc, char const *argv[])
{
    // Read File
    string filename, text; 
    vector<vector<string>> strIn, strRes;
    cout << "Input filename (with extension): ";
    cin >> filename;
    cout << "Filename is " << filename << endl;

    ifstream f (filename); int i = 0; cout << "i ke-" << i << endl;
    strIn.push_back(vector<string>()); strRes.push_back(vector<string>());
    while(getline(f, text)) {
        if (text.length() == 0) {
            i++;
            cout << "i ke-" << i << endl;
            strIn.push_back(vector<string>()); strRes.push_back(vector<string>());
            getline(f, text);
        }

        if (text.rfind('-', 0) == 0) {
            getline(f, text);
            text.erase(remove_if(text.begin(), text.end(), (int(*) (int)) isspace), text.end());
            strRes[i].push_back(text);
            cout << "Res: ";
        } else {
            text.erase(remove_if(text.begin(), text.end(), (int(*) (int)) isspace), text.end());
            text.erase(remove(text.begin(), text.end(), '+'), text.end());
            strIn[i].push_back(text);
        }
        cout << text << endl;
    }

    // Check Input
    cout << "\nstrIn : " << endl;
    for (auto j = strIn.begin(); j != strIn.end(); ++j) {
        for(auto k = (*j).begin(); k != (*j).end(); ++k) {
            cout << *k << ' ';
        }
        cout << endl;
    }

    cout << "\nstrRes : " << endl;
    for (auto j = strRes.begin(); j != strRes.end(); ++j) {
        for(auto k = (*j).begin(); k != (*j).end(); ++k) {
            cout << *k << ' ';
        }
        cout << endl;
    }

    // Shuffle Array
    

    f.close();

    return 0;
}

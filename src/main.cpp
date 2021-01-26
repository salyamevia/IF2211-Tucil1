#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

vector<string> uniqueChar(vector<string> vect);

int main(int argc, char const *argv[])
{
    // Read File
    string filename, text; 
    vector<vector<string>> strIn, strRes, strAll, strFinal;
    cout << "Input filename (with extension): ";
    cin >> filename;
    cout << "Filename is " << filename << endl;

    ifstream f (filename); int i = 0; //cout << "i ke-" << i << endl;
    strIn.push_back(vector<string>()); strRes.push_back(vector<string>()); strAll.push_back(vector<string>());
    while(getline(f, text)) {
        if (text.length() == 0) {
            i++;
            //cout << "i ke-" << i << endl;
            strIn.push_back(vector<string>()); strRes.push_back(vector<string>()); strAll.push_back(vector<string>());
            getline(f, text);
        }

        if (text.rfind('-', 0) == 0) {
            getline(f, text);
            text.erase(remove_if(text.begin(), text.end(), (int(*) (int)) isspace), text.end());
            strRes[i].push_back(text); strAll[i].push_back(text);
            //cout << "Res: ";
        } else {
            text.erase(remove_if(text.begin(), text.end(), (int(*) (int)) isspace), text.end());
            text.erase(remove(text.begin(), text.end(), '+'), text.end());
            strIn[i].push_back(text); strAll[i].push_back(text);
        }
        //cout << text << endl;
    }

    // Check Input
    /*
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
    */

    cout << "\nstrAll : " << endl;
    for (auto j = strAll.begin(); j != strAll.end(); ++j) {
        for(auto k = (*j).begin(); k != (*j).end(); ++k) {
            cout << *k << ' ';
        }
        cout << endl;
    }

    for (auto it = strAll.begin(); it != strAll.end(); ++it) {
        // Check unique elements
        vector<char> uniqueChar = uniqueChar(it);
        cout << "\nuniqueChar : " << endl;
        for (auto j = uniqueChar.begin(); j != uniqueChar.end(); ++j) {
            cout << *j << ' ';
        }
        // Shuffle
        // Checker
        // Push to strFinal
        // >>> Huruf pertama tidak boleh menyatakan angka 0 <<<
        // Print strFinal, waktu, total tes
    }

    f.close();

    return 0;
}

vector<char> uniqueChar(vector<string> vect) {
    vector<char> res;
    for (auto i = vect.begin(); i < vect.end(); ++i) {
        for (auto const &c: (*i)){
            cout << "c: " << c << endl;
            if ((find(res.begin(), res.end(), c) == res.end()) && (!isspace(c))) {
                res.push_back(c);
            }
        }
    }

    return res;
}


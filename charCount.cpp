#include <iostream>
#include <vector>
#include <string>
using namespace std;

int charCountInString(string str, char c){
    int count = 0;
    for(int i = 0; i < str.size(); i++){
        if(str[i] == c){
            count++;
        }
    }
    return count;
}

int main(){
    int count = 0;
    string str;
    char c;
    cout << "Enter a string: ";
    getline(cin, str);

    cout << "Enter a character: ";
    cin >> c;
    count = charCountInString(str, c);
    cout << "The character \"" << c << "\" appears " << count << " times in the string \"" << str << "\"" << endl;

    return 0;
}

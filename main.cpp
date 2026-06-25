#include <iostream>
using namespace std;
int main() {
float voltage;
cout<<"Enter voltage:";
cin >> voltage;
if (voltage >= 12.0){
cout<<"motor start!";}
else {cout << "low power!";}
return 0;
}
#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Введи год: " << endl;
    cin >> num; // прошу пользователя ввести значение переменной и сохраняю его

    if (num % 2 == 0) {  // если остаток от деления num на 2 равен 0
        cout << "Молодец!" << endl; // пишу это
        cout << "Четное!" << endl; // пишу это
    } else {  // иначе
        cout << "Нечетное!" << endl;  // пишу это
    }
    return 0;
}

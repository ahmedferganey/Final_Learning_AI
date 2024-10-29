#include <iostream>
#include <iostream>
#include <vector>
#include <array>
#include <stdexcept>
#include <string>
#include <iomanip>

using namespace std;

class MathLibrary{
public:
    static constexpr double add(double a, double b) { return a + b; }
    static constexpr double multiply(double a, double b) { return a * b; }
};

class Account{
private:
    string owner;
    double balance;

public:
    Account(const string& name, double initial_balance) : owner(name), balance(initial_balance){}

    void deposit(double amount) {balance += amount;}

    void withdraw(double amount){
        if (amount <= balance){
            balance -= amount;
        }else{
            throw runtime_error("Insufficient funds");
        }
    }

    double getBalance() const {return balance;}
    /*
By marking methods as const, you prevent accidental modifications 
to the object’s state. This is especially useful in larger codebases 
where the risk of unintentional changes can lead to bugs.   

    Account myAccount(100.0);
    const Account constAccount(200.0);

    // Valid: Non-const object can call non-const and const methods
    myAccount.deposit(50.0);
    double myBalance = myAccount.getBalance();

    // Valid: Const object can only call const methods
    double constBalance = constAccount.getBalance();

    */
};

class Bank{
    private:
        vector<Account> accounts;
    public:
        void addAccount(const Account& account){
            accounts.push_back(account);
            /*
addAccount is a method that takes an Account object by reference and 
uses push_back() to add it to the accounts vector. This allows the bank 
to maintain a collection of account objects, which can be accessed and 
manipulated later.            
            */
        }
        void showAccounts() const{
            for (const auto& account : accounts){
                cout << "Account balance: " << account.getBalance() << endl;
            }
        }
};


// String Manipulation and Array Handling: Contact Manager
class Contact {
private:
    std::string name;
    std::string phone;

public:
    Contact(const std::string& name, const std::string& phone)
        : name(name), phone(phone) {}

    void display() const {
        std::cout << "Name: " << name << ", Phone: " << phone << "\n";
    }
};

class ContactManager {
private:
    std::vector<Contact> contacts;


public:

    void addContact(const Contact& contact) {
        contacts.push_back(contact);
    }

    void showContacts() const {
        for (const auto& contact : contacts) {
            contact.display();
        }
    }
};








const int NUM_STUDENTS =3;

struct Student{
    string name;
    int grade;
};

int main(){


    // Math Library Demo
    constexpr double x = 5.0;
    constexpr double y = 10.0;
    std::cout << "Math Library:\n";
    std::cout << "Add: " << MathLibrary::add(x, y) << "\n";
    std::cout << "Multiply: " << MathLibrary::multiply(x, y) << "\n\n";

    // Banking System Demo
    std::cout << "Banking System:\n";
    Bank bank;
    Account acc1("Alice", 1000);
    Account acc2("Bob", 1500);
    bank.addAccount(acc1);
    bank.addAccount(acc2);
    bank.showAccounts();
    std::cout << "\n";


    // Contact Manager Demo
    std::cout << "Contact Manager:\n";
    ContactManager manager;
    manager.addContact(Contact("Alice", "123-456-7890"));
    manager.addContact(Contact("Bob", "987-654-3210"));
    manager.showContacts();
/////////////////////////////////////////////////
    array<Student, NUM_STUDENTS> students = {{
        {"ahmed", 26}, {"mariam", 22}, {"alaa", 24}
    }};
    cout << setw(10) << "Name" << setw(10) << "Grade\n";
    for (const auto& student : students){
        std::cout << std::setw(10) << student.name << std::setw(10) << student.grade << "\n";
    }
    return 0;

}

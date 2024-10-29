#include <iostream>
#include <iomanip>

double celsiusToFahrenheit(double c) { return (c * 9.0 / 5) + 32; }
double fahrenheitToCelsius(double f) { return (f - 32) * 5.0 / 9; }
double celsiusToKelvin(double c) { return c + 273.15; }

int main() {
    double temperature;
    char scale;

    std::cout << "Enter temperature (e.g., 36.6 C): ";
    std::cin >> temperature >> scale;

    if (scale == 'C') {
        auto fahrenheit = celsiusToFahrenheit(temperature);
        auto kelvin = celsiusToKelvin(temperature);
        std::cout << "Fahrenheit: " << fahrenheit << "\nKelvin: " << kelvin << "\n";
    } else if (scale == 'F') {
        auto celsius = fahrenheitToCelsius(temperature);
        std::cout << "Celsius: " << celsius << "\n";
    } else {
        std::cout << "Unsupported scale.\n";
    }

    return 0;
}

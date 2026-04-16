import 'dart:io';
import 'functions.dart' show add, usersenc;
import 'dart:convert' as convert;
import 'package:http/http.dart' as http;
import 'test.dart' show _balance;
import 'functions.dart' show usersenc;

class Users {
  String? name;
  String? pass;
  String? email;

  printname() {
    print("Name: $name");
  }
}

class constructor {
  String? name;
  constructor(this.name) {
    print("Constructor called with name: $name");
  }
}

// defaukt
class person {
  String name;
  int age;
  person(this.name, this.age);
  void greet() => print("👋 Hello, I'm $name and I'm $age years old.");
}

// named
class shape {
  double width, height;
  shape.square(double size) : width = size, height = size;
  shape.rectange(this.width, this.height);
  void describe() => print("📐 Shape: ${width} x ${height}");
}

// factory with cashing
class logger {
  static final Map<String, logger> _cache = {};
  final String name;
  factory logger(String name) {
    return _cache.putIfAbsent(name, () => logger._internal(name));
  }
  logger._internal(this.name);
  void log(String message) => print("📝 [$name]: $message");
}

// private
class configmanager {
  static final configmanager _instance = configmanager._internal();
  configmanager._internal();
  factory configmanager() => _instance;
  void show() => print("⚙️ Using single instance of ConfigManager");
}

// 5. Const Constructor
class Point {
  final int x, y;

  const Point(this.x, this.y);

  void printPosition() => print("📍 Point at ($x, $y)");
}

// 6. Redirecting Constructor
class Animal {
  String species;
  int legs;

  Animal(this.species, this.legs);

  Animal.insect(String species) : this(species, 6);

  void info() => print("🐾 $species with $legs legs.");
}

void main() {
  Users ferganey = Users();
  ferganey.name = "ferganey";
  ferganey.printname();

  constructor c1 = constructor("mariam");
  constructor c2 = constructor("ahmed");

  /// The above code is attempting to create an instance of a `person` class with a default constructor in
  /// Dart. However, there are some issues in the code:
  /// 1. The `person` class definition is missing.
  /// 2. The constructor invocation should use the `new` keyword.
  /// 3. The `greet()` method is being called on the `person` instance, assuming it exists in the `person`
  /// class.
  // // 1. Default constructor
  // var person = person("Ahmed", 25);
  // person.greet();

  // 2. Named constructor
  var square = shape.square(5);
  var rectangle = shape.rectange(3, 6);
  square.describe();
  rectangle.describe();

  // 3. Factory constructor
  var logger1 = logger("App");
  var logger2 = logger("App");
  logger1.log("Started successfully.");
  print("Logger instances are identical: ${identical(logger1, logger2)}");

  // 4. Singleton via private constructor
  var config = configmanager();
  config.show();

  // 5. Const constructor
  const p1 = Point(1, 2);
  const p2 = Point(1, 2);
  p1.printPosition();
  print("Points are identical: ${identical(p1, p2)}");

  // 6. Redirecting constructor
  var ant = Animal.insect("Ant");
  ant.info();

  // usersenc._balance = "1000";
  usersenc user = usersenc();
  user.setBalance("1000");
  print("getbalance: ${user.getBalance()}");
}

////////////////////////////////////////////////////////////////////////////////

/// Application 1

// void main(List<String> arguments) {
//   print("=== Dart Full Project ===");

//   // Variables & Types
//   var name = "mariam";
//   final nickname = "mimo";
//   const country = "Egypt";
//   print("I love $name ($nickname) from $country");

//   // Numbers & Conversion
//   String strNum = "7";
//   int parsed = int.parse(strNum);
//   print("Parsed int: $parsed");

//   double num1 = 7.7;
//   print("Double: ${num1.runtimeType}, toInt: ${num1.toInt()}");

//   // Arithmetic
//   print("2 / 7 = ${2 / 7}");
//   print("2 ~/ 7 = ${2 ~/ 7}");
//   print("7 % 3 = ${7 % 3}");

//   // Increment Operators
//   int inc = 0;
//   print("Post-increment: ${inc++}");
//   print("Pre-increment: ${++inc}");

//   // Logical
//   print("!(true && true): ${!(3 > 1 && 2 < 4)}");
//   /// these are all 15 string methods  Ex:  
//   /// string methods like toUpperCase, trim, contains, replaceAll and 
//   // String methods
//   String str = " Hello World ";
//   print(str.toUpperCase());
//   print("Trim");
//   print(str.trim().contains("World"));
//   print(str.replaceAll("World", "Dart"));

//   // Compare
//   print("Compare: ${"mariam".compareTo("Mariam")}");

//   // Null-aware operators
//   String? nullableString;
//   print(nullableString ?? "Default Value");

//   String? name3 = null;
//   print(name3 ?? "No Name"); // ➜ prints: No Name
//   name3 = "ahmed";
//   print(name3 ?? "No Name"); // ➜ prints: Ahmed


//   // Input
//   stdout.write("Enter your name: ");
//   String? yourName = stdin.readLineSync() ?? "Unknown";

//   stdout.write("Enter your number: ");
//   int yourNum = int.tryParse(stdin.readLineSync() ?? "") ?? 0;

//   print("Your name is $yourName and your number is $yourNum");

//   // Conditional
//   stdout.write("Enter a key: ");
//   String? key = stdin.readLineSync();
//   if (key == "mariam") {
//     print("Welcome mariam");
//   } else if (key == "ferganey") {
//     print("Welcome ferganey");
//   } else {
//     print("Access denied");
//   }

//   // Enum usage
//   stdout.write("Enter day (mon/tue/wed): ");
//   String? inputDay = stdin.readLineSync();
//   Day? day = Day.values.firstWhere((e) => e.name == inputDay, orElse: () => Day.unknown);
//   switch (day) {
//     case Day.mon:
//       print("Start of week!");
//       break;
//     case Day.tue:
//     case Day.wed:
//       print("Midweek days");
//       break;
//     default:
//       print("Unknown day");
//   }

//   // Try-catch
//   try {
//     stdout.write("Enter number A: ");
//     int a = int.parse(stdin.readLineSync()!);
//     stdout.write("Enter number B: ");
//     int b = int.parse(stdin.readLineSync()!);
//     print("Sum: ${add(a, b)}");
//   } catch (e) {
//     print("Invalid input: $e");
//   }

//   // Assertion
//   assert(key == "mariam", "Key must be mariam");

//   // Loops
//   print("For loop:");
//   for (int i = 0; i < 3; i++) {
//     print(i);
//   }

//   print("While loop:");
//   int x = 0;
//   while (x < 2) {
//     print("x = $x");
//     x++;
//   }

//   // Collections
//   List<String> fruits = ["apple", "banana", "cherry"];
//   fruits.forEach((f) => print("Fruit: $f"));
//   print("Mapped fruits: ${fruits.map((e) => e.toUpperCase()).toList()}");

//   Map<String, int> scores = {"mariam": 100, "ferganey": 90};
//   scores.forEach((k, v) => print("$k has score $v"));

//   Set<int> nums = {1, 2, 2, 3};
//   print("Unique nums: $nums");

//   // Higher-order function
//   List<int> numbers = [1, 2, 3, 4];
//   print("Even numbers: ${numbers.where((e) => e % 2 == 0).toList()}");
//   int sum = numbers.reduce((a, b) => a + b);
//   print("Sum using reduce: $sum");

//   // Function usage
//   greet("Ahmed");
//   greet("Mariam", greeting: "Salam");
//   greet("Ali", greeting: "Hi", punctuation: "!!!");

//   // Class usage
//   Person p1 = Person(name: "Mariam", age: 22);
//   p1.sayHello();

//   // Recursive function
//   print("Factorial(5): ${factorial(5)}");

//   // Random number
//   var random = Random();
//   int rand = random.nextInt(100);
//   print("Random number: $rand");

//   // DateTime
//   DateTime now = DateTime.now();
//   print("Now: $now | Year: ${now.year}");

//   // File I/O
//   File file = File("output.txt");
//   file.writeAsStringSync("Hello Dart World!\nTime: $now\n", mode: FileMode.append);
//   print("File written: ${file.path}");
// }

// /// Enum
// enum Day { mon, tue, wed, unknown }

// /// Functions
// int add(int a, int b) => a + b;

// void greet(String name, {String greeting = "Hello", String punctuation = "."}) {
//   print("$greeting, $name$punctuation");
// }

// /// Recursive factorial
// int factorial(int n) => (n <= 1) ? 1 : n * factorial(n - 1);

// /// Class
// class Person {
//   String name;
//   int age;

//   Person({required this.name, required this.age});

//   void sayHello() {
//     print("Hi, I am $name and I am $age years old.");
//   }
// }


////////////////////////////////////////////////////////////////////////////////

/// Applicatiom  2

// void main(List<String> arguments) {
//   print("=== Dart Full List Framework ===");

//   // Simple list operations
//   List str = ["mariam", "ahmed", "ali"];
//   print("Length: ${str.length}");
//   print("Is empty: ${str.isEmpty}");
//   print("Reversed: ${str.reversed.toList()}");
//   print("First item: ${str[0]}");
//   print("Index of 'mariam': ${str.indexOf("mariam")}");

//   // Single element list
//   List strsingle = ["ali"];
//   print("Single value: ${strsingle.single}");

//   // Constant list
//   const List constantName = ["ahmed&mariam"];
//   print("Constant list: $constantName");

//   // Adding items
//   List adding = ["ahmed", "mariam", "azza", "rania"];
//   adding.add("ali");
//   adding.addAll(["sara", "mona"]);
//   adding.insertAll(0, ["Yara", "Hassan"]);
//   print("List after additions: $adding");

//   // Iteration using forEach
//   adding.forEach((name) {
//     print("Hello $name");
//   });

//   // Map to new values
//   print("Mapped to upper case: ${adding.map((e) => "Welcome ${e.toUpperCase()}").toList()}");

//   // Removing elements
//   adding.removeAt(0);
//   adding.removeRange(0, 2);
//   adding.replaceRange(3, 5, ["ahmed", "ahmed&mariam"]);
//   print("After remove/replace: $adding");

//   // 3D list
//   List _3D = [
//     [
//       [1, 2, 3],
//       [4, 5, 6],
//       [7, 8, 9],
//     ],
//     [
//       [74, 77, 35],
//       [41, 52, 63],
//       [74, 28, 96],
//     ],
//   ];
//   print("3D List: $_3D");
//   print("Element [1][2][1]: ${_3D[1][2][1]}");

//   // Shape detection
//   int depth = _3D.length;
//   int rows = _3D[0].length;
//   int cols = _3D[0][0].length;
//   print("Shape: [$depth][$rows][$cols]");

//   // List dimension detection
//   void printDimension(dynamic list) {
//     if (list is List) {
//       if (list.isNotEmpty && list[0] is List) {
//         if (list[0].isNotEmpty && list[0][0] is List) {
//           print("3D List");
//         } else {
//           print("2D List");
//         }
//       } else {
//         print("1D List");
//       }
//     } else {
//       print("Not a List");
//     }
//   }

//   print("Dimension Check:");
//   printDimension(str);
//   printDimension([[1, 2], [3, 4]]);
//   printDimension(_3D);

//   // Merge two lists
//   List l1 = ["ahmed"];
//   List l2 = ["mariam"];
//   List merged = [...l1, ...l2];
//   print("Merged List: $merged");

//   // Filter list
//   List number = [1, 2, 3, 4, 5, 6, 7];
//   var filtered = number.where((element) => element >= 3);
//   print("Filtered >=3: ${filtered.toList()}");

//   // Extra: sort and reverse
//   List unsorted = [9, 2, 5, 1, 7];
//   unsorted.sort();
//   print("Sorted: $unsorted");
//   print("Reversed: ${unsorted.reversed.toList()}");

// }

////////////////////////////////////////////////////////////////////////////////

/// Applicatiom  3

  // print("=== Dart Full Set Project ===");

  // // Creating a Set
  // Set<String> names = {"Ahmed", "Mariam", "Ali", "Ahmed"};
  // print("Initial Set: $names"); // Note: "Ahmed" will appear only once

  // print(names.elementAt(0));

  // // Checking length
  // print("Length: ${names.length}");

  // // Checking if set is empty
  // print("Is Empty: ${names.isEmpty}");
  // print("Is Not Empty: ${names.isNotEmpty}");

  // // Adding elements
  // names.add("Sara");
  // print("After Adding Sara: $names");

  // names.addAll(["Rania", "Ali", "Mona"]);
  // print("After Adding Multiple: $names");

  // // Removing elements
  // names.remove("Ali");
  // print("After Removing Ali: $names");

  // // Containment
  // print("Contains Mariam: ${names.contains("Mariam")}");
  // print("Contains Ahmed: ${names.contains("Ahmed")}");

  // // Looping
  // print("Printing each name:");
  // for (var name in names) {
  //   print("-> $name");
  // }

  // // Using forEach
  // print("Using forEach:");
  // names.forEach((name) => print("Hello $name"));

  // // Set operations
  // Set<String> setA = {"Ahmed", "Ali", "Mariam"};
  // Set<String> setB = {"Mariam", "Sara", "Yara"};

  // print("Set A: $setA");
  // print("Set B: $setB");

  // print("Union: ${setA.union(setB)}"); // All unique elements
  // print("Intersection: ${setA.intersection(setB)}"); // Common elements
  // print("Difference A - B: ${setA.difference(setB)}"); // Only in A

  // // Converting Set to List
  // List<String> nameList = names.toList();
  // print("Converted Set to List: $nameList");

  // // Converting List to Set (for removing duplicates)
  // List<String> duplicatedList = ["Ali", "Ali", "Ahmed", "Ahmed", "Sara"];
  // Set<String> uniqueNames = Set.from(duplicatedList);
  // print("Unique from List: $uniqueNames");

  // // Creating empty set with proper type
  // var emptySet = <int>{};
  // emptySet.add(10);
  // emptySet.add(20);
  // print("Empty int Set filled: $emptySet");

  // // Set with numbers: check even/odd
  // Set<int> numbers = {1, 2, 3, 4, 5, 6};
  // var even = numbers.where((n) => n.isEven);
  // print("Even Numbers: $even");

  // var odd = numbers.where((n) => n.isOdd);
  // print("Odd Numbers: $odd");
  // 
  
////////////////////////////////////////////////////////////////////////////////

/// Applicatiom  4

  // print("=== Dart Full Map Project ===");

  // // Creating a map with keys and values
  // Map<String, String> user = {
  //   "name": "Ahmed",
  //   "city": "Cairo",
  //   "job": "Engineer",
  // };
  // print("User Map: $user");

  // // Accessing values
  // print("Name: ${user["name"]}");
  // print("City: ${user["city"]}");

  // // Adding a new key-value pair
  // user["age"] = "26";
  // print("After adding age: $user");

  // // Updating a value
  // user["city"] = "Alexandria";
  // print("After updating city: $user");

  // // Removing a key
  // user.remove("job");
  // print("After removing job: $user");

  // // Check if key/value exists
  // print("Contains key 'name': ${user.containsKey("name")}");
  // print("Contains value 'Ahmed': ${user.containsValue("Ahmed")}");

  // // Getting all keys and values
  // print("Keys: ${user.keys}");
  // print("Values: ${user.values}");

  // // Iterating through a map
  // print("Looping through entries:");
  // user.forEach((key, value) {
  //   print("$key -> $value");
  // });

  // // Map with different data types
  // Map<String, dynamic> mixed = {
  //   "name": "Mariam",
  //   "age": 25,
  //   "married": false,
  // };
  // print("Mixed Map: $mixed");

  // // Creating an empty map
  // Map<String, int> scores = {};
  // scores["Ali"] = 90;
  // scores["Sara"] = 88;
  // print("Scores: $scores");

  // // Get value with default fallback
  // print("Score of Ahmed: ${scores["Ahmed"] ?? "Not Found"}");

  // // Using map entries
  // for (var entry in scores.entries) {
  //   print("${entry.key} scored ${entry.value}");
  // }

  // // Converting list to map
  // List<String> keys = ["a", "b", "c"];
  // List<int> values = [1, 2, 3];
  // Map<String, int> newMap = Map.fromIterables(keys, values);
  // print("New map from two lists: $newMap");

  // // Nested Map
  // Map<String, Map<String, dynamic>> users = {
  //   "user1": {"name": "Ali", "age": 22},
  //   "user2": {"name": "Nora", "age": 28},
  // };
  // print("Nested Users Map: $users");
  // print("Name of user1: ${users["user1"]?["name"]}");


////////////////////////////////////////////////////////////////////////////////

/// Application 5

//   print("=== Dart Functions Examples ===");

//   // 1. Simple function call
//   greet();

//   // 2. Function with parameters
//   greetUser("Ahmed");

//   // 3. Function with return value
//   int sum = add(5, 10);
//   print("Sum: $sum");

//   // 4. Arrow function
//   print("Square of 4: ${square(4)}");

//   // 5. Function with optional positional parameter
//   describeUser("Mariam");
//   describeUser("Mariam", 25);

//   // 6. Function with named parameters
//   printUserInfo(name: "Ali", age: 30);
//   printUserInfo(age: 22, name: "Sara");

//   // 7. Named parameters with default values
//   greetPerson(name: "Mohamed");
//   greetPerson();
//   greetPersonQuestion(name: "Mariam");
//   // 8. Anonymous function
//   var list = [1, 2, 3];
//   list.forEach((num) {
//     print("Item: $num");
//   });

//   // 9. Higher-order function (takes a function as parameter)
//   executeFunction(multiply, 3, 4);

//   // 10. Returning function from another function
//   var triple = makeMultiplier(3);
//   print("Triple of 5: ${triple(5)}");
// }

// // Function with no parameters or return
// void greet() {
//   print("Hello, welcome to Dart!");
// }

// // Function with parameters
// void greetUser(String name) {
//   print("Hello, $name!");
// }

// // Function with return value
// int add(int a, int b) {
//   return a + b;
// }

// // Arrow function
// int square(int x) => x * x;

// // Optional positional parameter
// void describeUser(String name, [int? age]) {
//   print("Name: $name");
//   if (age != null) print("Age: $age");
// }

// // Named parameters
// void printUserInfo({required String name, required int age}) {
//   print("User: $name, Age: $age");
// }

// // Named parameters with default values
// void greetPerson({String name = "Guest"}) {
//   print("Hello, $name!");
// }

// // Named parameters with default values
// void greetPersonQuestion({String? name}) {
//   print("Hello, $name!");
// }

// // Higher-order function: takes function as argument
// void executeFunction(int Function(int, int) op, int a, int b) {
//   print("Result: ${op(a, b)}");
// }

// int multiply(int a, int b) => a * b;

// // Returning a function
// Function makeMultiplier(int factor) {
//   return (int x) => x * factor;
// }

////////////////////////////////////////////////////////////////////////////////

/// Application 6


// void main(List<String> arguments) {
//   print("=== Dart Project Entry Point ===");

//   // You can add your Dart code here.
//   // For example, you can call functions, create classes, etc.
//   // This is just a placeholder to show where your main logic would go.
//   List users = ["ahmed", "mariam", "ali"];
//   var seg = users.take(2);
//   print(seg);
//   var segskip = users.skip(2);
//   print(segskip);
//   var numbers = List.generate(10, (index) => index + 1); // [1,2,...,10]
//   print(numbers);
//   var middleThree = numbers.skip(3).take(3);
//   print(middleThree); // (4, 5, 6)

//   List numbersfold = [1, 2, 3, 4, 5];
//   var resfold = numbersfold.fold(4, (previousvalue, element) {
//     print(element);
//     print(previousvalue);
//     return element + previousvalue;
//   });
//   print(resfold); // 20

//   var resred = numbersfold.reduce((previousvalue, element) {
//     print(element);
//     print(previousvalue);
//     return element + previousvalue;
//   });
//   print(resred); // 20

//   // Nullable example
//   int? userAge = 28;
//   print('User age: $userAge');

//   userAge = null;
//   print('User age after update: $userAge');

//   int displayAge = userAge ?? 18;
//   print('Display age: $displayAge');

//   String? nameFromAPI;
//   String userName = nameFromAPI ?? 'Guest';
//   print('User name: $userName');

//   nameFromAPI ??= 'Unknown';
//   print('Final name: $nameFromAPI');

//   String? city;
//   print('City name length: ${city?.length}');

//   String? gender = getUserGender();
//   String resultGender = gender!;
//   print('User gender: $resultGender');

//   // ========= Demonstrating `late` keyword =========

//   late String welcomeMessage; // Declared but not initialized immediately

//   if (resultGender == 'Male') {
//     welcomeMessage = 'Welcome, Mr. $userName';
//   } else {
//     welcomeMessage = 'Welcome, Ms. $userName';
//   }

//   print(
//     welcomeMessage,
//   ); // Will crash if `welcomeMessage` is accessed before initialization

//   // List <int> = [1,2,3,4,null];
//   List<int?> numbersnul = [1, 2, 3, 4, null];
//   print(numbersnul);

//   Map<String, String?> usersmap = {"name": "mariam", "Age": null};
//   print(usersmap);

//   print("Hello, Dart World!");
// }

// /// Simulated backend function
// String? getUserGender() {
//   // return null; // Uncomment to test null crash
//   // return null; //Null check operator used on a null value
//   return 'Male';
// }

////////////////////////////////////////////////////////////////////////////////

/// Application 7

// /// This is the main entry point for the Dart project.
// library;
// import 'dart:io';

// void main(List<String> arguments) {
//   print("=== Dart Project Entry Point ===");
//   // Simulating sign-in inputs (in real app these come from user input)
//   String? inputEmail;
//   String? inputPassword;

//   // Null-aware assignment
//   inputEmail ??= 'user@example.com';
//   inputPassword ??= '123456';

//   // Null coalescing: fallback to "Unknown"
//   String email = inputEmail ?? 'Unknown';
//   String password = inputPassword ?? 'Unknown';

//   // Using null assertion (!)
//   // (Be sure these aren't null at this point)
//   String verifiedEmail = email!;
//   String verifiedPassword = password!;

//   // Using late variable: initialized later
//   late String signInMessage;

//   if (signIn(verifiedEmail, verifiedPassword)) {
//     signInMessage = '✅ Sign in successful. Welcome, $verifiedEmail!';
//   } else {
//     signInMessage = '❌ Sign in failed. Please check credentials.';
//   }

//   print(signInMessage);

// ////////////////////////////////////////////////////////////////////////////////
//   List<Map<String, String>> users = [
//     {"username": "thaer", "password": "thaer123"},
//     {"username": "admin", "password": "admin123"},
//   ];

//   stdout.write("Enter Your Username: ");
//   String? username = stdin.readLineSync();

//   stdout.write("Enter Your Password: ");
//   String? password2 = stdin.readLineSync();

//   Map<String, String> res = users.firstWhere(
//     (element) =>
//         element['username'] == username && element['password'] == password2,
//     orElse: () => {"username": "", "password": ""},
//   );

//   if (res['username'] == "") {
//     print("❌ User Not Found");
//   } else {
//     print("✅ Welcome, ${res['username']}!");
//   }

//   print("Hello, Dart World!");
// }

// /// Simulated sign-in logic
// bool signIn(String email, String password) {
//   // Normally you'd check against a DB here
//   const storedEmail = 'user@example.com';
//   const storedPassword = '123456';

//   return email == storedEmail && password == storedPassword;
// }


////////////////////////////////////////////////////////////////////////////////

/// Application 8


// import 'dart:io';

// class DataFormatException implements Exception {
//   final String message;
//   DataFormatException(this.message);
// }

// void main() {
//   // Exception: Base class for all exceptions you can throw/catch.
//   // Error: Base class for serious errors that shouldn't usually be caught.

//   // StateError: Operation was called in an invalid state.
//   // Example: Accessing an iterator after it's done.

//   // ArgumentError: Invalid argument passed to a function.
//   // Example: passing null to a function that doesn't allow it.

//   // RangeError: A value is outside the valid range.
//   // Example: Accessing index 10 in a list of length 5.

//   // UnsupportedError: An unsupported operation was attempted.
//   // Example: modifying an unmodifiable list.

//   // UnimplementedError: A function that has not been implemented yet.
//   // Often used as a placeholder during development.

//   // FormatException: A string failed to parse as expected.
//   // Example: parsing 'abc' as a number.

//   // TypeError: A value of the wrong type was used.
//   // Example: assigning a String to an int variable.

//   // CastError: An object couldn't be cast to the expected type.
//   // Example: casting Object to int when it's actually a String.

//   // IOException: Generic I/O error (base for file and network errors).

//   // FileSystemException: Thrown when reading/writing files fails.
//   // Example: file not found, permission denied, etc.

//   // SocketException: Thrown when a network socket error occurs.
//   // Example: no internet connection.

//   // HttpException: Thrown when an HTTP request fails.
//   // Example: 404 Not Found, bad response, etc.

//   // ProcessException: Thrown when starting or running a subprocess fails.

//   // TimeoutException: Thrown when an operation times out.
//   // Example: HTTP request or async task takes too long.

//   // IsolateSpawnException: Thrown when an isolate (parallel process) fails to start.

//   // IntegerDivisionByZeroException: Thrown on integer division by zero (~/ operator).

//   // Custom Exception Example:
//   // class MyCustomException implements Exception {
//   //   final String message;
//   //   MyCustomException(this.message);
//   // }

//   final filePath = 'data.txt';

//   try {
//     print('📂 Reading file: $filePath');
//     final file = File(filePath);

//     if (!file.existsSync()) {
//       throw FileSystemException("File not found", filePath);
//     }

//     final lines = file.readAsLinesSync();
//     if (lines.isEmpty) {
//       throw DataFormatException("File is empty.");
//     }

//     final numbers = <double>[];

//     for (var line in lines) {
//       try {
//         final value = double.parse(line.trim());
//         numbers.add(value);
//       } catch (_) {
//         throw DataFormatException("Invalid number format in line: '$line'");
//       }
//     }

//     final avg = numbers.reduce((a, b) => a + b) / numbers.length;
//     print("✅ Average value: $avg");

//   } on FileSystemException catch (e) {
//     print("🛑 File Error: ${e.message} (${e.path})");

//   } on DataFormatException catch (e) {
//     print("📉 Data Error: ${e.message}");

//   } catch (e) {
//     print("❌ Unknown Error: $e");

//   } finally {
//     print("🔁 File processing completed.");
//   }
// }

////////////////////////////////////////////////////////////////////////////////

/// Application 9

// import 'dart:io';
// import 'functions.dart' show add;
// import 'dart:convert' as convert;
// import 'package:http/http.dart' as http;
// void main(List<String> arguments) async  {
//   double x = 3;
//   print(x);
//   // double res = add(1, 2); //type 'int' is not a subtype of type 'double'
//   double res = add(1.0, 2.0); // works fine

//   // This example uses the Google Books API to search for books about http.
//   // https://developers.google.com/books/docs/overview
//   var url =
//       Uri.https('www.googleapis.com', '/books/v1/volumes', {'q': '{http}'});

//   // Await the http get response, then decode the json-formatted response.
//   var response = await http.get(url);
//   if (response.statusCode == 200) {
//     var jsonResponse =
//         convert.jsonDecode(response.body) as Map<String, dynamic>;
//     var itemCount = jsonResponse['totalItems'];
//     print('Number of books about http: $itemCount.');
//   } else {
//     print('Request failed with status: ${response.statusCode}.');
//   }


//   print(res);
// }

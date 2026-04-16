import 'package:flutter/material.dart';

void main() {
  runApp(const SimpleCartApp());
}

class SimpleCartApp extends StatefulWidget {
  const SimpleCartApp({super.key});

  @override
  State<SimpleCartApp> createState() => _SimpleCartAppState();
}

class _SimpleCartAppState extends State<SimpleCartApp> {
  bool isDarkTheme = false;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: isDarkTheme ? ThemeData.dark() : ThemeData.light(),
      home: ProductListScreen(
        onToggleTheme: () => setState(() => isDarkTheme = !isDarkTheme),
      ),
    );
  }
}

// Dummy Product Model
class Product {
  final String name;
  final double price;
  final String category;

  Product(this.name, this.price, this.category);
}

List<Product> allProducts = [
  Product("T-shirt", 25, "Clothing"),
  Product("Shoes", 80, "Footwear"),
  Product("Watch", 150, "Accessories"),
  Product("Jeans", 40, "Clothing"),
  Product("Sneakers", 100, "Footwear"),
];

// Product List Screen
class ProductListScreen extends StatefulWidget {
  final VoidCallback onToggleTheme;
  const ProductListScreen({super.key, required this.onToggleTheme});

  @override
  State<ProductListScreen> createState() => _ProductListScreenState();
}

class _ProductListScreenState extends State<ProductListScreen>
    with SingleTickerProviderStateMixin {
  List<Product> cart = [];
  String selectedCategory = 'All';
  bool showOnlyAffordable = false;

  late AnimationController _animController;

  @override
  void initState() {
    super.initState();
    _animController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 300),
      lowerBound: 0.9,
      upperBound: 1.0,
    )..forward();
  }

  @override
  void dispose() {
    _animController.dispose();
    super.dispose();
  }

  List<Product> get filteredProducts {
    return allProducts.where((product) {
      if (selectedCategory != 'All' && product.category != selectedCategory) {
        return false;
      }
      if (showOnlyAffordable && product.price > 50) {
        return false;
      }
      return true;
    }).toList();
  }

  void addToCart(Product product) {
    setState(() {
      cart.add(product);
    });
  }

  void removeFromCart(Product product) {
    setState(() {
      cart.remove(product);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("🛒 SimpleCart"),
        actions: [
          IconButton(
            icon: const Icon(Icons.color_lens),
            onPressed: widget.onToggleTheme,
            tooltip: "Toggle Theme",
          ),
          IconButton(
            icon: const Icon(Icons.shopping_cart),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => CartScreen(cart: cart),
                ),
              );
            },
          ),
        ],
      ),
      body: Column(
        children: [
          // Filters
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                DropdownButton<String>(
                  value: selectedCategory,
                  items: ['All', 'Clothing', 'Footwear', 'Accessories']
                      .map((cat) =>
                          DropdownMenuItem(value: cat, child: Text(cat)))
                      .toList(),
                  onChanged: (value) {
                    setState(() {
                      selectedCategory = value!;
                    });
                  },
                ),
                const SizedBox(width: 20),
                Checkbox(
                  value: showOnlyAffordable,
                  onChanged: (val) =>
                      setState(() => showOnlyAffordable = val!),
                ),
                const Text("Under \$50")
              ],
            ),
          ),
          // Product Grid
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(8),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2, childAspectRatio: 3 / 2),
              itemCount: filteredProducts.length,
              itemBuilder: (_, index) {
                final product = filteredProducts[index];
                return ScaleTransition(
                  scale: _animController,
                  child: Card(
                    elevation: 4,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(product.name,
                            style:
                                const TextStyle(fontWeight: FontWeight.bold)),
                        Text("\$${product.price.toStringAsFixed(2)}"),
                        ElevatedButton(
                          onPressed: () => addToCart(product),
                          child: const Text("Add to Cart"),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

// Cart Screen with ListView.separated Toggle
class CartScreen extends StatefulWidget {
  final List<Product> cart;

  const CartScreen({super.key, required this.cart});

  @override
  State<CartScreen> createState() => _CartScreenState();
}

class _CartScreenState extends State<CartScreen> {
  bool useSeparated = false;

  @override
  Widget build(BuildContext context) {
    double total = widget.cart.fold(0, (sum, item) => sum + item.price);

    return Scaffold(
      appBar: AppBar(title: const Text("🛍️ Your Cart")),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Use Separated List"),
                Switch(
                  value: useSeparated,
                  onChanged: (val) {
                    setState(() {
                      useSeparated = val;
                    });
                  },
                ),
              ],
            ),
          ),
          Expanded(
            child: widget.cart.isEmpty
                ? const Center(child: Text("Your cart is empty"))
                : useSeparated
                    ? ListView.separated(
                        itemCount: widget.cart.length,
                        separatorBuilder: (_, __) => const Divider(),
                        itemBuilder: (_, index) {
                          final product = widget.cart[index];
                          return ListTile(
                            title: Text(product.name),
                            trailing:
                                Text("\$${product.price.toStringAsFixed(2)}"),
                          );
                        },
                      )
                    : ListView.builder(
                        itemCount: widget.cart.length,
                        itemBuilder: (_, index) {
                          final product = widget.cart[index];
                          return ListTile(
                            title: Text(product.name),
                            trailing:
                                Text("\$${product.price.toStringAsFixed(2)}"),
                          );
                        },
                      ),
          ),
          Padding(
            padding: const EdgeInsets.all(16),
            child: Text(
              "Total: \$${total.toStringAsFixed(2)}",
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          )
        ],
      ),
    );
  }
}

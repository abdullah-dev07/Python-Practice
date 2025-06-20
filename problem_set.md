
# Python Concepts Practice Problems


## 1 Deep Copy vs Shallow Copy

**Problem:**

You are given a list of students where each student is represented as a list containing name and a list of grades:

```python
students = [
    ["Ali", [90, 80]],
    ["Sara", [85, 75]],
    ["John", [70, 60]]
]
````

* Make a shallow copy and deep copy of `students`.
* Change the first grade of "Ali" to 100 in both copies.
* Print original, shallow copy, and deep copy and observe differences.

---

## 2 Decorators

**Problem:**

Write a decorator called `log_execution` that:

* Prints "Starting function" before a function runs.
* Prints "Function finished" after the function runs.
* Apply it to a function `calculate_sum(a, b)` that returns the sum of two numbers.

---

## 3 Iterators

**Problem:**

Create a custom iterator class `SquareIterator` that:

* Accepts `n` and generates squares of numbers from 1 to `n`.
* Example: for `n = 5` → should yield 1, 4, 9, 16, 25.

---

## 4 File Handling

**Problem:**

You are given a file `students.txt` containing:

```
Ali,90
Sara,85
John,70
```

* Read this file and store data as a dictionary `{name: score}`.
* Add 5 bonus marks to every student and write the updated scores to a new file `updated_students.txt`.

---

## 5 OOP: Classes and Objects

**Problem:**

Design a class `BankAccount` with:

* Attributes: `account_number`, `balance`
* Methods:

  * `deposit(amount)`
  * `withdraw(amount)`
  * `display_balance()`

Create an object and demonstrate deposits and withdrawals.

---

## 6 Inheritance

**Problem:**

Create a base class `Vehicle` with:

* Attributes: `make`, `model`
* Method: `display_info()`

Create subclasses `Car` and `Motorcycle` that inherit from `Vehicle`, but:

* Add specific attributes like `number_of_doors` for Car, and `engine_cc` for Motorcycle.
* Override `display_info()` to include subclass attributes.

---

## 7 Polymorphism

**Problem:**

Create a function `vehicle_sound()` that accepts any object of class `Car` or `Motorcycle` (from problem 6).

* Each subclass should have a method `make_sound()`.
* Call `vehicle_sound()` with both objects and use polymorphism to call correct sound.

---

## 8 Generators

**Problem:**

Write a generator function `fibonacci_generator(n)` that yields first `n` Fibonacci numbers.

* Test it with `n = 10`.

---

## 9 Combined Problem (Bonus Challenge)

**Problem:**

Build a **Student Management System**:

* Use:

  * OOP for Student class
  * File handling to save/load student data
  * Decorators for logging student creation
  * Iterators to iterate over student list
  * Deep copy to create backup of student data

---

## 10 Lists

**Problem:**

Remove duplicates from a list without using set.


---

## 11 Combined Problem (Bonus Challenge No. 2)

**Problem:**

Build a Library Management System that includes the following functionality:

✅ Requirements & Concepts to Use

**OOP**:

* Create a Book class with attributes like title, author, ISBN, and availability status.
* Create a Library class to manage books.

**File Handling**:

* Save the book inventory to a file (library_data.txt)

* Load the book inventory from the file on startup

**Decorators**:

* Create a decorator to log every book addition or removal to/from the library, printing a message like "Book added: [title]".

**Iterators**:

* Implement a custom iterator in the Library class to iterate over all books that are currently available.

**Deep Copy**:

* Implement a method that returns a deep copy of the current book inventory so that changes can be made safely (e.g., for admin testing or backup).

---

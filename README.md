# Smart Grocery List

Smart Grocery List is a Python application that automatically generates a grocery list based on user-selected recipes and dietary preferences. The user provides their dietary preferences (vegetarian, gluten-free, etc.), selects recipes for the week, and the program compiles the required ingredients into a convenient, organized grocery list, taking into account the ingredients the user already has.

## Features

- Easy user registration and authentication
- Add, update, and manage dietary preferences
- Select and manage favorite recipes from a recipe database
- Automatically generate grocery lists based on selected recipes and user preferences

## Installation

1. Clone the project repository:

   ```
   git clone https://github.com/yourusername/smart_grocery_list.git
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # or "venv\Scripts\activate" on Windows
   ```

3. Install required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```
python -m app.main
```

The application supports various command line arguments for managing user accounts, adding recipes, and generating grocery lists. Please refer to the built-in help by running:

```
python -m app.main --help
```

For example, to create a user account, run:

```
python -m app.main --new-user --username username --email email@example.com
```

To add recipes to your list, run:

```
python -m app.main --add-recipes 1 2 3
```

To generate a grocery list, run:

```
python -m app.main --generate-list
```

## Contributions

Contributions are welcome! Please feel free to submit pull requests or open issues on this repository.

## License

This project is released under the MIT License.
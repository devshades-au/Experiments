# Inventory Management System

Welcome to the Inventory Management System! This Flask-based web application helps you manage your inventory assets efficiently.

## Features

- **Track Assets**: Keep track of hardware assets easily.
- **Add New Assets**: Add new assets to your inventory seamlessly.
- **Search and Filter**: Search and filter assets based on various criteria.
- **View Details**: View detailed information about each asset.
- **Edit and Delete**: Edit or delete existing assets as needed.

## Requirements

- Python 3.x
- Flask
- MySQL Server
- MySQL Connector/Python
- Python-dotenv

## Installation

1. **Clone the Repository**: 
git clone <repository-url>
cd <repository-directory>

2. **Install Dependencies**: 
pip install -r requirements.txt


3. **Configure Database**: 
- Create a `.env` file in the root directory.
- Configure your database connection details:
  ```
  DB_HOST=localhost
  DB_USER=<your-database-username>
  DB_PASSWORD=<your-database-password>
  DB_NAME=<your-database-name>
  ```

4. **Set up Database**: 
- Execute the SQL script (`database.sql`) to create the necessary tables in your MySQL database.

5. **Run the Application**: 
python app.py


6. **Access the Application**: 
- Access the application in your web browser at `http://localhost:5000`.

## Usage

- Navigate to the home page (`/`) to get started.
- Use the navigation links to access different features:
- `/inventory` - View all inventory assets
- `/add_asset` - Add a new asset to the inventory
- `/search` - Search for assets based on keywords
- Edit or delete existing assets using the provided options in the inventory view.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).



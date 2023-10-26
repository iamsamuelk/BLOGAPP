BLOGAPP

BLOGAPP is a simple backend based Blog App for creating, reading, updating, and deleting blog posts. It provides a platform for users to share their thoughts, articles, and stories.

## Features

- **User Authentication**: Users can create accounts and log in.

- **Create Blog Posts**: Registered users can create new blog posts, which consists of a title and body.

- **Read Blog Posts**: Users can view a list of blog posts and read the full content of each post.

- **Update Blog Posts**: Authors can edit and update their own blog posts.

- **Delete Blog Posts**: Authors can delete their own blog posts.

- **Timestamps**: Each blog post is timestamped with the creation date and the date of the last update.

- **User Permissions**: Only the author of a blog post can edit or delete it.



## Technologies Used

- **FastAPI**: The web framework for building the backend of the application.

- **SQLAlchemy**: The SQL toolkit and Object-Relational Mapping (ORM) for database management.

- **SQLite**: The lightweight, serverless database used to store blog data.

- **JWT (JSON Web Tokens)**: Used for user authentication and authorization.



## Installation

1. Clone the repository: `git clone https://github.com/iamsamuelk/BLOGAPP.git`

2. Change directory to the project folder: `cd BLOGAPP`

3. Install dependencies: `pip install -r requirements.txt`

4. Activate virtual environment `source env/bin/activate`

5. Run the application: `uvicorn blog.main:app --reload`



## Usage

1. Access the application in your web browser by visiting `http://localhost:8000`.

2. Create a user account and log in.

3. Start creating, reading, updating, and deleting blog posts.




## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your fork locally.

3. Create a new branch for your feature or bug fix.

4. Make your changes and commit them.

5. Push your changes to your fork on GitHub.

6. Create a pull request to the original repository.

Please ensure that your code follows the project's coding standards and conventions.



## License

This project is licensed under the [MIT License](LICENSE). You are free to use and modify this project for your purposes.



## Contact

If you have any questions or suggestions regarding the project, feel free to contact us at [samuel.kwuelum@gmail.com](mailto:samuel.kwuelum@gmail.com).

Thank you for using BLOGAPP! We hope you find it useful for your blogging needs.
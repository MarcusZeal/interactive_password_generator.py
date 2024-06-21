# Interactive Password Generator

This project provides a Python-based interactive password generator script that allows users to create random passwords with customizable options. You can specify the total length of the password and the number of special characters included.

## Features

- Generate random passwords of specified length.
- Include a customizable number of special characters.
- Interactive command-line interface for user input.
- Docker support for running the script and tests in an isolated environment.

## Requirements

- Python 3.6 or higher
- Docker (optional, for running the script and tests in a Docker container)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/MarcusZeal/interactive_password_generator.git
   cd interactive_password_generator
   ```

2. Ensure you have Python 3.6 or higher installed. You can check your Python version with:
   ```sh
   python --version
   ```

3. (Optional) If you want to use Docker, ensure you have Docker installed. You can check your Docker version with:
   ```sh
   docker --version
   ```

## Usage

### Running the Interactive Script

You can run the interactive password generator script directly using Python:

```sh
python interactive_password_generator.py
```

You will be prompted to enter the total length of the password and the number of special characters. The script will then generate and display the password.

### Running the Script in Docker

To run the script in a Docker container, follow these steps:

1. Build the Docker image:
   ```sh
   docker build -t password-generator .
   ```

2. Run the Docker container:
   ```sh
   docker run -it --rm password-generator
   ```

The `-it` flag ensures that the container runs in interactive mode, allowing you to provide input and see output.

## Testing

This project includes unit tests to verify the functionality of the password generator. The tests are written using the `unittest` framework.

### Running Tests Locally

You can run the tests locally using Python:

```sh
python -m unittest discover
```

### Running Tests in Docker

To run the tests in a Docker container, modify the `CMD` instruction in the Dockerfile to run the tests instead of the interactive script:

```dockerfile
CMD ["python", "-m", "unittest", "discover"]
```

Then, build and run the Docker image:

```sh
docker build -t password-generator-test .
docker run --rm password-generator-test
```

## Project Structure

```
interactive_password_generator/
│
├── Dockerfile
├── generate_password.py
├── interactive_password_generator.py
├── test_generate_password.py
└── README.md
```

- `Dockerfile`: Docker configuration file to set up the environment and run the script/tests.
- `generate_password.py`: Python module containing the password generator function.
- `interactive_password_generator.py`: Interactive script for generating passwords.
- `test_generate_password.py`: Unit tests for the password generator function.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

This `README.md` provides an overview of the project, including features, installation instructions, usage, testing, project structure, and contribution guidelines. You can customize it further as needed.
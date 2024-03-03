# GitHub Repository Search Tool

This is a Python application with a Tkinter-based GUI that allows users to search GitHub repositories based on a query. The search results are displayed in the graphical interface, and users can export the results to a styled PDF with clickable links.

## Features

- **GitHub Repository Search:** Input a query to search for repositories on GitHub.
- **Graphical User Interface (GUI):** A user-friendly interface for interacting with the application.
- **Export to PDF:** Save the search results to a PDF document with clickable repository links.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Install required Python packages using `pip install -r requirements.txt`.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/gmpsankalpa/github-repo-search-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd github-repo-search-tool
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up your GitHub Personal Access Token:

    - Create a file named `.env` in the project directory.
    - Add your GitHub Personal Access Token to the `.env` file:

        ```env
        GITHUB_TOKEN=your-github-token
        ```

2. Run the application:

    ```bash
    python github_search_tool.py
    ```

3. In the GUI, enter a search query and click the "Search" button.

4. View the search results in the interface.

5. Optionally, click the "Export to PDF" button to save the results to a PDF file.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the GitHub API for providing the data used in this application.

---

<div align="center">

   ![repo size](https://img.shields.io/github/repo-size/gmpsankalpa/github-repo-search-tool?label=Repo%20Size&style=for-the-badge&labelColor=black&color=20bf6b)
   ![GitHub forks](https://img.shields.io/github/forks/gmpsankalpa/github-repo-search-tool?&labelColor=black&color=0fb9b1&style=for-the-badge)
   ![GitHub stars](https://img.shields.io/github/stars/gmpsankalpa/github-repo-search-tool?&labelColor=black&color=f7b731&style=for-the-badge)
   ![GitHub LastCommit](https://img.shields.io/github/last-commit/gmpsankalpa/github-repo-search-tool?logo=github&labelColor=black&color=d1d8e0&style=for-the-badge)

</div>

Happy coding!

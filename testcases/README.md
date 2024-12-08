# P2P Postman Collection Test Case Generator
This python project helps to generate parameteized test cases for the P2P Postman Collection. 
## Project Structure
The project directory is organized as follows:

```
/home/simon/uni/s5/vs/p2p-postman-collection/testcases
├── creators/
|   ├── system/
|       ├── CompStatusTestCreator.py
|       ├── DeleteCompTestCreator.py
|       ├── ...
|   ├── message/
|   ├──BaseTestCreator.py
├── out/
│   ├── test_cases
│       ├── testcase1.csv
│       ├── testcase1.csv
│       └── ...
├── star
|   ├── Component.py
├── ColumnName.py
├── TestGenerator.py
├── .gitignore
├── README.md
```

- **out/test_cases/**: Contains all the generated test case files in csv-format.
- **creators/**: Contains all the test case creators for the endpoints.
    - **BaseTestCreator.py**: Base class for all test case creators.
- **star/Component**: Contains data model for the component.
- **ColumnName.py**: Contains all possible column names for the test case files.

## How to run the project
### Prerequisites
- Python 3
### Run using IDE
1. Open the project in an IDE.
2. [OPTIONAL] If needed, add new test case creators in the `creators/` directory.
    1. Copy an existing test case creator and modify the following methods/variables:
        - `FILENAME`: Define the name of the test case file.
        - `HEADERS`: Define the headers for the test case file.
        - `create_test_case()`: Define the test case creation logic.
3. Open the `TestGenerator.py` file and edit the main method to your needs by adding/removing desired test case creators and defining the components.
4. Run the `TestGenerator.py` file.
5. The generated test case files will be saved in the `out/test_cases/` directory.
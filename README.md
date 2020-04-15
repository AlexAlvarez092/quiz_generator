# Quiz generator tool
---
Simple tool to generate quizzes.

**Input**
- Excel file with raw data (data.xls)

**Output**
- ./quiz.txt - Generated quiz
- ./key.txt - Answer keys

*Both files in the same folder as the script*

## Usage
1. Fill the excel file with the raw data and properties
  - In the first sheet, goes raw data **Without header** -- just raw data
  - In the second sheet, goes configuration properties -- label already is
  in first column and the property must gone in the second one

2. Install requirements

3. Execute quizGenerator.py script

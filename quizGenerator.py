#! python3
# quizGenerator.py - Create quizzes with questions and answers in random order

import random
import xlrd

# RAW data dictionary
d = {}

def readData():
    """ Rear from excel sheet RAW data and configuration options """
    # open the workbook
    wb = xlrd.open_workbook('data.xls')

    # dara is in the first sheet
    sh_data = wb.sheet_by_index(0)

    # config is in the second sheet
    sh_config = wb.sheet_by_index(1)
    global test_name
    test_name = sh_config.cell(0, 1). value
    global question_pattern
    question_pattern = sh_config.cell(1, 1).value
    global num_of_answers
    num_of_answers = sh_config.cell(2, 1).value

    # set the number of rows
    global rows
    rows = sh_data.nrows

    for i in range(sh_data.nrows):
        cell_value_class = sh_data.cell(i, 0).value
        cell_value_id = sh_data.cell(i, 1).value
        d[cell_value_class] = cell_value_id

def generateQuiz():
    """ Generate the quizzes """
    # Create the quiz and answer key files
    quizFile = open('quiz.txt', 'w')
    keyFile = open('key.txt', 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\n')
    # TODO: Set quiz name as parametre
    quizFile.write((' ' * 20) + test_name)
    quizFile.write('\n\n')

    # Shuffle the order of the answer options
    capitals = list(d.keys())
    random.shuffle(capitals)

    # Loop through all 50 capitals, maquing a question for each
    for questionNum in range(rows):
        # Get right and wrong answer
        correctAnswer = d[capitals[questionNum]]
        wrongAnswers = list(d.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # TODO: dinamically asign number of wrong answers
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file
        #quizFile.write('%s. ' + question_pattern +' %s\n' % (questionNum + 1, capitals[questionNum]))
        quizFile.write('%s. ' % (questionNum + 1) + question_pattern + ' %s\n' % (capitals[questionNum]))
        for i in range(int(num_of_answers)):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file
        keyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
        answerOptions.index(correctAnswer)]))
    quizFile.close()
    keyFile.close()


readData()
generateQuiz()

#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QButtonGroup, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle, randint

total = 0
score = 0

class Question():
    def __init__(
        self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 240)
main_win.setWindowTitle('Memory Card')

question_list = []
question_list.append(
    Question('Государственный язык Португалии', 'Португальский', 'Ангийский', 'Испанский','Французский')
)
question_list.append(
    Question('Столица Новой Зеландии.', 'Веллингтон', 'Хараре', 'Могадишо','Фамагуста')
)
question_list.append(
    Question('Столица Сьерра-Леоне', 'Фритаун', 'Минск', 'Конакри','Добрич')
)
question_list.append(
    Question('Столица Фиджи', 'Сува', 'Нукуалофа', 'Алжир','Альта-Грасия')
)
question_list.append(
    Question('Какого цвета нет на флаге России', 'Чёрный', 'Синий', 'Белый','Красный')
)
question_list.append(
    Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы','Алеуты')
)


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question_Lable.setText(q.question)
    correc_answer.setText(q.right_answer)
    show_question()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неверно')
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score, '\nРейтинг:', main_win.score/main_win.total*100)

def show_correct(result):
    right.setText(result)
    show_result()

def next_question():
    if len(question_list) != 0:
        cur_question = randint(0, len(question_list) - 1)
        ask(question_list[cur_question])
        question_list.pop(cur_question)
        main_win.total += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
    else:
        main_win.close()

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Следующий вопрос':
        next_question()

question_Lable = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
AnsGroupBox.hide()

right = QLabel('Правильно/Неправильно')
correc_answer = QLabel('Правильный ответ')

layout_ans_1 = QVBoxLayout()
layout_ans_1.addWidget(right)
layout_ans_1.addWidget(correc_answer, alignment = Qt.AlignCenter)

AnsGroupBox.setLayout(layout_ans_1)

main_layout = QVBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

main_layout.addWidget(question_Lable, alignment = Qt.AlignCenter)
main_layout.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
main_layout.addWidget(AnsGroupBox, alignment = Qt.AlignCenter)
main_layout.addWidget(btn_OK, alignment = Qt.AlignCenter)

main_win.setLayout(main_layout)

btn_OK.clicked.connect(click_OK)

main_win.setLayout(main_layout)

main_win.total = 0
main_win.score = 0

next_question()

main_win.show()
app.exec_()
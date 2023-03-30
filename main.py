import tkinter as tk
import random
import time

# Questions pour le test
questions = [
    {
        "question": "Quel est le prochain nombre dans cette séquence ? 2, 4, 6, 8, ...",
        "options": ["10", "11", "12", "14"],
        "answer": "10",
        "difficulty": 1
    },
    {
        "question": "Quel est le résultat de l'opération suivante : 12 x 4 ÷ 2 ?",
        "options": ["24", "32", "44", "48"],
        "answer": "24",
        "difficulty": 1
    },
    {
        "question": "Complétez la série suivante : J, F, M, A, M, __",
        "options": ["J", "J", "J", "J"],
        "answer": "J",
        "difficulty": 1
    },
    {
        "question": "Quel est le contraire de 'prudent' ?",
        "options": ["téméraire", "généreux", "intelligent", "heureux"],
        "answer": "téméraire",
        "difficulty": 2
    },
    {
        "question": "Dans quelle direction pointe l'aiguille des minutes d'une horloge à 2h30 ?",
        "options": ["vers le haut", "vers le bas", "vers la gauche", "vers la droite"],
        "answer": "vers la droite",
        "difficulty": 2
    },

    {
        "question": "Quel est le carré de 12 ?",
        "options": ["144", "120", "132", "156"],
        "answer": "144",
        "difficulty": 3
    },
    {
        "question": "Dans une série de nombres, le deuxième est le double du premier, le troisième est le triple du deuxième, le quatrième est le quadruple du troisième, etc. Quel est le sixième nombre de cette série si le premier est 2 ?",
        "options": ["64", "48", "96", "72"],
        "answer": "64",
        "difficulty": 4
    },
    {
        "question": "Quel est le plus grand océan de la Terre ?",
        "options": ["L'océan Atlantique", "L'océan Indien", "L'océan Pacifique", "L'océan Arctique"],
        "answer": "L'océan Pacifique",
        "difficulty": 2
    },
    {
        "question": "Quel est le nom de l'équation suivante : E=mc² ?",
        "options": ["Loi de la gravitation universelle", "Théorème de Pythagore", "Principe de relativité restreinte", "Formule de l'énergie cinétique"],
        "answer": "Principe de relativité restreinte",
        "difficulty": 5
    },
    {
        "question": "Quel est le nom du plus grand désert chaud du monde ?",
        "options": ["Le désert de Gobi", "Le désert de l'Atacama", "Le Sahara", "Le désert d'Arabie"],
        "answer": "Le Sahara",
        "difficulty": 2
    },
    {
        "question": "Dans quelle ville se trouve la tour Eiffel ?",
        "options": ["Paris", "Londres", "Berlin", "New York"],
        "answer": "Paris",
        "difficulty": 1
    },
    {
        "question": "Quel est l'élément chimique dont le symbole est Ag ?",
        "options": ["Argon", "Argent", "Or", "Platine"],
        "answer": "Argent",
        "difficulty": 3
    },
    {
        "question": "Qui a écrit la pièce de théâtre 'Roméo et Juliette' ?",
        "options": ["Victor Hugo", "Molière", "William Shakespeare", "Albert Camus"],
        "answer": "William Shakespeare",
        "difficulty": 2
    },
    {
        "question": "Quel est le nom de l'acteur principal de la trilogie 'Le Seigneur des Anneaux' ?",
        "options": ["Tom Hanks", "Johnny Depp", "Orlando Bloom", "Elijah Wood"],
        "answer": "Elijah Wood",
        "difficulty": 1
    },
    {
        "question": "Quel est le nombre manquant dans la séquence suivante : 1, 4, 9, 16, 25, __",
        "options": ["30", "36", "40", "49"],
        "answer": "36",
        "difficulty": 2
    },
    {
        "question": "Dans quelle ville est né Mozart ?",
        "options": ["Linz", "Salzbourg", "Vienne", "Graz"],
        "answer": "Salzbourg",
        "difficulty": 3
    },
    {
        "question": "Quel est le nom du héros dans le roman 'Les Misérables' de Victor Hugo ?",
"options": ["Valjean", "Cosette", "Fantine", "Javert"],
"answer": "Valjean",
"difficulty": 3
},
{
"question": "Dans quelle année est mort Léonard de Vinci ?",
"options": ["1506", "1519", "1532", "1564"],
"answer": "1519",
"difficulty": 3
},
# Ajoutez d'autres questions ici
]

class IQTestLogic:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.correct_answers = 0
        self.total_score = 0
        self.start_time = time.time()

    def get_current_question(self):
        return self.questions[self.current_question]

    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question]["answer"]
        is_correct = selected_answer == correct_answer

        if is_correct:
            self.correct_answers += 1
            self.total_score += self.questions[self.current_question]["difficulty"]

        self.current_question += 1
        return is_correct

    def has_more_questions(self):
        return self.current_question < len(self.questions)

    def get_results(self):
        score = round(self.total_score / len(self.questions))
        duration = round(time.time() - self.start_time)
        minutes = duration // 60
        seconds = duration % 60
        return score, duration, minutes, seconds

class TestLogic:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.correct_answers = 0
        self.total_score = 0
        self.start_time = time.time()

    def next_question(self):
        self.current_question += 1

    def check_answer(self, index, options):
        if options[index] == self.questions[self.current_question]["answer"]:
            self.correct_answers += 1
            self.total_score += self.questions[self.current_question]["difficulty"]
            return True
        else:
            return False

    def get_results(self):
        score = round(self.total_score / len(self.questions))
        duration = round(time.time() - self.start_time)
        minutes = duration // 60
        seconds = duration % 60
        return score, duration, minutes, seconds

    def restart(self):
        self.current_question = 0
        self.correct_answers = 0
        self.total_score = 0
        self.start_time = time.time()


class IQTest:
    def __init__(self, master, questions):
        self.master = master
        self.logic = TestLogic(questions)
        master.title("Test de QI")

        self.question_label = tk.Label(master, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", font=("Arial", 12), command=lambda x=i: self.check_answer(x))
            button.pack(fill=tk.X, padx=50, pady=10)
            self.answer_buttons.append(button)

        self.next_button = tk.Button(master, text="Suivant", font=("Arial", 12), command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

        self.difficulty_label = tk.Label(master, text="")
        self.difficulty_label.pack(side="left", padx=10)

        self.score_label = tk.Label(master, text="")
        self.score_label.pack(side="right", padx=10)

        self.show_question()

    def next_question(self):
        self.logic.next_question()
        if self.logic.current_question == len(self.logic.questions):
            self.show_results()
        else:
            self.show_question()

            for button in self.answer_buttons:
                button.config(bg="SystemButtonFace", state="normal")
            self.next_button.config(state="disabled")

    def show_question(self):
        current_question = self.logic.questions[self.logic.current_question]
        self.question_label.config(text=current_question["question"])
        options = current_question["options"][:]
        random.shuffle(options)
        for i in range(4):
            self.answer_buttons[i].config(text=options[i], state="normal", bg="SystemButtonFace")

        self.difficulty_label.config(text=f"Difficulté : {current_question['difficulty']}")
        self.score_label.config(text=f"Score : {self.logic.correct_answers}/{self.logic.current_question}")

    def check_answer(self, index):
        correct = self.logic.check_answer(index, [btn["text"] for btn in self.answer_buttons])
        if correct:
            self.answer_buttons[index].config(bg="green")
        else:
            self.answer_buttons[index].config(bg="red")

        for button in self.answer_buttons:
            button.config(state="disabled")
        self.next_button.config(state="normal")

    def show_results(self):
        score, duration, minutes, seconds = self.logic.get_results()
        correct_answers = self.logic.correct_answers
        total_questions = len(self.logic.questions)
        result_text = f"Vous avez obtenu {correct_answers} bonnes réponses sur {total_questions} en {minutes:02d}:{seconds:02d}. "
        if score == total_questions:
            result_text += "Félicitations, vous êtes très intelligent !"
        elif score >= total_questions * 0.75:
            result_text += "Vous avez une intelligence supérieure à la moyenne."
        elif score >= total_questions * 0.5:
            result_text += "Vous avez une intelligence dans la moyenne."
        else:
            result_text += "Vous pouvez améliorer votre score en pratiquant davantage."
        self.question_label.config(text=result_text)

        self.difficulty_label.pack_forget()
        self.score_label.pack_forget()
        for button in self.answer_buttons:
            button.pack_forget()
        self.next_button.pack_forget()

        restart_button = tk.Button(self.master, text="Recommencer", font=("Arial", 12), command=self.restart)
        restart_button.pack(pady=20)

    def restart(self):
        self.logic.restart()
        self.show_question()
        self.difficulty_label.pack(side="left", padx=10)
        self.score_label.pack(side="right", padx=10)
        self.next_button.config(state="disabled")
        self.master.geometry("800x500")

root = tk.Tk()
app = IQTest(root, questions)
root.mainloop()

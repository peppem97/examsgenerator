import json

class ExamsCorrector():
    def __init__(self) -> None:
        self.results = []
        self.questions_number = 0

    def correct(self, exam_number):
        with open(f"exam_{exam_number}_solutions.data") as f:
            solutions = json.load(f)
        for question_number in solutions.keys():
            signed = int(input(f"Risposta della domanda {question_number}: "))
            result = (signed == solutions[question_number])
            self.results.append(result)
            print("\033[92mCorretta!\033[0m\n" if result else "\033[91mErrata!\033[0m\n")
            self.questions_number = self.questions_number + 1

    def compute_result(self):
        corrects_number = len(list(filter(lambda x: x, self.results)))
        print(f"Risposte corrette: {corrects_number} su {self.questions_number}")
        print(f"Risultato: {round((corrects_number/self.questions_number) * 10, 2)}")

    def start(self):
        exam_number = int(input("Numero esame: "))
        self.correct(exam_number)
        self.compute_result()


        



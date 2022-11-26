from examsgenerator import ExamsGenerator

config = {
    "source_file": "Domande",
    "source_extension": "xlsx",
    "destination_file": "exam",
    "deep_filtering": True,
    "subject": "TPSIT",
    "classroom": "4H",
    "era": 1,
    "sector": "PRATICA",
    "title": "Compito Pratico di T.P.S.I.T. - A.S. 2022/2023 - Classe 4H",
    "heading": "Cognome e Nome: ___________________________________________",
    "questions_number": 20,
    "options_supported": 4,
    "shuffle_questions": True,
    "shuffle_options": True,
    "export_solutions": True,
    "exams_number": 5,
    "only_count": False,
    "subject_denomination": "MATERIA",
    "classroom_denomination": "CLASSE",
    "era_denomination": "ERA",
    "sector_denomination": "SETTORE",
    "type_denomination": "TIPO",
    "question_denomination": "DOMANDA",
    "solution_denomination": "CORRETTA",
    "option_denomination": "OPZIONE"
}

if __name__ == "__main__":
    exams_generator = ExamsGenerator(config)
    exams_generator.start()



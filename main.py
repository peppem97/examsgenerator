from examsgenerator import ExamsGenerator

config = {
    "source_file": "Domande",
    "source_extension": "xlsx",
    "destination_file": "exam",
    "deep_filtering": True,
    "subject": "SISTEMI E RETI",
    "classroom": "4F",
    "era": 2,
    "sector": "PRATICA",
    "title": "Compito Pratico di Sistemi e Reti - A.S. 2022/2023 - Classe 4F",
    "heading": "Cognome e Nome: ___________________________________________",
    "questions_number": 40,
    "options_supported": 4,
    "shuffle_questions": True,
    "shuffle_options": True,
    "exams_number": 5,
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



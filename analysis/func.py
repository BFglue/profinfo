# -*- coding: utf-8 -*-
import os

from django.db import connection
from django.conf import settings
from analysis.analyser import Analyser
from hackathon.models import Profession, Vacancy


def create_profession_training_data():
    """ 
        Creates training data set
    """
    professions = Profession.objects.all()
    for profession in professions:
        vacancies = Vacancy.objects.filter(job_name=profession.name)[:30]
        if vacancies.count() > 0:
            directory = os.path.join(settings.DATA_FOLDER, str(profession.id))
            try:
                os.makedirs(directory)
            except:
                pass
            # vacancies = Vacancy.objects.filter(initial_profession_id=profession.id)[:30]
            c = 0
            for vac in vacancies:
                path = os.path.join(directory, str(profession.id) + "_" + str(c) + ".txt")
                f = open(path, "w")
                file_str = vac.job_name.encode("utf-8") + " ".encode("utf-8") + vac.duty.encode("utf-8")
                f.write(file_str)
                f.close()
                c += 1


def predict_professions(dataset):
    """ 
        Predicts professions for given dataset
        and fills rows with predicted data
    """
    a = Analyser()
    a.train(settings.DATA_FOLDER)
    
    for row in dataset:
        profession_id = a.predict(row.job_name + ' ' + row.duty)
        row.predicted_profession_id = profession_id
        row.save()


def predict_profession_by_vacancy_text(duty):
    """ 
        Predicts one profession by its text
    """
    a = Analyser()
    a.train(settings.DATA_FOLDER)
    profession_id = a.predict(duty)
    try:
        profession = Profession.objects.get(pk=profession_id)
        print profession.name
    except:
        print "Не удалось определить профессию"
        pass


def fill_foreign_keys():
    query = """
        INSERT INTO analysis_profinfoglobal
        SELECT 
            NULL id,
            CURDATE() `date`,
            predicted_profession_id profession_id,
            count(id) actuality,
            avg(salary_max) avg_salary,
            education min_education
        FROM 
            hackathon_vacancy
        GROUP BY
            predicted_profession_id
    """

    with connection.cursor() as cursor:
        cursor.execute(query)


# @todo Перенести функции в соответствующие им модули
# @todo Написать management commands

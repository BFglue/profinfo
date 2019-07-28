# -*- coding: utf-8 -*-

import json
import requests

from hackathon.models import *

def trudvsem_adapter(profession_name, profession, save_to_db=False, limit=0):
    def get_data_with_offset(profession_name, offset):
        url = "http://opendata.trudvsem.ru/api/v1/vacancies?text=%s&offset=%s" % (profession_name, offset)
        r = requests.get(url)
        if r.status_code == 200:
            resul_json = json.loads(r.text)
            return resul_json
        else:
            return None
    vacancies = []
    max_offset = 0
    vacancies_count = 0
    print profession_name
    first_result = get_data_with_offset(profession_name, 0)
    if first_result:
        vacancies_count = first_result['meta']['total']
        # vacancies += first_result['results']['vacancies']
        try:
            if limit != 0 and limit < vacancies_count:
                vacancies_count = limit
                vacancies += first_result['results']['vacancies'][:limit]
            else:
                vacancies += first_result['results']['vacancies']
        except:
            pass
        max_offset = vacancies_count // 100
    if max_offset > 0:
        for offset in range(1, max_offset + 1):
            print "page %s from %s" % (offset, max_offset)
            vac = get_data_with_offset(profession_name, offset)
            if vac:
                vacancies += vac['results']['vacancies']

    if save_to_db:
        for vacancy in vacancies:
            args = {}
            try:
                if profession_name.lower() not in vacancy['vacancy'].get('job-name').lower():
                    continue
                if vacancy['vacancy']['category']:
                    args['category'] = vacancy['vacancy']['category'].get('specialisation')
                if vacancy['vacancy']['region']:
                    args['region_code'] = vacancy['vacancy']['region'].get('region_code')
                if vacancy['vacancy']['region']:
                    args['region_name'] = vacancy['vacancy']['region'].get('name')
                args['salary_min'] = vacancy['vacancy'].get('salary_min')
                args['salary_max'] = vacancy['vacancy'].get('salary_max')
                args['job_name'] = vacancy['vacancy'].get('job-name')
                args['duty'] = vacancy['vacancy'].get('duty')
                if vacancy['vacancy']['requirement']:
                    args['education'] = vacancy['vacancy']['requirement'].get('education')
                args['initial_profession_id'] = profession.id
                # print args['region_name']
                obj, created = Vacancy.objects.get_or_create(**args)
            except:
                pass

    else:
        return vacancies





    
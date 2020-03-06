import requests
import json
import time
from banco_dados import create_table, data_entry, query

status_check = True
not_sucess_sao_paulo = True
not_sucess_santos = True
not_sucess_salvador = True
not_sucess_rio = True
not_sucess_sao_carlos = True
not_sucess_maceio = True

create_table()

while status_check:
    if not_sucess_sao_paulo:
        requisition = requests.get('http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token=b22460a8b91ac5f1d48f5b7029891b53')
        if requisition.status_code != 200:
            print('ocorreu um erro')
            time.sleep(60)
        else:
            status_check = False
            not_sucess_sao_paulo = False
            sao_paulo = json.loads(requisition.text)
            data_entry(sao_paulo)

    if not_sucess_santos:
        requisition = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3675/current?token=b22460a8b91ac5f1d48f5b7029891b53')
        if requisition.status_code != 200:
            print('ocorreu um erro')
            time.sleep(60)
        else:
            status_check = False
            not_sucess_santos = False
            santos = json.loads(requisition.text)
            data_entry(santos)

    if not_sucess_salvador:
        requisition = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/7564/current?token=b22460a8b91ac5f1d48f5b7029891b53')
        if requisition.status_code != 200:
            print('ocorreu um erro')
            time.sleep(60)
        else:
            status_check = False
            not_sucess_salvador = False
            salvador = json.loads(requisition.text)
            data_entry(salvador)

    if not_sucess_rio:
        requisition = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/5959/current?token=b22460a8b91ac5f1d48f5b7029891b53')
        if requisition.status_code != 200:
            print('ocorreu um erro')
            time.sleep(60)
        else:
            status_check = False
            not_sucess_rio = False
            rio = json.loads(requisition.text)
            data_entry(rio)

    if not_sucess_sao_carlos:
        requisition = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3680/current?token=b22460a8b91ac5f1d48f5b7029891b53')
        if requisition.status_code != 200:
            print('ocorreu um erro')
            time.sleep(60)
        else:
            status_check = False
            not_sucess_sao_carlos = False
            sao_carlos = json.loads(requisition.text)
            data_entry(sao_carlos)

    if not_sucess_maceio:
        requisition = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/6809/current?token=b22460a8b91ac5f1d48f5b7029891b53')
        if requisition.status_code != 200:
            print('ocorreu um erro')
            time.sleep(60)
        else:
            status_check = False
            not_sucess_maceio = False
            maceio = json.loads(requisition.text)
            data_entry(maceio)

query()

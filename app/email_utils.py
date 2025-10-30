import requests
from datetime import datetime
from flask import current_app

def send_simple_message(to, subject, newUser):
    app = current_app
    print('Enviando mensagem (POST)...', flush=True)
    print('URL: ' + str(app.config['API_URL']), flush=True)
    print('api: ' + str(app.config['API_KEY']), flush=True)
    print('from: ' + str(app.config['API_FROM']), flush=True)
    print('to: ' + str(to), flush=True)
    print('subject: ' + str(app.config['FLASKY_MAIL_SUBJECT_PREFIX']) + ' ' + subject, flush=True)
    print('text: ' + "Prontuário: PT3032515\n" + "Nome: Soraya Gomes da Silva\n" + "Novo usuário cadastrado: " + newUser, flush=True)

    resposta = requests.post(app.config['API_URL'],
                             auth=("api", app.config['API_KEY']),
                             data={"from": app.config['API_FROM'],
                                   "to": to,
                                   "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                                   "text": "Prontuário: PT3032515\n"
                                           "Nome: Soraya Gomes da Silva\n"
                                           "Novo usuário cadastrado: " + newUser})

    print('Enviando mensagem (Resposta)...' + str(resposta) + ' - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), flush=True)
    return resposta

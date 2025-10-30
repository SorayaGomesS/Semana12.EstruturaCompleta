import requests
from datetime import datetime
from flask import current_app

def send_simple_message(to, subject, new_user):
    app = current_app
    print('Enviando mensagem (POST)...', flush=True)
    print('URL: ' + str(app.config['API_URL']), flush=True)
    print('api: ' + str(app.config['API_KEY']), flush=True)
    print('from: ' + str(app.config['API_FROM']), flush=True)

    text = (
        f"Prontuário: PT3032515\n"
        f"Nome: Soraya Gomes da Silva\n"
        f"Novo usuário cadastrado: {new_user}"
    )

    response = requests.post(
        app.config['API_URL'],
        auth=("api", app.config['API_KEY']),
        data={
            "from": app.config['API_FROM'],
            "to": to,
            "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
            "text": text
        }
    )

    print('Resposta:', response, '-', datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), flush=True)
    return response

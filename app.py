from flask import Flask, render_template, request, flash
from datetime import datetime
from models import Pessoa, db_session
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lanalindaperfeitamaravilhosa'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        suggestion = request.form.get('suggestion')

        suggestion_list.append(suggestion)

    return render_template('index.html')

@app.route('/atividades/criar', methods=['GET', 'POST'])
def criar_atividade():
    if request.method == 'POST':
        name_activity = request.form.get('form_name_activity')
        description_activity = request.form.get('form_description_activity')
        priority_activity = request.form.get('form_priority_activity')
        resources_activity = request.form.getlist('form_resources_activity')
        resources_activity = ", ".join(resources_activity)
        date_activity = request.form.get('form_date_activity')
        date_activity = datetime.strptime(date_activity, '%Y-%m-%d').date()

        activity_data = {
            'name_activity': name_activity,
            'description_activity': description_activity,
            'priority_activity': priority_activity,
            'resources_activity': resources_activity,
            'date_activity': date_activity
        }

        activity_list.append(activity_data)

    return render_template('criar_atividade.html')

@app.route('/atividades/listar')
def listar_atividades():
    activities = activity_list

    return render_template('listar_atividades.html', activities=activities)

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

@app.route('/pessoa/criar', methods=['GET', 'POST'])
def criar_pessoa():
    if request.method == 'POST':
        nome_form = request.form.get('form_nome')
        email_form = request.form.get('form_email')
        senha_form = request.form.get('form_senha')
        if not nome_form:
            flash('Preencha o nome', 'error')
            return render_template('criar_pessoa.html')
        try:
            nova_pessoa = Pessoa(nome_pessoa=nome_form, email=email_form, senha_hash=senha_form)
            db_session.add(nova_pessoa)
            db_session.commit()
            return render_template('pessoa.html')
        except SQLAlchemyError:
            db_session.rollback()
            flash('Erro ao salvar pessoa no bando de dados', 'error')
            return render_template('criar_pessoa.html')
        except:
            db_session.rollback()
            flash('Erro inesperado', 'error')
            return render_template('criar_pessoa.html')
    return render_template('criar_pessoa.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
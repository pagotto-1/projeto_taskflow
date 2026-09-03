from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

activity_list = []
suggestion_list = []

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
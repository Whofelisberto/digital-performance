from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user_model import authenticate
from models.metric_model import get_metrics

web_bp = Blueprint('web', __name__)

@web_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@web_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = authenticate(email, password)
    if not user:
        flash('Credenciais inválidas', 'error')
        return redirect(url_for('web.home'))

    # Salva usuário na sessão
    session['user'] = user
    return redirect(url_for('web.dados'))

@web_bp.route('/dados')
def dados():
    user = session.get('user')
    if not user:
        return redirect(url_for('web.home'))

    # Pegando parâmetros da URL para paginação e ordenação

    sort_by = request.args.get('sort_by', 'date')
    order = request.args.get('order', 'asc')
    page = int(request.args.get('page', 1))
    per_page = 25
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    role = user.get('role', 'user')

    # Buscar métricas (ajuste conforme sua função)

    df = get_metrics(date_from, date_to, sort_by, order, role)
    total = len(df)
    metrics = df.iloc[(page-1)*per_page : page*per_page].to_dict(orient="records")

    return render_template(
        'dados.html',
        user=user,
        metrics=metrics,
        role=role,
        order=order,
        sort_by=sort_by,
        page=page,
        per_page=per_page,
        total=total,
        request=request
    )

@web_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('web.home'))

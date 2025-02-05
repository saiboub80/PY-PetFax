from flask import Blueprint, render_template, request, redirect
from petfax import models

fact = Blueprint('fact', __name__)


@fact.route('/new')
def new():
    return render_template('facts/new.html')


@fact.route('/facts', methods=['GET', 'POST'])
def facts():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact_content = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact_content)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')

    results = models.Fact.query.all()
    for result in results:
        pass  # You can remove this line once you add operations

    return render_template('facts/facts.html', facts=results, title='Facts')


# @app.route('/about')
# def about():
#     return render_template('about.html')

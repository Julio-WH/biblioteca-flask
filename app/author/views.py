from flask import render_template, url_for, flash, redirect
from . import author
from ..models import db
from ..forms import AuthorForm
from ..models import Authors


@author.route('/list')
def list_authors():
    authors = Authors.query.all()
    context = {
        'authors': authors
    }
    return render_template('author/list.html', **context)


@author.route('/add', methods=['GET', 'POST'])
def add_author():
    form = AuthorForm()
    context = {
        'title': "Agregar",
        'form': form
    }
    if form.validate_on_submit():
        author = Authors(
            name=form.name.data,
            lastname=form.lastname.data,
            email=form.email.data
        )
        db.session.add(author)
        db.session.commit()
        flash('Author registrado con éxito!', 'success')
        return redirect(url_for('author.list_authors'))
    return render_template('author/form.html', **context)


@author.route('/edit/<int:author_id>', methods=['GET', 'POST'])
def edit_author(author_id):
    author = Authors.query.get_or_404(author_id)
    form = AuthorForm(obj=author)
    context = {
        'title': "Editar",
        'form': form,
        'author': author
    }
    if form.validate_on_submit():
        author = Authors(
            name=form.name.data,
            lastname=form.lastname.data,
            email=form.email.data
        )
        db.session.add(author)
        db.session.commit()
        flash('Author editado con éxito!', 'success')
        return redirect(url_for('author.list_authors'))
    return render_template('author/form.html', **context)


@author.route('/delete/<int:author_id>', methods=['GET', 'POST'])
def delete_author(author_id):
    author = Authors.query.get_or_404(author_id)
    form = AuthorForm(obj=author)
    context = {
        'title': 'Eliminar',
        'form': form,
        'author': author
    }
    if form.validate_on_submit():
        db.session.delete(author)
        db.session.commit()
        flash('Author Eliminado con éxito!', 'success')
        return redirect(url_for('author.list_authors'))
    return render_template('author/delete.html', **context)

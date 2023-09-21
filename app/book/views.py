from flask import render_template, url_for, flash, session, redirect
from . import book
from ..models import Authors
from ..forms import BookForm
from ..models import Books


@book.route('/list')
def list_books():
    books = Books.query.all()
    context = {
        'books': books
    }
    return render_template('book/list.html', **context)


@book.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    authors = Authors.query.all()
    if not authors:
        flash('Necesitas un autor minimo...', 'warning')
        return redirect(url_for('author.add_author'))
    context = {
        'title': "Agregar",
        'form': form
    }
    if form.validate_on_submit():
        book = Books(
            title=form.title.data,
            author=form.lastname.data,
            pub_date=form.pub_date.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Libro registrado con éxito!', 'success')
        return redirect(url_for('book.list_books'))
    return render_template('book/form.html', **context)

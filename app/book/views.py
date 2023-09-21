from flask import render_template, url_for, flash, session, redirect
from . import book
from ..models import db
from ..models import Authors
from ..models import Books
from ..forms import BookForm


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
    form.authors.choices = [(author.id, f'{author.name} {author.lastname}') for author in authors]
    if not authors:
        flash('Necesitas un autor minimo, agrega uno...', 'warning')
        return redirect(url_for('author.add_author'))
    context = {
        'title': "Agregar",
        'form': form
    }
    if form.validate_on_submit():
        book = Books(
            title=form.title.data,
            autor_id=form.authors.data,
            pub_date=form.pub_date.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Libro registrado con éxito!', 'success')
        return redirect(url_for('book.list_books'))
    return render_template('book/form.html', **context)


@book.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Books.query.get_or_404(book_id)
    form = BookForm(obj=book)
    authors = Authors.query.all()
    form.authors.choices = [(author.id, f'{author.name} {author.lastname}') for author in authors]
    context = {
        'title': "Editar",
        'form': form,
        'book': book
    }
    if form.validate_on_submit():
        book.title = form.title.data,
        book.autor_id = form.authors.data,
        book.pub_date = form.pub_date.data
        db.session.commit()
        flash('Libro editado con éxito!', 'success')
        return redirect(url_for('book.list_books'))
    return render_template('book/form.html', **context)


@book.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    book = Books.query.get_or_404(book_id)
    form = BookForm(obj=book)
    authors = Authors.query.all()
    form.authors.choices = [(author.id, f'{author.name} {author.lastname}') for author in authors]
    context = {
        'title': 'Eliminar',
        'form': form,
        'book': book
    }
    if form.validate_on_submit():
        db.session.delete(book)
        db.session.commit()
        flash('Libro Eliminado con éxito!', 'success')
        return redirect(url_for('book.list_books'))
    return render_template('book/form.html', **context)


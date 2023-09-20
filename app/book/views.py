from flask import render_template, url_for, flash, session, redirect
from . import book
from ..models import Books


@book.route('/list')
def list_books():
    books = Books.query.all()
    context = {
        'books': books
    }
    return render_template('book/list.html', **context)

from flask import render_template, flash, redirect, url_for, request, current_app
from app.main import bp

@bp.route('/')


@bp.route('/main')
def main():
    return render_template('main.html', title='WorkoutPedia')

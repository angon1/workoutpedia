from flask import current_app
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    jsonify,
)
from app.exercises.models import Exercise, Tag
from werkzeug.urls import url_parse
from app.exercises.forms import ExerciseForm


# def exerciseShowNameSerializedImpl(name):
#     exercise = Exercise.query.filter_by(name=name).one()
#     exerciseJson = exercise.asDict()
#     return jsonify(exerciseJson)

# def exerciseAddToBase(form):
#     print("trolololo \n {} \n".format(request))
#     exercise = Exercise(
#         name=form.name.data,
#         description=form.description.data,
#         movieLink=form.movieLink.data,
#     )
#     db.session.add(exercise)
#     db.session.commit()
#     flash("Exercise added to db")


# def exerciseNewImpl():

#     form = ExerciseForm()
#     if form.validate_on_submit():
#         exerciseAddToBase(form)
#         print("tralalalalala \n {} \n".format(request))
#         return redirect(url_for("main.main"))
#     flash("Somehow Exercise can't be added")
#     return render_template("edit.html", title="WorkoutPedia", form=form)


# def exerciseEditOnSubmit(id, form):
#     exercise = Exercise.query.get(id)
#     exercise.name = form.name.data
#     exercise.description = form.description.data
#     exercise.movieLink = form.movieLink.data
#     db.session.commit()
#     exercise = Exercise.query.get(id)
#     flash("Exercise changes saved")
#     return render_template("show.html", title="WorkoutPedia", exercise=exercise)


# def exerciseEditOnGet(id, form):
#     exercise = Exercise.query.get(id)
#     form.name.data = exercise.name
#     form.description.data = exercise.description
#     form.movieLink.data = exercise.movieLink
#     return render_template("edit.html", title="WorkoutPedia", id=id, form=form)


# def exerciseEditImpl(id):
#     form = ExerciseForm()
#     if form.validate_on_submit():
#         return exerciseEditOnSubmit(id, form)
#     elif request.method == "GET":
#         return exerciseEditOnGet(id, form)


# def exerciseGetAllFromBase():
#     return Exercise.query.all()


# def exerciseListImpl():
#     exerciseList = exerciseGetAllFromBase()
#     return render_template(
#         "index.html", title="WorkoutPedia", exerciseList=exerciseList
#     )


# def exerciseGetFromBase(name):
#     return Exercise.query.filter_by(name=name).first()


# def exerciseShowNameImpl(name):
#     exercise = exerciseGetFromBase(name)
#     return render_template("show.html", title="WorkoutPedia", exercise=exercise)


# def exerciseDeleteFromBase(id):
#     exercise = Exercise.query.get(id)
#     db.session.delete(exercise)
#     db.session.commit()
#     flash("Exercise {} succesfully removed from db".format(exercise.name))


# # Serializers
# # exercises:
# def exerciseListSerializedImpl():
#     exerciseList = Exercise.query.all()
#     serializedExerciseList = []
#     for i in exerciseList:
#         serializedExerciseList.append(i.to_dict(only=("id", "name")))
#     return jsonify(serializedExerciseList)


# def exerciseListSerializedFullImpl():
#     exerciseList = Exercise.query.all()
#     serializedExerciseList = []
#     for exercise in exerciseList:
#         serializedExerciseList.append(exercise.asDict())
#     return jsonify(serializedExerciseList)


# def exerciseIdSerializeImpl(id):
#     exercise = Exercise.query.get(id)
#     exerciseJson = exercise.asDict()
#     return jsonify(exerciseJson)


# def exerciseIdGetTagsImpl(id):
#     exercise = Exercise.query.get(id)
#     return jsonify(exercise.tagsDict())


# # # tag-exercise
# # def addTagsListToExercise(id, tagsList):
# #     return Exercise.query.get(id).addTagsList(tagsList)

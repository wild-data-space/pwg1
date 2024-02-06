#Importer les packages de creation de la webapp et de la gestion des routes et des transfert de donnees
from flask import Flask, render_template, request, flash
#Import Le package de gestion de base de donnees
from flask_sqlalchemy import SQLAlchemy
#Importer le package de la cretion de date de creation de chaque element par defaut
from datetime import datetime
#Importer le package d'encrypt des mot de passe
from flask_bcrypt import Bcrypt
#Creation de la web app
app = Flask(__name__)
#Configuration du lien de la base de donnee et du cle de securite qui est essentiel dans le transfert de donnees
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = 'GHTLPWEPedkeoprpw1232018@@()#4'
#Creation d'un moteur de gestion de BD
db = SQLAlchemy(app)
#Creation d'un moteur de gestion d'encrypt
bcrypt = Bcrypt(app)

#Creation de classe d'utilisateur Model de table de donnee qui va etre appelee user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Identification de colonne de cle primaire automatique
    email = db.Column(db.String(20), unique=True, nullable=False) #identification de colonne d'email non null et unique a taille 20 caractere
    password = db.Column(db.String(60), nullable=False) #identification de colonne de mot de passe non null de taille 60
    todos = db.relationship('Todo', backref='user_id', lazy=True) #identification de la relation avec la table todo a travers la colonne user_id

#Creation de la table Todo
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created = db.Column(db.DateTime, default = datetime.utcnow)
    due_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #champs cle etranger qui servie comme cle de relation entre user et tot

#Creation de route avec deux methode d'access lecture et ecriture
@app.route('/register', methods = ["GET",'POST'])
@app.route('/', methods = ["GET",'POST'])
def register():
    if request.method == 'POST': #pour verifier est ce que l'utilisateur a soumettre la formulaire
        #Extraction des donnees de la formulaire
        email_form = request.form['email']
        password1 = request.form['password']
        password2 = request.form['confirm_password']
        if password2 != password1:
            flash('Resaisi le mot de passe', 'danger')
        else:
            #Verification de l'existance d'un user avec l'email saisie
            user_exist = User.query.filter_by(email = email_form).first()
            if user_exist:
                #Renvoie de message d'erreur
                flash('Email deja utilise', 'danger')
            else:
                #Creation d'utilisateur
                user = User(email = email_form, password = bcrypt.generate_password_hash(password1))
                #Ajout de l'utilisateur dans la table de donnee
                db.session.add(user)
                #Confirmation de l'ajout
                db.session.commit()
    return render_template('register.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

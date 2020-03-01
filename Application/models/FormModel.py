from Application import db

class FormModel(db.Model):
	
	__tablename__='Example'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False, unique=True)
	
	def __repr__(self):
		return '<Example {}>'.format(self.name)

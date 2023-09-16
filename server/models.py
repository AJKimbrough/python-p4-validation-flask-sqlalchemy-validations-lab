from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_author_name(self, key, author):
        if author == '':
            raise ValueError("Author must have a name.")
        return author
        
       
        
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) != 10:
            raise ValueError("Invalid number")
        return number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validates_content(self, key, content):
        if len(content) <= 250:
            raise ValueError("Not correct size")
        return content
    
    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Too long")
        return summary
    
    @validates('title')
    def validates_title(self, key, title):
        if title not in ["Won't Believe', 'Secret', 'Top', 'Guess'"]:
            raise ValueError("Title is invalid")
        return title
    
    @validates('category')
    def validates_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Invalid category")
        return category


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

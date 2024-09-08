from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    serialize_rules = ('-reviews.customer',)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'

    reviews = db.relationship('Review' , back_populates='customer') 
     
    items = association_proxy('reviews', 'item')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'items': [item.to_dict() for item in self.items] if self.items else []  
        }


class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    serialize_rules = ('-reviews.item',)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'
    reviews = db.relationship('Review' , back_populates='item')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'reviews': [review.to_dict() for review in self.reviews] if self.reviews else []
            #'items': [item.to_dict() for item in self.items] 
        }
class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer , primary_key=True)
    comment = db.Column(db.String)
    customer_id = db.Column(db.Integer , db.ForeignKey('customers.id'), nullable=False)
    item_id = db.Column(db.Integer , db.ForeignKey('items.id'), nullable=False)

    serialize_rules = ('-customer.reviews', '-item.reviews')
   
    customer =db.relationship ('Customer' , back_populates='reviews')
    item=db.relationship('Item' , back_populates='reviews')
    
    def to_dict(self):
        
        return {
            'id': self.id,
            'comment': self.comment,
            'customer': self.customer.to_dict() if self.customer else None,
            'item': self.item.to_dict() if self.item else None
        }

from app import db

class master_items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique=True, nullable=True)
    status = db.Column(db.SmallInteger)
    images = db.Column(db.String(1000), nullable=True)
    chara = db.Column(db.Text(), nullable=True)
    calorie = db.Column(db.String(100), nullable=True)
    protein = db.Column(db.String(100), nullable=True)
    lipid = db.Column(db.String(100), nullable=True)
    carbohydrate = db.Column(db.String(100), nullable=True)
    carb = db.Column(db.String(100), nullable=True)
    loc_code  = db.Column(db.String(16), nullable=True)
    req_flg = db.Column(db.SmallInteger)
    del_flg = db.Column(db.SmallInteger)
    regAt = db.Column(db.Integer)
    updAt = db.Column(db.Integer)
    salt = db.Column(db.Float)

    def __init__(self, name , status , images , chara , calorie , protein , lipid , carbohydrate , carb , loc_code  ,req_flg , del_flg , regAt ,updAt , salt ):
        #self.id = id
        self.name = name
        self.status = status
        self.images = images
        self.chara = chara
        self.calorie = calorie
        self.protein = protein
        self.lipid = lipid
        self.carbohydrate = carbohydrate
        self.carb = carb
        self.loc_code  = loc_code
        self.req_flg = req_flg
        self.del_flg = del_flg
        self.regAt = regAt
        self.updAt = updAt
        self.salt = salt


class master_tags(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tag_id = db.Column(db.Integer)
    name = db.Column(db.String(500), unique=True, nullable=True)
    tag_cat_id = db.Column(db.Integer)
    del_flg = db.Column(db.SmallInteger)
    regAt = db.Column(db.Integer)
    updAt = db.Column(db.Integer)

    def __init__(self, tag_id , name,  tag_cat_id,  del_flg,  regAt , updAt):
        #self.id  = id
        self.tag_id = tag_id 
        self.name = name
        self.tag_cat_id = tag_cat_id
        self.del_flg = del_flg
        self.regAt = regAt 
        self.updAt = updAt
    
class user_tag_items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_id = db.Column(db.Integer)
    tag_id = db.Column(db.Integer)
    del_flg = db.Column(db.Integer)
    regAt  = db.Column(db.Integer)
    updAt = db.Column(db.Integer)
   
    def __init__(self, item_id, tag_id, del_flg, regAt, updAt):
        self.item_id = item_id
        self.tag_id = tag_id
        self.del_flg = del_flg
        self.regAt = regAt
        self.updAt = updAt


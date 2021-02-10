from app import app, db
from app.models import user_tag_items, master_items, master_tags
from flask import jsonify, request
import time


@app.route('/')
def index():
    page = 0
    per_page = 10
    items = []

    m_item = master_items.query.paginate(page,per_page,error_out=False)

    for i in m_item.items:
        item = i.__dict__
        item.pop('_sa_instance_state')

        items.append(item)

    response = {"result":items}
    
    return jsonify(response), 200


@app.route('/<id>', methods=['GET'])
def detail(id):
    m_item = master_items.query.filter_by(id=id).first()
    
    if m_item:
        m_tags = master_tags.query\
            .join(user_tag_items, master_tags.id==user_tag_items.tag_id)\
            .filter(user_tag_items.item_id==id)\
            .all()
        ingredients = [i.name for i in m_tags]

        result = {
            "id": m_item.id,
            "name": m_item.name,
            "status": m_item.status,
            "chara": m_item.chara,
            "images": m_item.images,
            "ingredients": ingredients,
            "nutrition": {
                "calorie": m_item.calorie,
                "protein": m_item.protein,
                "lipid": m_item.lipid,
                "carbohydrate": m_item.carbohydrate,
                "carb": m_item.carb,
                "salt": m_item.salt
            }
        }

        return jsonify(result), 200
    else:
        return jsonify({"result":f"ID:{id} not found"}), 404


@app.route('/', methods=['POST'])
def register():
    data = request.form
    cur_time = int(time.time())
    
    m_item = master_items(data.get('name'), data.get('status'), data.get('images'), data.get('chara'), data.get('calorie'), data.get('protein'), data.get('lipid'), data.get('carbohydrate'), data.get('carb'), data.get('loc_code'), data.get('req_flg'), data.get('del_flg'), cur_time, cur_time, data.get('salt'))
    
    db.session.add(m_item)
    db.session.commit()

    return jsonify({"result":'created'}), 201


@app.route('/<id>', methods=['PUT'])
def update(id):
    data = request.form
    m_item = master_items.query.filter_by(id=id)

    if m_item.first():
        m_item.update(data)
        db.session.commit()

        return jsonify({"result":'updated'}), 200
    else:
        return jsonify({"result":f"ID:{id} not found"}), 404


@app.route('/<id>', methods=['DELETE'])
def delete(id):
    m_item = master_items.query.filter_by(id=id)

    if m_item.first():
        m_item.delete()
        db.session.commit()

        return jsonify({"result":'deleted'}), 200
    else:
        return jsonify({"result":f"ID:{id} not found"}), 404


if __name__ == '__main__':
   #db.create_all()
   app.run(debug = True)
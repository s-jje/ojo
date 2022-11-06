from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:test@cluster0.b5hksj0.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/comments', methods=['GET'])
def show_comment():
    comment_list = list(db.comments.find({}))
    for comment in comment_list:
        comment['_id'] = str(comment['_id'])

    return jsonify({'comments': comment_list})


@app.route('/comments', methods=['POST'])
def post_comment():
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']
    time_receive = request.form['time_give']

    doc = {
        'comment': comment_receive,
        'name': name_receive,
        'time': time_receive
    }
    comment_id = db.comments.insert_one(doc).inserted_id

    return jsonify({'comment_id': str(comment_id)})


@app.route('/comments', methods=['DELETE'])
def delete_comment():
    comment_id_receive = request.form['comment_id_give']
    db.comments.delete_one({'_id': ObjectId(comment_id_receive)})

    return jsonify({'msg': '댓글 삭제 완료'})


@app.route('/comments', methods=['PATCH'])
def update_comment():
    comment_id_receive = ObjectId(request.form['comment_id_give'])
    comment_receive = request.form['comment_give']
    db.comments.update_one({'_id': comment_id_receive}, {'$set': {'comment': comment_receive}})

    return jsonify({'msg': '댓글 수정 완료'})


@app.route('/sw')
def popup_sw():
    return render_template('Profile_SW.html')


@app.route('/se')
def popup_se():
    return render_template('Profile_SE.html')


@app.route('/yb')
def popup_yb():
    return render_template('Profile_YB.html')


@app.route('/sj')
def popup_sj():
    return render_template('Profile_SJ.html')


@app.route('/yj')
def popup_yj():
    return render_template('Profile_YJ.html')


@app.route("/sw/comments", methods=["POST"])
def post_comment_sw():
    comment_receive = request.form['comment_give']
    doc = {
        'comment': comment_receive,
    }
    db.comments_SW.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route("/se/comments", methods=["POST"])
def post_comments_se():
    comment_receive = request.form['comment_give']
    doc = {
        'comment': comment_receive,
    }
    db.comments_SE.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route("/yb/comments", methods=["POST"])
def post_comments_yb():
    comment_receive = request.form['comment_give']
    doc = {
        'comment': comment_receive,
    }
    db.comments_YB.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route("/sj/comments", methods=["POST"])
def post_comments_sj():
    comment_receive = request.form['comment_give']
    doc = {
        'comment': comment_receive,
    }
    db.comments_SJ.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route("/yj/comments", methods=["POST"])
def post_comments_yj():
    comment_receive = request.form['comment_give']
    doc = {
        'comment': comment_receive,
    }
    db.comments_YJ.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route("/sw/comments", methods=['DELETE'])
def delete_comment_sw():
    delete_receive = request.form['comment_give']
    db.comments_SW.delete_one({'comment': delete_receive})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/se/comments", methods=['DELETE'])
def delete_comment_se():
    delete_receive = request.form['comment_give']
    db.comments_SE.delete_one({'comment': delete_receive})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/yb/comments", methods=['DELETE'])
def delete_comment_yb():
    delete_receive = request.form['comment_give']
    db.comments_YB.delete_one({'comment': delete_receive})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/sj/comments", methods=['DELETE'])
def delete_comment_sj():
    delete_receive = request.form['comment_give']
    db.comments_SJ.delete_one({'comment': delete_receive})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/yj/comments", methods=['DELETE'])
def delete_comment_yj():
    delete_receive = request.form['comment_give']
    db.comments_YJ.delete_one({'comment': delete_receive})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/sw/comments", methods=["GET"])
def show_comments_sw():
    comments_list = list(db.comments_SW.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


@app.route("/se/comments", methods=["GET"])
def show_comments_se():
    comments_list = list(db.comments_SE.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


@app.route("/yb/comments", methods=["GET"])
def show_comments_yb():
    comments_list = list(db.comments_YB.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


@app.route("/sj/comments", methods=["GET"])
def show_comments_sj():
    comments_list = list(db.comments_SJ.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


@app.route("/yj/comments", methods=["GET"])
def show_comments_yj():
    comments_list = list(db.comments_YJ.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)

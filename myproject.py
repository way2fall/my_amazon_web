from flask import Flask, render_template, redirect, url_for, session, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youcouldneverfindoutwhatthisishahaha'   # 设置密钥防止CSRF攻击
manager = Manager(app)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = 'uploads'   # 设置上传文件的目录，同时一定要保证服务器上有该路径，因为不会自动生成
ALLOWED_EXTENSIONS = ['txt', 'xlsx', 'xls']    # 设置允许的文件格式

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    # 配置上传文件目录


# 定义表单类
class AdwordsForm(Form):
    adwords_file = FileField()
    submit = SubmitField('Submit')


class JapanForm(Form):
    jp_words = TextAreaField('请输入关键词：', validators=[DataRequired()])
    submit = SubmitField('Submit')


# 文件格式检查，有“.”并且是允许的格式则返回True
def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1] in ALLOWED_EXTENSIONS


def split_words(words):
    with open('brands.txt') as b:
        brands = [brand.strip().lower() for brand in b.readlines()]    # 将brands全部转为小写
        # print(brands)
    words_chaos = list(set([i.lower() for i in words]) - set(brands))    # 将传入的word列表转为小写后删除brands中的品牌
    # words_chaos.sort(key=words.index)    # 当words_chaos中包含words中没有的词时无法这样使用
    length = 0
    partial = []
    nested_partial = []
    final = []
    for i in words_chaos:
        if length + len(i) + 1 < 100:
            if i != words_chaos[-1]:
                nested_partial.append(i)
                length = length + len(i) + 1
            else:
                nested_partial.append(i)
                partial.append(nested_partial)
                length = 0
                nested_partial = []
        else:
            partial.append(nested_partial)
            nested_partial = []
            nested_partial.append(i)
            length = len(i) + 1

    for i in partial:
        j = ','.join(i)
        final.append(j)
    return final


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=('GET', 'POST'))
def upload():
    form = AdwordsForm()    # 实例化一个表单
    if form.validate_on_submit():
        # 通过secure_filename获取安全的文件名，并使用session来保存，原因是下面使用了POST/重定向/GET方法，需要在请求间保存数据
        # 不然render_template中的filename永远为空了
        session['filename'] = secure_filename(form.adwords_file.data.filename)
        if allowed_file(session.get('filename')):
            form.adwords_file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], session.get('filename')))    # 保存文件
            print('{} uploaded successfully!'.format(session.get('filename')))
        else:
            session['filename'] = None
            flash('不支持的格式')
            print('Invalid file!!')
        return redirect(url_for('upload'))    # POST/重定向/GET方法
    return render_template('upload.html', form=form, filename=session.get('filename'))


@app.route('/instashaper', methods=('GET', 'POST'))
def instashaper():
    form = JapanForm()
    if form.validate_on_submit():
        new_words = form.jp_words.data.split('/n')
        keywords = []
        for i in new_words:
            j = i.split()
            keywords.extend(j)
        new_keywords = list(set(keywords))
        new_keywords.sort(key=keywords.index)
        # print(new_keywords)
        new_keywords = split_words(new_keywords)
        # print(new_keywords)

        return render_template('instashaper_result.html', new_words=new_keywords)
    return render_template('instashaper.html', form=form)


if __name__ == '__main__':
    manager.run()

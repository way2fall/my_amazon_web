from flask import Flask, render_template, redirect, url_for, session, flash
from flask_script import Manager    # flask.ext. 已经deprecated，现在开始使用flask_
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youcouldneverfindoutwhatthisishahaha'   # 设置密钥防止CSRF攻击
manager = Manager(app)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = 'uploads'   # 设置上传文件的目录，同时一定要保证服务器上有该路径，因为不会自动生成
ALLOWED_EXTENSIONS = []    # 设置允许的文件格式

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    # 配置上传文件目录


# 定义表单类
class AdwordsForm(Form):
    adwords_file = FileField()
    submit = SubmitField('Submit')


class JapanForm(Form):
    jp_words = TextAreaField('请输入关键词：', validators=[DataRequired()])
    # 一定要coerce=int，否则前台会提示not a valid choice
    group_num = SelectField('每组字符数', choices = [(1000, 1000), (750,750), (500, 500), (250, 250), (100, 100), (50, 50)], coerce=int)
    submit = SubmitField('Submit')


class PhraseForm(Form):
    ad_words = TextAreaField('请输入关键词：', validators=[DataRequired()])
    # 一定要coerce=int，否则前台会提示not a valid choice
    group_num = SelectField('每组字符数', choices = [(1000, 1000), (750,750), (500, 500), (250, 250), (100, 100), (50, 50)], coerce=int)
    submit = SubmitField('Submit')


# 文件格式检查，有“.”并且是允许的格式则返回True
def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1] in ALLOWED_EXTENSIONS


def split_phrases(phrases, limit):
    with open('brands.txt', encoding='utf-8') as b:
        brands = [brand.strip().lower() for brand in b.readlines()]
    phrases = [i.strip().lower() for i in phrases]
    phrases_li = []
    for i in phrases:
        phrase_list = i.split(' ')
        new_phrase = ' '.join([i for i in phrase_list if i not in brands])
        # print('this is new phrase:', new_phrase)
        phrases_li.append(new_phrase)
        # print(phrase_list)
    # return phrases_li
    # print(phrases_li)
    length = 0
    inner_group = []
    outer_group = []
    final = []
    for i in phrases_li:
        if length + len(i) < limit:
            # print("AAA")
            if i != phrases_li[-1]:
                # print("CCC")
                inner_group.append(i)
                # print(i)
                length = length + len(i) + 1
            else:
                # print('DDD')
                inner_group.append(i)
                outer_group.append(inner_group)
                length = 0
                inner_group = []

        elif i != phrases_li[-1]:
            # print("BBB")
            outer_group.append(inner_group)
            inner_group = []
            inner_group.append(i)
            length = len(i) + 1
        else:
            outer_group.append(inner_group)
            inner_group = []
            inner_group.append(i)
            outer_group.append(inner_group)

    for j in outer_group:
        k = ','.join(j)
        final.append(k)

    return final


def split_words(words, limit):
    with open('brands.txt', encoding='utf-8') as b:
        brands = [brand.strip().lower() for brand in b.readlines()]    # 将brands全部转为小写
        # print(brands)
    words_chaos = list(set([i.lower() for i in words]) - set(brands))    # 将传入的word列表转为小写后删除brands中的品牌
    words = [i.strip().lower() for i in words]
    words_chaos.sort(key=words.index)    # 当words_chaos中包含words中没有的词时无法这样使用
    length = 0
    partial = []
    nested_partial = []
    final = []
    for i in words_chaos:
        if length + len(i) + 1 < limit:
            if i != words_chaos[-1]:
                nested_partial.append(i)
                length = length + len(i) + 1
            else:
                nested_partial.append(i)
                partial.append(nested_partial)
                length = 0
                nested_partial = []
        elif i != words_chaos[-1]:
            partial.append(nested_partial)
            nested_partial = []
            nested_partial.append(i)
            length = len(i) + 1
        else:
            partial.append(nested_partial)
            nested_partial = []
            nested_partial.append(i)
            partial.append(nested_partial)

    for i in partial:
        j = ' '.join(i)
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
    print(form.group_num.data)
    if form.validate_on_submit():
        new_words = form.jp_words.data.split('\n')
        random.shuffle(new_words)
        keywords = []
        for i in new_words:
            j = i.split()
            keywords.extend(j)
        new_keywords = list(set(keywords))
        new_keywords.sort(key=keywords.index)
        # print(new_keywords)
        new_keywords = split_words(new_keywords, form.group_num.data)
        # print(new_keywords)
        return render_template('instashaper_result.html', new_words=new_keywords)
    return render_template('instashaper.html', form=form)


@app.route('/phraseshaper', methods=('GET', 'POST'))
def phraseshaper():
    form = PhraseForm()
    if form.validate_on_submit():
        new_words = form.ad_words.data.split('\n')
        random.shuffle(new_words)
        new_keywords = split_phrases(new_words, form.group_num.data)

        return render_template('phraseshaper_result.html', new_keywords=new_keywords)

    return render_template('phraseshaper.html', form=form)



if __name__ == '__main__':
    manager.run()

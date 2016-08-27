from flask import render_template, redirect, url_for, session, flash, current_app
from .forms import AdwordsForm, JapanForm, PhraseForm, BrandSubmit
import random
from . import main
from ..words_process import split_words, split_phrases, allowed_file
from werkzeug.utils import secure_filename
import os


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/upload', methods=('GET', 'POST'))
def upload():
    form = AdwordsForm()    # 实例化一个表单
    if form.validate_on_submit():
        # 通过secure_filename获取安全的文件名，并使用session来保存，原因是下面使用了POST/重定向/GET方法，需要在请求间保存数据
        # 不然render_template中的filename永远为空了
        session['filename'] = secure_filename(form.adwords_file.data.filename)
        if allowed_file(session.get('filename')):
            form.adwords_file.data.save(os.path.join(current_app.config['UPLOAD_FOLDER'], session.get('filename')))    # 保存文件
            print('{} uploaded successfully!'.format(session.get('filename')))
        else:
            session['filename'] = None
            flash('不支持的格式')
            print('Invalid file!!')
        return redirect(url_for('.upload'))    # POST/重定向/GET方法
    return render_template('upload.html', form=form, filename=session.get('filename'))


@main.route('/instashaper', methods=('GET', 'POST'))
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


@main.route('/phraseshaper', methods=('GET', 'POST'))
def phraseshaper():
    form = PhraseForm()
    if form.validate_on_submit():
        new_words = form.ad_words.data.split('\n')
        random.shuffle(new_words)
        new_keywords = split_phrases(new_words, form.group_num.data)

        return render_template('phraseshaper_result.html', new_keywords=new_keywords)

    return render_template('phraseshaper.html', form=form)


@main.route('/brandsubmitly998899', methods=('GET','POST'))
def brands_sub():
    form = BrandSubmit()
    if form.validate_on_submit():
        with open('brands.txt', 'a') as br:
            br.write(form.brand_file.data+'\n')
        return render_template('brand_result.html')
    return render_template('brand_submit.html', form=form)
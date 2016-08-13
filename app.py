from flask import Flask, render_template, redirect, url_for, session, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HARD TO GUESS STRING'   # 设置密钥防止CSRF攻击
manager = Manager(app)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = 'uploads'   # 设置上传文件的目录，同时一定要保证服务器上有该路径，因为不会自动生成
ALLOWED_EXTENSIONS = ['txt', 'xlsx', 'xls']    # 设置允许的文件格式

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    # 配置上传文件目录


# 定义表单类
class AdwordsForm(Form):
    adwords_file = FileField()
    submit = SubmitField('Submit')


# 文件格式检查，有“.”并且是允许的格式则返回True
def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1] in ALLOWED_EXTENSIONS


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


if __name__ == '__main__':
    manager.run()

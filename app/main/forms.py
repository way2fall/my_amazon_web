from wtforms import FileField, SubmitField, TextAreaField, SelectField
from flask_wtf import Form
from wtforms.validators import DataRequired


class AdwordsForm(Form):
    adwords_file = FileField()
    submit = SubmitField('Submit')


class JapanForm(Form):
    jp_words = TextAreaField('请输入关键词，结果以不重复的单个词语呈现：', validators=[DataRequired()])
    # 一定要coerce=int，否则前台会提示not a valid choice
    group_num = SelectField('每组字符数', choices=[(1000, 1000), (750, 750),
                                              (500, 500), (250, 250), (100, 100), (50, 50)], coerce=int)
    submit = SubmitField('Submit')


class PhraseForm(Form):
    ad_words = TextAreaField('请输入关键词，结果以乱序的长尾词呈现：', validators=[DataRequired()])
    # 一定要coerce=int，否则前台会提示not a valid choice
    group_num = SelectField('每组字符数', choices=[(1000, 1000), (750, 750),
                                              (500, 500), (250, 250), (100, 100), (50, 50)], coerce=int)
    submit = SubmitField('Submit')


class BrandSubmit(Form):
    brand_file = TextAreaField('请输入品牌名：', validators=[DataRequired()])
    submit = SubmitField('Submit')
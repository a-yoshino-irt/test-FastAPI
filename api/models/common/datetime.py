# 作成日時や更新日時のデフォルト値をJST時間で入れるためのクラスと関数
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime


class JstNow(expression.FunctionElement):
    type = DateTime()

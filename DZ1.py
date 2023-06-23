from jinja2 import Template

button = [
    {'href': '/index', 'class': 'active', 'title': 'Главная'},
    {'href': '/news', 'class': '', 'title': 'Новости'},
    {'href': '/about', 'class': '', 'title': 'О компании'},
    {'href': '/shop', 'class': '', 'title': 'Магазин'},
    {'href': '/contacts', 'class': '', 'title': 'Контакты'}
]

html = """
{% macro menu(list) -%}
    <ul>
        {%- for m in list -%}
            {% if m.class == '' %}
            <li><a href="{{ m.href }}">{{ m.title }}</a></li>
            {% else %}
            <li><a href="{{ m.href }}" class="{{ m.class }}">{{ m.title }}</a></li>
            {% endif %}
        {%- endfor %}
    </ul>
{% endmacro %}

{{ menu(but) }}
"""

tm = Template(html)
msg = tm.render(but=button)
print(msg)


# put = [
#     {'type': 'text', 'name': 'firstname', 'placeholder': 'Имя'},
#     {'type': 'text', 'name': 'lastname', 'placeholder': 'Фамилия'},
#     {'type': 'text', 'name': 'address', 'placeholder': 'Адрес'},
#     {'type': 'tel', 'name': 'phone', 'placeholder': 'Телефон'},
#     {'type': 'email', 'name': 'email', 'placeholder': 'Почта'}
# ]
#
# info = """
# {% macro p_info(list) -%}
#     {% for p in list %}
#     <p><input type="{{ p.type }}" name="{{ p.name }}" placeholder="{{ p.placeholder }}"></p>
#     {% endfor %}
# {% endmacro %}
#
# {{ p_info(put) }}
# """
#
# pm = Template(info)
# dannie = pm.render(put=put)
# print(dannie)






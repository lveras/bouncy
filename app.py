# -*- coding: utf-8 -*-
# Copyright (C) 2019  Luciano Veras
#
# Teste prático para a vaga de Desenvolvedor Python
# Empresa: 3con

from flask import Flask, render_template
from teste_pratico import TestePratico
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)


def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.ylabel('Percent bouncy')
    plt.xlabel('Number')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return 'data:image/png;base64,{}'.format(graph_url)


@app.route('/')
def index(chart=False):
    if chart:
        d = TestePratico()
        df_res = d.bouncy()
        chart_url = build_graph(df_res['Number'], df_res['Bouncy Percent'])

        return render_template('chart.html', chart=chart_url,
                               num=df_res['Number'].max())

    else:
        return render_template('index.html')


@app.route('/chart')
def chart():
    return index(chart=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

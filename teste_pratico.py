# -*- coding: utf-8 -*-
# Copyright (C) 2019  Luciano Veras
#
# Teste prático para a vaga de Desenvolvedor Python
# Empresa: 3con

import pandas as pd


class TestePratico(object):
    def __init__(self):
        point = 1
        new_point = 21781
        
        self.df = pd.DataFrame(columns=['num', 'bouncy'])
        self.df = self.df.append(self.inc_range(
            point=point, new_point=new_point))
        
        self.percent = self.check_percent()
    
    @staticmethod
    def filter_bouncy(val):
        res = []
        num = [int(v) for v in str(val)]
        res.append(num)
        num.reverse()
        res.append(num)
    
        for n in res:
            i = 1
            while i < len(n):
                if n[i] < n[i - 1]:
                    return False
                i = i + 1
    
        return True

    def inc_range(self, point, new_point):
        
        res = [{'num': i, 'bouncy': self.filter_bouncy(i)}
                for i in range(int(point), int(new_point)+1)]
        
        return res

    def check_percent(self):
        res = self.df[self.df['bouncy'] == False].count() * 100 / \
              self.df.count()
        return res[0]

    def bouncy(self):
        df_res = pd.DataFrame(columns=['Number', 'Bouncy Percent'])
        while True:
            point = self.df['num'].max()
            percent = self.check_percent()
            df_res = df_res.append({'Number': point, 'Bouncy Percent': percent},
                                   ignore_index=True)
            print('Num: {} | Percent: {}'.format(point, percent))

            if percent < 99:
                new_point = int(point * 99 / percent)
                new_point = new_point + 1 if new_point == point else new_point
                
                vals = self.inc_range(point=point, new_point=new_point)

                self.df = self.df.append(vals)

            else:
                return df_res

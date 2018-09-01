import os
import csv
import datetime
from django.db import models


PLATAFORMAS_CHOICES = (
    ('Não identificado', 'Não identificado'),
    ('TV', 'TV'),
    ('Mobile', 'Mobile'),
    ('Site', 'Site'),
    ('Game', 'Game'),
    ('Back End', 'Back End'),
    ('Todos', 'Todos'),

)


class Formulario(models.Model):
    tipo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    plataforma = models.CharField(max_length=20, choices=PLATAFORMAS_CHOICES)
    marca = models.CharField(max_length=250, blank=True, null=True)
    provedores = models.CharField(max_length=250, blank=True, null=True, default='Não identificado')
    datainicio = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Data de Início")
    datafim = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True, verbose_name="Data de Fim")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.tipo,
            self.descricao,
            self.plataforma
        )

    def save(self, *args, **kwargs):
        from django.conf import settings

        object_dict = {
             'tipo': self.tipo,
             'descricao': self.descricao,
             'plataforma': self.plataforma,
             'marca': self.marca,
             'provedores': self.provedores,
             'datainicio': self.datainicio.strftime("%Y%m%d"),
             'datafim': self.datafim,
             'observacao': self.observacao,
             'created': self.created
        }

        if object_dict['datafim']:
            object_dict['datafim'] = object_dict['datafim'].strftime("%Y%m%d")
        else:
            pass

        filename = 'formulario.csv'
        complete_path = os.path.join(settings.MEDIA_ROOT, filename)

        fieldnames = [
            'tipo',
            'descricao',
            'plataforma',
            'marca',
            'provedores',
            'datainicio',
            'datafim',
            'observacao',
            'created'
        ]

        with open(complete_path, 'w', newline='\n', encoding='utf-8') as csv_file:
            cw = csv.DictWriter(
                csv_file, fieldnames,
                delimiter='|', quoting=csv.QUOTE_ALL,
            )
            cw.writeheader()
            cw.writerow(object_dict)


        super(Formulario, self).save(*args, **kwargs)




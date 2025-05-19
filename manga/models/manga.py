# manga_library/models/manga.py

from odoo import models, fields

class Monmanga(models.Model):
    _name = 'manga.monmanga'
    _description = 'Manga'

    nom = fields.Char(string='Titre', required=True)
    auteur = fields.Char(string='Auteur')
    anne_parution = fields.Integer('anné de parution')

    def create_manga(self):
        self.env['manga.monmanga'].create({
            'nom': 'One Piece',
            'auteur': 'Eiichiro Oda',  
            'anne_parution': 1997,
        })

    def init(self):
        self.create_manga()

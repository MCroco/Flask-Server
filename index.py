"""
Created on 2020-01-10 Last Update 2020-01-23
@author : Jacques Gérard - UNamur (www.unamur.be)
@author : Fabrice Orbant - UNamur (www.unamur.be)
"""
if __name__ == '__main__': from SHIDev.session import loginRequired
from SHI.web import webPage
from yattag import Doc
import SHI.local_db as db
from SHI.tools import sizingImage
import parametres
import menuProf
import menuEtu
import tableau_de_bord_prof
import tableau_de_bord_moderateur
from vues.personne import PersonPageView
from datetime import datetime,date


@loginRequired
def page(S = None):
    doc, tag, text = Doc().tagtext()
    if S:
        with tag('div',klass='wrapper'):
            # doc, tag, text = menu_moderateur.sidebar(doc, tag, text)
            """TABLEAU DE BORD PROFS"""
            # doc, tag, text = tableau_de_bord_prof.tableau_de_bord_page(doc, tag, text)
            doc, tag, text = tableau_de_bord_moderateur.tableau_de_bord_page(doc, tag, text)
            # doc, tag, text = tableau_de_bord_admin.tableau_de_bord_page(doc, tag, text)
            # doc, tag, text = tableau_de_bord_etudiant.tableau_de_bord_page(doc, tag, text)
                           
        webPage(Page = doc, Session = S, CSS='dist/css/mycss.css', JS='myjs.js')
    else:
        webPage(doc)



if __name__ == '__main__':
    page()

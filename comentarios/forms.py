from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):

        raw_data = self.data
        recaptcha_responde = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(   
            'https://www.google.com/recaptcha/api/siteverify',
            data = {
                'secret': '6LdUwVMmAAAAAE67PNIfK2NYxLqvd1RwxEm8-wBC',
                'response': recaptcha_responde
            }
        )

        recaptcha_result = recaptcha_request.json()
        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpa, ocorreu um erro, tente novamente.'
            )


        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

    
    # if not comenatrio:
    #     self.add_error(
    #         'comentario',
    #         'Você não infomrou um comentario!!'

    #     )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')



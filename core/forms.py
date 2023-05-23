from django import forms

from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField


# TODO: replace Form with ModelForm
class VolunteerForm(forms.Form):

    template_name = "forms/daisyui-form.html"

    def __init__(self, fields=[],  *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.fields = fields


class PeopleForm(forms.Form):
    first_name = CharField(label="Primeiro nome", max_length=15, required=True)
    last_name = CharField(label="Sobrenome", required=False, max_length=15)
    email = EmailField(label="Seu melhor e-mail", required=True)
    whatsapp = MaskField(label="Número de telefone", mask="(00) 0 0000-0000")
    zipcode = ZipCodeField(label="CEP de atendimento",
                           mask="00000-000", required=True)

    template_name = "forms/daisyui-form.html"


COLOR_CHOICES = (
    ("", "Cor"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Indígena", "Indígena"),
    ("Amarela", "Amarela"),
    ("Branca", "Branca"),
)

GENDER_CHOICES = (
    ("", "Identidade de gênero"),
    ("Mulher cisgênero", "Mulher cisgênero (que se identifica com o sexo que lhe foi designado ao nascer)"),
    ("Mulher transgênero/travesti",
     "Mulher transgênero/travesti (possui outra identidade de gênero, diferente da que lhe foi designada ao nascer)"),
    ("Prefiro não responder", "Prefiro não responder"),
)


class People2Form(forms.Form):
    color = ChoiceField(label="Cor", choices=COLOR_CHOICES)
    gender = ChoiceField(label="Identidade de gênero", choices=GENDER_CHOICES)
    phone = MaskField(label="Telefone de atendimento com DDD",
                      mask="(00) 0 0000-0000")

    document_number = MaskField(label="CRP", mask="00/000000", required=True)
    # document_number = MaskField(label="OAB", mask="(00) 0 0000-0000")

    template_name = "forms/daisyui-form.html"

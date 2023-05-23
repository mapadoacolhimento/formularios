from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


from .forms import PeopleForm, People2Form, VolunteerForm
from .choices import (
    COLOR_CHOICES,
    GENDER_CHOICES,
    AVAILABILITY_CHOICES,
    MODALITY_CHOICES,
    LIBRAS_CHOICE,
)
from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField
from django.contrib.auth.models import User

# Create your views here.
step_forms = {
    1: {
        "first_name": CharField(label="Primeiro nome", required=True),
        "last_name": CharField(label="Sobrenome", required=False),
        "email": EmailField(label="Seu melhor e-mail"),
        "whatsapp": MaskField(label="Número de telefone", mask="(00) 0 0000-0000"),
        "zipcode": ZipCodeField(label="CEP de atendimento", mask="00000-000"),
    },
    2: {
        "color": ChoiceField(label="Cor", choices=COLOR_CHOICES),
        "gender": ChoiceField(label="Identidade de gênero", choices=GENDER_CHOICES),
        "phone": MaskField(
            label="Telefone de atendimento com DDD", mask="(00) 0 0000-0000"
        ),
        "document_number": MaskField(label="CRP", mask="00/000000"),
    },
    3: {
        "Vagas para atendimento:": ChoiceField(
            label="Vagas para atendimento:", choices=AVAILABILITY_CHOICES
        ),
        "Modalidade de atendimento:": ChoiceField(
            label="Modalidade de atendimento", choices=MODALITY_CHOICES
        ),
        "Atende em linguagem de sinais (libras):": ChoiceField(
            label="Atende em linguagem de sinais (libras)", choices=LIBRAS_CHOICE
        ),
    },
    4: {
        "Há quanto tempo você atua com acolhimento de mulheres em situação de violência?": ChoiceField(
            widget=forms.RadioSelect,
            choices=[
                ('0', 'Não tenho experiência'),
                ('1/2', 'Menos 6 meses'),
                ('1', 'Menos de 1 ano'),
                ('2', 'Menos de 2 anos'),
                ('5', 'Menos de 5 anos'),
                ('9', 'Menos de 10 anos'),
                ('10', 'Mais de 10 anos'),
            ], required=False),
    },
    5: {
        "": ChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[
                ('violência contra as mulheres', 'Violência contra as mulheres'),
                ('assistência social', 'Assistência social'),
                ('saúde mental', 'Saúde mental'),
                ('psicologia clínica', 'Psicologia clínica'),
                ('psicologia jurídica', 'Psicologia jurídica'),
                ('psicologia social', 'Psicologia social'),
                ('terapia sistêmica/familiar', 'Terapia sistêmica/familiar'),
                ('serviços públicos', 'Serviços públicos'),
                ('não tenho experiência', 'Não tenho experiência'),
                ('outros', 'Outros'),
            ]),
    },
     6: {
         "": ChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[
                ('psicologia analítica de jung ou análise junguiana', 'Psicologia Analítica de Jung ou Análise Junguiana'),
                ('assistência social', 'Assistência social'),
                ('psicanálise', 'Psicanálise'),
                ('behaviorismo ou analítico comportamental', 'Behaviorismo ou Analítico Comportamental'),
                ('humanismo', 'Humanismo'),
                ('psicoterapia corporal', 'Psicoterapia Corporal'),
                ('cognitivo-Comportamental ou tcc', 'Cognitivo-Comportamental ou TCC'),
                ('gestalt-terapia', 'Gestalt-terapia'),
                ('abordagem centrada na Pessoa (acp)', 'Abordagem Centrada na Pessoa (ACP)'),
                ('outros', 'Outros'),
            ]),
    },
}

def index(request):
    return render(request=request, template_name="home.html")


def fill_steps(request, type_form, step):
    fields = step_forms.get(step)
    if not fields:
        raise Exception("Etapa não existe")

    if request.method == "POST":
        form = VolunteerForm(fields=fields, data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/{type_form}/{step+1}")
        else:
            if step == list(step_forms)[-1]:
                return HttpResponseRedirect("/")
    else:
        form = VolunteerForm(fields=fields)

    return render(request, "forms/people.html", {"form": form})

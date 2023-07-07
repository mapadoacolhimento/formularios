from core.bonde.models import FormEntries, Activists

from core.models import FormData
import json


def create_new_form_entrie(form_data: FormData):
    activist, created = Activists.objects.get_or_create(email=form_data.values["email"])

    if created:
        activist.first_name = form_data.values["first_name"]
        activist.last_name = form_data.values["last_name"]
        activist.name = (
            form_data.values["first_name"] + " " + form_data.values["last_name"]
        )
        activist.save()

    if form_data.type_form == "psicologa":
        widget_id = 17628
        form_mapping = [
            {
                "uid": "field-1533733461113-5",
                "kind": "text",
                "label": "NOME",
                "placeholder": "",
                "required": True,
                "value": form_data.values["first_name"]
            },
            {
                "uid": "field-1533733485653-99",
                "kind": "text",
                "label": "SOBRENOME",
                "placeholder": "",
                "required": True,
                "value": form_data.values["last_name"]
            },
            {
                "uid": "field-1533733493037-11",
                "kind": "email",
                "label": "SEU MELHOR EMAIL",
                "placeholder": "",
                "required": True,
                "value": form_data.values["email"]
            },
            {
                "uid": "field-1533733501716-34",
                "kind": "text",
                "label": "CRP (Só números)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["document_number"]
            },
            {
                "uid": "field-1533733650118-7",
                "kind": "text",
                "label": "CEP DE ATENDIMENTO (Só números)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["zipcode"]
            },
            {
                "uid": "field-1533734419113-13",
                "kind": "text",
                "label": "TELEFONE PARA ATENDIMENTO (COM DDD)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["phone"]
            },
            {
                "uid": "field-1533734468460-38",
                "kind": "text",
                "label": "WHATSAPP (COM DDD)",
                "placeholder": "Obrigatório para contato com a equipe",
                "required": True,
                "value": form_data.values["whatsapp"]
            },
            {
                "uid": "field-1533734495315-40",
                "kind": "dropdown",
                "label": "Como voluntária do Mapa do Acolhimento, você se dispõe a atender, pelo menos, uma (1) mulher que precisa de ajuda. Caso você tenha mais tempo disponível, você pode atender mais de uma (1) mulher, de maneira concomitante. Lembrando que os atendimentos devem ser sempre individuais. Quantas vagas você pode oferecer para atender, simultaneamente, mulheres do Mapa do Acolhimento?",
                "placeholder": "1, 2, 3, 4, 5 ou mais",
                "required": True,
                "value": form_data.values["aviability"]
            },
            {
                "uid": "extra_field_color",
                "label": "color",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["color"]
            },
            {
                "uid": "extra_field_gender",
                "label": "gender",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["gender"]
            },
            {
                "uid": "extra_field_birth_date",
                "label": "birth_date",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["birth_date"]
            },
            {
                "uid": "extra_field_libras",
                "label": "libras",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["libras"]
            },
            {
                "uid": "extra_field_years_of_experience",
                "label": "years_of_experience",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["years_of_experience"]
            },
            
            {
                "uid": "extra_field_approach",
                "label": "approach",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["approach"]
            },
            
            {
                "uid": "extra_field_modality",
                "label": "modality",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["modality"]
            },
            {
                "uid": "extra_field_fields_of_work",
                "label": "fields_of_work",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["fields_of_work"]
            },
            {
                "uid": "extra_field_status",
                "label": "status",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["status"]
            },
        ]
    else:
        widget_id = 17633
        form_mapping = [
            {
                "uid": "field-1533735738039-59",
                "kind": "text",
                "label": "NOME",
                "placeholder": "",
                "required": True,
                "value": form_data.values["first_name"]
            },
            {
                "uid": "field-1533735745400-14",
                "kind": "text",
                "label": "SOBRENOME",
                "placeholder": "",
                "required": True,
                "value": form_data.values["last_name"]
            },
            {
                "uid": "field-1533735752669-39",
                "kind": "email",
                "label": "SEU MELHOR EMAIL",
                "placeholder": "",
                "required": True,
                "value": form_data.values["email"]
            },
            {
                "uid": "field-1533735761357-93",
                "kind": "text",
                "label": "OAB (Só números)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["document_number"]
            },
            {
                "uid": "field-1533735803691-45",
                "kind": "text",
                "label": "CEP DE ATENDIMENTO (Só números)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["zipcode"]
            },
            {
                "uid": "field-1533735813563-2",
                "kind": "text",
                "label": "TELEFONE PARA ATENDIMENTO (COM DDD)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["phone"]
            },
            {
                "uid": "field-1533735832329-53",
                "kind": "text",
                "label": "WHATSAPP (COM DDD)",
                "placeholder": "",
                "required": True,
                "value": form_data.values["whatsapp"]
            },
            {
                "uid": "field-1533735888966-20",
                "kind": "dropdown",
                "label": "Como voluntária do Mapa do Acolhimento, você se dispõe a atender, pelo menos, uma (1) mulher que precisa de ajuda. Caso você tenha mais tempo disponível, você pode atender mais de uma (1) mulher, de maneira concomitante. Quantas vagas você pode oferecer para atender, simultaneamente, mulheres do Mapa do Acolhimento (lembrando que isso pode incluir o acompanhamento de processos do início ao fim) ?",
                "placeholder": "1, 2, 3, 4, 5 ou mais",
                "required": True,
                "value": form_data.values["aviability"]
            },
            {
                "uid": "extra_field_color",
                "label": "color",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["color"]
            },
            {
                "uid": "extra_field_gender",
                "label": "gender",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["gender"]
            },
            {
                "uid": "extra_field_birth_date",
                "label": "birth_date",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["birth_date"]
            },
            {
                "uid": "extra_field_libras",
                "label": "libras",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["libras"]
            },
            {
                "uid": "extra_field_modality",
                "label": "modality",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["modality"]
            },
            
            {
                "uid": "extra_field_years_of_experience",
                "label": "years_of_experience",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["years_of_experience"]
            },
            {
                "uid": "extra_field_fields_of_work",
                "label": "fields_of_work",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["fields_of_work"]
            },
            {
                "uid": "extra_field_status",
                "label": "status",
                "kind": "text",
                "placeholder": "",
                "required": False,
                "value": form_data.values["status"]
            },
        ]

    form_entries = FormEntries.objects.create(
        fields=json.dumps(form_mapping),
        activist=activist,
        widget_id=widget_id,
        mobilization_id=949,
    )

    return form_entries

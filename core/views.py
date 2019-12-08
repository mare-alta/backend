from rest_framework import generics, status
import sys
sys.path.append("..")
from core.serializers import *
import requests
from rest_framework.response import Response
import base64
import json


##########################################################


class base_list(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    """
    sql_string = None
    fields_dict = None

    def filtros_adicionais(self, query, fields):
        fields = {k: [x for x in v if x in self.request.query_params] for k, v in fields.items()}
        fields = {k: v for k, v in fields.items() if len(v) > 0}
        for table, fields in fields.items():
            for field in fields:
                value = self.request.query_params[field]
                adicional = "and {}.{} = '{}'".format(table, field, value)
                query += adicional
        return query

    def get_queryset(self):
        sql_string = self.sql_string
        sql_string = self.filtros_adicionais(query=sql_string, fields=self.fields_dict)
        self_model = self.serializer_class.Meta.model
        r = self_model.objects.raw(sql_string)
        return r


class base_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    """
    lookup_url_kwarg = 'id'
    sql_string = None

    def get_object(self):
        id = self.request.query_params[self.lookup_url_kwarg]
        sql = self.sql_string
        sql = sql.format(id)
        self_model = self.serializer_class.Meta.model
        r = self_model.objects.raw(sql)
        return r[0] if len(r) == 1 else None


##########################################################


class LevelList(base_list):
    serializer_class = LevelSerializer
    sql_string = """SELECT core_level.*
                    FROM core_level
                    where 1=1"""
    fields_dict = {}


class LevelDetail(base_detail):
    serializer_class = LevelSerializer
    sql_string = """SELECT core_level.id
                    FROM core_level
                    where core_level.id = {}"""


class ComplaintList(base_list):
    serializer_class = ComplaintSerializer
    sql_string = """SELECT core_complaint.*
                    FROM core_complaint
                    where 1=1"""
    fields_dict = {'core_level': ['id', ]}

    def post(self, request, *args, **kwargs):
        create_return = self.create(request, *args, **kwargs)

        url = 'http://willianchan.pythonanywhere.com/gravidade'
        myobj = {"texto": create_return.data['desc']}
        return_ml = requests.post(url, json=myobj)
        model = self.serializer_class.Meta.model
        model.objects.filter(pk=create_return.data['id']).update(level_ml_model=return_ml.text.upper())
        ajustado = model.objects.filter(pk=create_return.data['id'])

        return Response(ajustado.values(), status=status.HTTP_201_CREATED)


class ComplaintDetail(base_detail):
    serializer_class = ComplaintSerializer
    sql_string = """SELECT core_complaint.id
                    FROM core_complaint
                    where core_complaint.id = {}"""


class AnswerList(base_list):
    serializer_class = AnswerSerializer
    sql_string = """SELECT core_answer.*
                    FROM core_answer
                    where 1=1"""
    fields_dict = {}


class AnswerDetail(base_detail):
    serializer_class = AnswerSerializer
    sql_string = """SELECT core_answer.id
                    FROM core_answer
                    where core_answer.id = {}"""


class ImageList(base_list):
    serializer_class = ImageSerializer
    sql_string = """SELECT core_image.*
                    FROM core_image
                    where 1=1"""
    fields_dict = {}

    def post(self, request, *args, **kwargs):
        create_return = self.create(request, *args, **kwargs)

        url = 'https://177.67.49.218/powerai-vision-ingram/api/dlapis/ab043177-91a0-4727-8f42-f77a282a13b9'
        file_base64 = create_return.data['image']

        try:
            file_base64 = file_base64[file_base64.find(',') + 1:]
            with open("imageToSave.png", "wb") as fh:
                fh.write(base64.b64decode(file_base64))
            myobj = {"files": open('imageToSave.png', 'rb')}
            return_ml = requests.post(url, files=myobj, verify=False)
            model = self.serializer_class.Meta.model
            r = list(json.loads(return_ml.text)['classified'].keys())[0].upper()
            retorno_api = r if return_ml.status_code == 200 else 'ERRO'
            model.objects.filter(pk=create_return.data['id']).update(appropriate=retorno_api)
            ajustado = model.objects.filter(pk=create_return.data['id'])
            return Response(ajustado.values(), status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))


class ImageDetail(base_detail):
    serializer_class = ImageSerializer
    sql_string = """SELECT core_image.id
                    FROM core_image
                    where core_image.id = {}"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import sys
sys.path.append("..")
from core.serializers import LevelSerializer, ComplaintSerializer


##########################################################


class base_list(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    """
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
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


class ComplaintDetail(base_detail):
    serializer_class = ComplaintSerializer
    sql_string = """SELECT core_complaint.id
                    FROM core_complaint
                    where core_complaint.id = {}"""
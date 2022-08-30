from rest_framework.viewsets import ModelViewSet


class MerFoodCateInfo(ModelViewSet):
    queryset = Food_Category.objects.filter(m_id=3)
    serializer_class = Cate_Ser
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    pagination_class = Bangenter

    def list(self, request, *args, **kwargs):

        token = request.headers.get("Authorization")
        print("token", token)
        payload = check_token(token)
        print("payload:", payload)

        if payload:
            ...


        self.queryset = Food_Category.objects.filter(m_id=m_id)
        return super().list(request, *args, **kwargs)


{"asdf":2345}.setdefault()
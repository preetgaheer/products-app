import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status  
# Create your views here.
from rest_framework import viewsets

from .models import ProductApi, ProductDetails
from .serializer import ProductApiSerialzer

class ProductApiViewset(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = ProductApi.objects.all()  
        serializers = ProductApiSerialzer(result, many=True)  
        return Response({'status': 'success', "products":serializers.data}, status=200)  
  
    def post(self, request): 
        serializer = ProductApiSerialzer(data=request.data)  
        if serializer.is_valid():
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 


class ProductApiViewOthers(APIView):

    def get(self,request, pk):
        product = ProductApi.objects.get(pk=pk)
        product_details = ProductDetails(product=product)
        product_details.save()
        serializer = ProductApiSerialzer(product,  many=False)
        return Response({'data' :serializer.data}, status=status.HTTP_200_OK)  

    def delete(self, pk):
        product = ProductApi.objects.get(pk=pk)
        product.delete()
        return Response({"status": "success", "data": "deleted"}, status=status.HTTP_200_OK)  

    def put(self, request, pk):
        p = ProductApi.objects.get(pk=pk)
        serializer = ProductApiSerialzer(p, data=request.data)
        if serializer.is_valid():
            p.title = request.data['title']
            p.description =  request.data['description']
            p.price =  request.data['price']
            p.save()
            pd = ProductDetails(product= p)
            pd.save()
            return Response(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def filter_weekly(data, days, date_format):
                past_date = datetime.datetime.now()-datetime.timedelta(days=days)
                filtered_products = {}
                for product, dates in data.items():
                    for date in dates:
                        if datetime.datetime.strptime(date, date_format) >= past_date:
                            if filtered_products.get(product) ==None:
                                filtered_products[product]= 1
                            else: 
                                filtered_products[product] += 1          
                return dict(sorted(filtered_products.items(), key=lambda x: x[1], reverse=True)[:5])


class ProductAnalytics(APIView):

    def get(self, request,time):
        p = ProductDetails.objects.all()
        popluar_data= {}
        date_format = "%d-%m-%Y"
        for detail in p:
            if popluar_data.get(detail.product.title)==None:
                popluar_data[detail.product.title] = [detail.retervails_date.strftime(date_format)]
            else:
                popluar_data[detail.product.title].append(detail.retervails_date.strftime(date_format))
        if time == 'all':
            popluar_data = {}
            for detail in p:
                if popluar_data.get(detail.product.title) == None:
                    popluar_data[detail.product.title] = 1
                else:
                    popluar_data[detail.product.title] += 1
            popluar_data = dict(sorted(popluar_data.items(), key=lambda x: x[1], reverse=True)[:5])
            return Response({"top5_all_time": popluar_data}, status=status.HTTP_200_OK)
        elif time == 'daily':
            filtered_products = filter_weekly(popluar_data, 1, date_format)
            return Response({"top5_daily": filtered_products} , status=status.HTTP_200_OK)

        elif time== 'weekly':
            filtered_products =  filter_weekly(popluar_data,7,date_format)
            return Response({"top5_weekly": filtered_products} , status=status.HTTP_200_OK)
        else:
            return Response({"Please pass a valid argument"}, status=status.HTTP_400_BAD_REQUEST) 


       
# p = ProductApi(title='car ', description= 'heheh', price= 22)
# p.save()
# pd = ProductDetails(product= p)
# print(pd)
# pd.save()


    


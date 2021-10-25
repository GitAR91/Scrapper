from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import status


class Parser(APIView):

    def get(self, request, part_number):
        result = list()
        url = settings.PARSING_URL + part_number
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            names = soup.findAll('span', {'class': 'listing-final-manufacturer'})
            part_numbers = soup.findAll('span', {'class': 'listing-final-partnumber'})
            prices = soup.findAll('span', {'class': 'ra-formatted-amount listing-price listing-amount-bold'})

            for i in range(len(names)):
                result.append(
                    {
                        'name': f'{names[i].contents[0]} {part_numbers[i].contents[0]}',
                        'price': prices[i].contents[0].contents[0]
                    }
                )
        except Exception as ex:
            return Response(data=result, status=status.HTTP_404_NOT_FOUND)

        if len(result) < 1:
            return Response(data=result, status=status.HTTP_404_NOT_FOUND)

        return Response(data=result, status=status.HTTP_200_OK)


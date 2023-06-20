import csv
from csv import DictReader
from django.core.management import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data data.csv"

    def handle(self, *args, **options):
        with open('data.csv', encoding='utf-8', newline='') as f:
            phone_data = csv.DictReader(f, delimiter=";")
            for row in phone_data:
                list = Phone(id=row['id'], name=row['name'], image=row['image'], price=row['price'],
                             release_date=row['release_date'], lte_exists=row['lte_exists'])
                list.save()
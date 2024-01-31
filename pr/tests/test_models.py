import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from pr.models import Club

@pytest.mark.django_db
def test_create_club():
    club_data = {
        'name': 'Vipers',
        'city': 'Kampala',
        'country': 'Uganda',
        'logo': SimpleUploadedFile("test_logo.jpg", b"file_content", content_type="image/jpeg"),
        'field_name': 'Nakivubo',
        'field_value_of_fans': 1000,
        'league_name': 'Startimes',
    }
    club = Club.objects.create(**club_data)

    assert club.name == 'Vipers'
    assert club.city == 'Kampala'
    assert club.country == 'Uganda'
    assert club.field_name == 'Nakivubo'
    assert club.field_value_of_fans == 1000
    assert club.league_name =='Startimes'


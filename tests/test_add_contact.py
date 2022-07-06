import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    # app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.сreate_new_contact(Contact(
        firstname="Name",
        middlename="Second",
        lastname="Last",
        nickname="Test",
        title="Test_Title",
        company="Test",
        home_number="1234567",
        mobile_number="1234567",
        work_number="1234567",
        fax="1234567",
        email="Test1@mail.com", email2="Test2@mail.com", email3="Test3@mail.com",
        homepage="Test.com",
        bday="16", bmonth="June", byear="2000",
        aday="21", amonth="September", ayear="1997",
        address2="None", phone2="None",
        notes="Best test"))
    app.rerturn_to_homepage()
    app.session.logout()




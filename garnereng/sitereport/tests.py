from django.test import TestCase
from datetime import datetime

from .models import *

# Models testing
class UsStateTestCase(TestCase):
    """UsState model tests"""

    def setUp(self):
        UsState.objects.create(state="Alabama", symbol="AL")

    def test_usstate_str(self):
        alabama = UsState.objects.get(state="Alabama")
        self.assertEqual(alabama.__str__(), "Alabama")


class RoleTestCase(TestCase):
    """Role model tests"""

    def setUp(self):
        Role.objects.create(label="Admin")

    def test_role_str(self):
        admin = Role.objects.get(label="Admin")
        self.assertEqual(admin.__str__(), "Admin")


class PersonTestCase(TestCase):
    """Person model tests"""

    def setUp(self):
        Person.objects.create(first="Foo", last="Bar")
        
    def test_person_str(self):
        foo = Person.objects.get(first="Foo")
        self.assertEqual(foo.__str__(), "Foo Bar")


class ClientTestCase(TestCase):
    """Client model tests"""

    def setUp(self):
        Client.objects.create(name="Baz")

    def test_client_str(self):
        baz = Client.objects.get(name="Baz")
        self.assertEqual(baz.__str__(), "Baz")


class ContractorTestCase(TestCase):
    """Contractor model tests"""

    def setUp(self):
        Contractor.objects.create(name="Foo")

    def test_contractor_str(self):
        foo = Contractor.objects.get(name="Foo")
        self.assertEqual(foo.__str__(), "Foo")


class PhaseTestCase(TestCase):
    """Phase model tests"""

    def setUp(self):
        Phase.objects.create(label="Bar")

    def test_phase_str(self):
        bar = Phase.objects.get(label="Bar")
        self.assertEqual(bar.__str__(), "Bar")


class StatusTestCase(TestCase):
    """Status model tests"""

    def setUp(self):
        Status.objects.create(label="Baz")

    def test_status_str(self):
        baz = Status.objects.get(label="Baz")
        self.assertEqual(baz.__str__(), "Baz")


class DamTypeTestCase(TestCase):
    """DamType model tests"""

    def setUp(self):
        DamType.objects.create(label="Foo")

    def test_damtype_str(self):
        foo = DamType.objects.get(label="Foo")
        self.assertEqual(foo.__str__(), "Foo")


class SpillwayTypeTestCase(TestCase):
    """SpillwayType model tests"""

    def setUp(self):
        SpillwayType.objects.create(label="Bar")

    def test_spillwaytype_str(self):
        bar = SpillwayType.objects.get(label="Bar")
        self.assertEqual(bar.__str__(), "Bar")


class TestTypeTestCase(TestCase):
    """TestType model tests"""

    def setUp(self):
        TestType.objects.create(label="Baz")

    def test_testtype_str(self):
        baz = TestType.objects.get(label="Baz")
        self.assertEqual(baz.__str__(), "Baz")


class ProjectTestCase(TestCase):
    """Project model tests"""

    def setUp(self):
        Client.objects.create(name="Foo Client")
        Project.objects.create(name="Bar Dam",
                client=Client.objects.get(name="Foo Client"))

    def test_project_str(self):
        bar = Project.objects.get(name="Bar Dam")
        self.assertEqual(bar.__str__(), "Bar Dam")


class SiteTestCase(TestCase):
    """Site model tests"""

    def setUp(self):
        UsState.objects.create(state="Alabama", symbol="AL")
        Client.objects.create(name="Foo Client")
        Project.objects.create(name="Bar Dam",
                client=Client.objects.get(name="Foo Client"))
        Site.objects.create(name="Baz Site",
                project=Project.objects.get(name="Bar Dam"),
                street="111 Anywhere Lane",
                city="Anywhere",
                state=UsState.objects.get(state="Alabama"),
                zip_code="11111")

    def test_project_str(self):
        baz = Site.objects.get(name="Baz Site")
        self.assertEqual(baz.__str__(), "Baz Site")


class ReportTestCase(TestCase):
    """Report model tests"""

    def setUp(self):
        UsState.objects.create(state="Alabama", symbol="AL")
        Client.objects.create(name="Foo Client")
        Project.objects.create(name="Bar Dam",
                client=Client.objects.get(name="Foo Client"))
        Site.objects.create(name="Baz Site",
                project=Project.objects.get(name="Bar Dam"),
                street="111 Anywhere Lane",
                city="Anywhere",
                state=UsState.objects.get(state="Alabama"),
                zip_code="11111")
        Report.objects.create(site=Site.objects.get(name="Baz Site"),
                date=datetime(1970, 1, 1))

    def test_report_str(self):
        report = Report.objects.get(date=datetime(1970, 1, 1))
        self.assertEqual(report.__str__(), "1970-01-01")

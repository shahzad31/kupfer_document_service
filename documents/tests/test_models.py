# -*- coding: utf-8 -*-
from datetime import datetime
import uuid

from django.core.exceptions import ValidationError
from django.test import TestCase
import pytz

from ..models import Document


class DocumentTest(TestCase):
    def test_document_save_required_fields(self):
        file_name = "Test File 1.jpg"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_all_fields(self):
        file_name = "Test File 1.jpg"
        file_description = "Test File 1"

        document = Document.objects.create(
            file_name=file_name,
            file_description=file_description,
            file_type='jpg',
            upload_date=datetime(2018, 1, 1, 12, 30, tzinfo=pytz.UTC),
            organization_uuid="TestUUID",
            workflowlevel1_uuids=['TestWF1UUID'],
            workflowlevel2_uuids=['TestWF2UUID'],
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)
        self.assertEqual(document_db.file_description, file_description)
        self.assertEqual(document_db.organization_uuid, 'TestUUID')
        self.assertEqual(document_db.workflowlevel1_uuids, ['TestWF1UUID'])
        self.assertEqual(document_db.workflowlevel2_uuids, ['TestWF2UUID'])

    def test_document_save_fails_missing_filename(self):
        document = Document(
            file_type='jpg',
            upload_date=datetime(2018, 1, 1, 12, 30, tzinfo=pytz.UTC),
            organization_uuid="TestUUID",
            workflowlevel1_uuids=['TestWF1UUID'],
            workflowlevel2_uuids=['TestWF2UUID'],
        )

        self.assertRaises(ValidationError, document.save)

    def test_document_save_fails_wrong_file_type(self):
        document = Document(
            file_name='file1.x',
            file_type='x',
            upload_date=datetime(2018, 1, 1, 12, 30, tzinfo=pytz.UTC),
            organization_uuid="TestUUID",
            workflowlevel1_uuids=['TestWF1UUID'],
            workflowlevel2_uuids=['TestWF2UUID'],
        )

        self.assertRaises(ValidationError, document.save)

    def test_document_save_fails_wrong_file_type2(self):
        document = Document(
            file_name='file1.x',
            file_type='png',
            upload_date=datetime(2018, 1, 1, 12, 30, tzinfo=pytz.UTC),
            organization_uuid="TestUUID",
            workflowlevel1_uuids=['TestWF1UUID'],
            workflowlevel2_uuids=['TestWF2UUID'],
        )

        self.assertRaises(ValidationError, document.save)

    def test_document_save_fails_wrong_date_format(self):
        document = Document(
            file_name='file2.jpg',
            file_type='jpg',
            upload_date='2018.5.5',
        )

        self.assertRaises(ValidationError, document.save)

    def test_document_save_file_type_jpg(self):
        file_name = "Test File 1.jpg"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_jpeg(self):
        file_name = "Test File 1.jpeg"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_png(self):
        file_name = "Test File 1.png"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_gif(self):
        file_name = "Test File 1.gif"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_pdf(self):
        file_name = "Test File 1.pdf"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_txt(self):
        file_name = "Test File 1.txt"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_doc(self):
        file_name = "Test File 1.doc"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_docx(self):
        file_name = "Test File 1.docx"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_xls(self):
        file_name = "Test File 1.xls"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_xlsx(self):
        file_name = "Test File 1.xlsx"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_ppt(self):
        file_name = "Test File 1.ppt"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)

    def test_document_save_file_type_pptx(self):
        file_name = "Test File 1.pptx"

        document = Document.objects.create(
            file_name=file_name,
            workflowlevel1_uuids=[str(uuid.uuid4())]
        )

        document_db = Document.objects.get(pk=document.pk)
        self.assertEqual(document_db.file_name, file_name)
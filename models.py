# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    title_tr = models.TextField()
    title_en = models.TextField()
    context_tr = models.TextField()
    context_en = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements'


class AtaChapters(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    parent_id = models.BigIntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ata_chapters'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    parent_id = models.BigIntegerField()
    is_active = models.IntegerField()
    level = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryProduct(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_product'


class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class Companies(models.Model):
    id = models.BigAutoField(primary_key=True)
    establishment_year = models.IntegerField()
    tax_number = models.CharField(max_length=191)
    tax_name = models.CharField(max_length=191)
    website = models.CharField(max_length=191)
    phone = models.CharField(max_length=191)
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    city = models.ForeignKey(Cities, models.DO_NOTHING)
    address = models.TextField()
    email = models.CharField(max_length=191)
    logo = models.CharField(max_length=191, blank=True, null=True)
    duns_number = models.CharField(max_length=191, blank=True, null=True)
    verified = models.IntegerField()
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    company_type = models.ForeignKey('CompanyTypes', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class CompanyDocumentTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_document_types'


class CompanyDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    get_date = models.CharField(max_length=191)
    path = models.CharField(max_length=191)
    valid_date = models.CharField(max_length=191)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    company_document_type = models.ForeignKey(CompanyDocumentTypes, models.DO_NOTHING)
    verified = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_documents'


class CompanyInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_information'


class CompanyNace(models.Model):
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    nace = models.ForeignKey('Naces', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_nace'


class CompanyTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_en = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_types'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=255, blank=True, null=True)
    phonecode = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FavoriteProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorite_products'


class FsgCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    parent_id = models.BigIntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fsg_codes'


class GtipCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    parent_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gtip_codes'


class Invites(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=191)
    token = models.CharField(unique=True, max_length=16)
    private_key = models.CharField(unique=True, max_length=191)
    encrypt_company = models.TextField()
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invites'


class Languages(models.Model):
    id = models.BigAutoField(primary_key=True)
    short_name = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name_tr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'languages'


class MessageContents(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    message_subject = models.ForeignKey('MessageSubjects', models.DO_NOTHING)
    message = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_contents'


class MessageSubjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_from = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_from')
    company_to = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_to')
    subject = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_subjects'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Naces(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'naces'


class Napcs(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'napcs'


class NatoStocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    parent_id = models.BigIntegerField()
    is_active = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nato_stocks'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title_en = models.CharField(max_length=191)
    title_tr = models.CharField(max_length=191)
    context_en = models.TextField()
    context_tr = models.TextField()
    image = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    news_hit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    max_product = models.IntegerField()
    max_photo = models.IntegerField()
    max_user = models.IntegerField()
    price = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class ProductDocumentSources(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_document_sources'


class ProductDocumentTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_document_source = models.ForeignKey(ProductDocumentSources, models.DO_NOTHING)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_document_types'


class ProductDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    get_date = models.CharField(max_length=191)
    valid_date = models.CharField(max_length=191)
    product_document_type = models.ForeignKey(ProductDocumentTypes, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    verified = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_documents'


class ProductImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=191)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_images'


class ProductInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    text = models.TextField()
    language = models.ForeignKey(Languages, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_information'


class ProductProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    value = models.CharField(max_length=191)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    language = models.ForeignKey(Languages, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_properties'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    nato_stock = models.ForeignKey(NatoStocks, models.DO_NOTHING, blank=True, null=True)
    fsg_code = models.ForeignKey(FsgCodes, models.DO_NOTHING, blank=True, null=True)
    ata_chapter = models.ForeignKey(AtaChapters, models.DO_NOTHING, blank=True, null=True)
    napc = models.ForeignKey(Napcs, models.DO_NOTHING, blank=True, null=True)
    gtip_code = models.ForeignKey(GtipCodes, models.DO_NOTHING, blank=True, null=True)
    is_active = models.IntegerField()
    verified = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    us97 = models.ForeignKey('Us97S', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class ShowCompanies(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    seen = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'show_companies'


class ShownProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    seen = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shown_products'


class Us97S(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=191)
    name_tr = models.CharField(max_length=191)
    name_en = models.CharField(max_length=191)
    parent_id = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'us97s'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    surname = models.CharField(max_length=191)
    phone = models.CharField(max_length=191)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=191)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=191)
    language = models.ForeignKey(Languages, models.DO_NOTHING)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

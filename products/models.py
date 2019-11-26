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

    def __str__(self):
        return self.code


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

    def __str__(self):
        return self.code


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

    def __str__(self):
        return self.code


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

    def __str__(self):
        return self.code


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

    def __str__(self):
        return self.code


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

    def __str__(self):
        return self.name_tr


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

    def __str__(self):
        return self.name_tr


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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


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

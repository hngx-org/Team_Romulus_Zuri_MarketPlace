# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AboutDetail(models.Model):
    bio = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about_detail'


class Activity(models.Model):
    action = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activity'


class Answer(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING, blank=True, null=True)
    options = models.TextField(blank=True, null=True)  # This field type is a guess.
    correct_option = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class Assessment(models.Model):
    skill = models.ForeignKey('Skill', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assessment'


class AssessmentCategory(models.Model):
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING, blank=True, null=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_category'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Award(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    presented_by = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'award'


class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Certificate(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate'


class Complaint(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    complaint_text = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=225, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complaint'


class ComplaintComment(models.Model):
    complaint = models.ForeignKey(Complaint, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complaint_comment'


class Coupon(models.Model):
    merchant = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING, blank=True, null=True)
    coupon_limit = models.IntegerField(blank=True, null=True)
    percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coupon_code = models.CharField(max_length=20, blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'


class CustomField(models.Model):
    field_type = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(max_length=255, blank=True, null=True)
    custom_section = models.ForeignKey('CustomUserSection', models.DO_NOTHING, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_field'


class CustomUserSection(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_user_section'


class Degree(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'degree'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class EducationDetail(models.Model):
    degree = models.ForeignKey(Degree, models.DO_NOTHING, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    field_from = models.CharField(max_length=255, db_column='\n  from', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    description = models.TextField(blank=True, null=True)
    to = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_detail'


class EmailVerification(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.DateTimeField()
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_verification'


class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)


    class Meta:
        """defines the metadata for the product model"""
        db_table = "favorites"
        managed = False
        verbose_name_plural = "Favorites"


class Images(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class InterestDetail(models.Model):
    interest = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interest_detail'


class LastViewedProduct(models.Model):
    class LastViewedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=225)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "last_viewed_product"
        managed = False
        verbose_name_plural = "LastViewedProducts"

    def __str__(self) -> str:
        return self.name

class MailLog(models.Model):
    email = models.CharField(max_length=225, blank=True, null=True)
    message_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    message_type = models.ForeignKey('MailType', models.DO_NOTHING, blank=True, null=True)
    stdefaultatus = models.TextField(db_column='stDEFAULTatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    request_origin = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_log'


class MailType(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_type'


class NotificationConfirmation(models.Model):
    mail_id = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'notification_confirmation'


class NotificationSetting(models.Model):
    email_summary = models.BooleanField(blank=True, null=True)
    special_offers = models.BooleanField(blank=True, null=True)
    community_update = models.BooleanField(blank=True, null=True)
    follow_update = models.BooleanField(blank=True, null=True)
    new_messages = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_setting'


class Order(models.Model):
    id = models.UUIDField(primary_key=True)
    customer = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    vat = models.DecimalField(db_column='VAT', max_digits=8, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    merchant = models.ForeignKey('User', models.DO_NOTHING, related_name='orderitem_merchant_set', blank=True, null=True)
    order_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_vat = models.DecimalField(db_column='order_VAT', max_digits=8, decimal_places=2)  # Field name made lowercase.
    order_discount = models.DecimalField(max_digits=8, decimal_places=2)
    promo = models.ForeignKey('Promotion', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_item'


class Permission(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permission'


class Permissions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PortfolioDetail(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portfolio_detail'


class PortfoliosAnalytics(models.Model):
    metric_amount_portfolios = models.CharField(max_length=225, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portfolios_analytics'


class Product(models.Model):
    """defines the product models"""
    ADMIN_STATUS = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('suspended', 'Suspended'),
        ('blacklisted', 'Blacklisted')
    )
    PRODUCT_STATUS = (
        ('active', 'Active'),
        ('temporary', 'Temporary')
    )
    id = models.UUIDField(primary_key=True, default=uuid4, null=False)
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    quantity = models.BigIntegerField(null=False)
    category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True)
    product_category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True)
    price = models.DecimalField( max_digits=20, decimal_places=2, null=False)
    discount_price = models.DecimalField( max_digits=20, decimal_places=2, null=False)
    tax = models.DecimalField( max_digits=20, decimal_places=2, null=False)
    admin_status = models.CharField(max_length=20, choices=ADMIN_STATUS, default="pending")
    is_deleted = models.CharField(max_length=20, choices=PRODUCT_STATUS, default="active")
    image_id = models.ForeignKey('ProductImage', on_delete=models.CASCADE, null=True)
    rating_id = models.ForeignKey('UserProductRating', on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=False, null=False)
    currency = models.CharField(max_length=10, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    class Meta:
        """defines the metadata for the product model"""
        db_table = "product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=225)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        """defines the metadata for the product model"""
        db_table = "product_category"
        managed = False
        verbose_name_plural = "ProductCategories"

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        """defines the metadata for the product model"""
        db_table = "product_image"
        managed = False
        verbose_name_plural = "ProductImages"

    def __str__(self) -> str:
        return self.url

class ProductLogs(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    action = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_logs'


class ProductReview(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    reply = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_review'


class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    parent_category_id = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        """defines the metadata for the product model"""
        db_table = "product_sub_category"
        managed = False
        verbose_name_plural = "ProductSubCategories"

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectsImage(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    image = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_image'


class PromoProduct(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    promo = models.ForeignKey('Promotion', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promo_product'


class Promotion(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=255)
    promotion_type = models.CharField(max_length=255)
    discount_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.BigIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    maximum_discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotion'


class Question(models.Model):
    question_no = models.IntegerField(blank=True, null=True)
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING, blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    question_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class Report(models.Model):
    report_type = models.CharField(max_length=225, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report'


class Revenue(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'revenue'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "role"
        managed = False
        verbose_name_plural = "roles"


class RolesPermissions(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey(Permission, models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles_permissions'


class SalesAnalytics(models.Model):
    metric_amount_goods_sold = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metric_average_sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metric_overall_revenue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metric_revenue_per_category = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metric_product_popularity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metric_total_orders = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales_analytics'


class SalesReport(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    sales = models.BigIntegerField()
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales_report'


class Section(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'


class Shop(models.Model):
    """defines the shop model"""
    SHOP_STATUS = (
        ('active', 'Active'),
        ('temporary', 'Temporary')
    )
    RESTRICTED = (
        ('no', 'No'),
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent')
    )
    ADMIN_STATUS = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('suspended', 'Suspended'),
        ('blacklisted', 'Blacklisted')
    )
    id = models.UUIDField(primary_key=True, default=uuid4, null=False)
    merchant_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=False)
    policy_confirmation = models.BooleanField(default=False)
    restricted = models.CharField(max_length=20, choices=RESTRICTED, default="no")
    admin_status = models.CharField(max_length=20, choices=ADMIN_STATUS, default="pending")
    is_deleted = models.CharField(max_length=20, choices=SHOP_STATUS, default='active')
    reviewed = models.BooleanField(default=False)
    rating = models.DecimalField( max_digits=20, decimal_places=2, default=0.00)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        """defines the metadata for the shop model"""
        db_table = "shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.name

class ShopLogs(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    action = models.CharField(max_length=20, blank=True, null=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_logs'


class Skill(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent_skill = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill'


class SkillBadge(models.Model):
    skill = models.ForeignKey(Skill, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    badge_image = models.TextField(blank=True, null=True)
    min_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skill_badge'


class SkillsDetail(models.Model):
    skills = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills_detail'


class SocialMedia(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_media'


class SocialUser(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    social_media = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_user'


class StoreTraffic(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store_traffic'


class TrackPromotion(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'track_promotion'


class Tracks(models.Model):
    track = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracks'


class Transaction(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    provider_ref = models.CharField(max_length=255, blank=True, null=True)
    in_app_ref = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaction'


class User(models.Model):
    """Identifies the user model based on the schema"""
    id = models.UUIDField(primary_key=True, default=uuid4, null=False)
    username = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE)
    section_order = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    two_factor_auth = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    profile_cover_photo = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=255, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)


    class Meta:
        """defines the metadata for the product model"""
        db_table = "user"
        managed = False
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.name

class UserAnalytics(models.Model):
    metric_total_number_users = models.IntegerField(blank=True, null=True)
    metric_total_number_daily_users = models.IntegerField(blank=True, null=True)
    metric_total_number_of_user_visitation_on_product = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_analytics'


class UserAssessment(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING, blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    time_spent = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_assessment'


class UserBadge(models.Model):
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    badge = models.ForeignKey(SkillBadge, models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_badge'


class UserPermission(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey(Permission, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_permission'


class UserProductInteraction(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20)  # e.g., "viewed," "purchased"
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user_product_interaction'


class UserProductRating(models.Model):
    """This is the user product rating, how the product is rated"""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(null=True)


    class Meta:
        """defines the metadata for the product model"""
        db_table = "user_product_rating"
        managed = False
        verbose_name_plural = "UserProductRatings"

class UserResponse(models.Model):
    user_assessment = models.ForeignKey(UserAssessment, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(Question, models.DO_NOTHING, blank=True, null=True)
    answer_id = models.IntegerField(blank=True, null=True)
    selected_response = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_response'


class UserTrack(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    track = models.ForeignKey(Tracks, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_track'


class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    class Meta:
        """defines the metadata for the product model"""
        db_table = "wishlist"
        managed = False
        verbose_name_plural = "Wishlists"


class WorkExperienceDetail(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_month = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.CharField(max_length=255, blank=True, null=True)
    end_month = models.CharField(max_length=255, blank=True, null=True)
    end_year = models.CharField(max_length=255, blank=True, null=True)
    is_employee = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_experience_detail'

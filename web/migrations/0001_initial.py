# Generated by Django 2.1.1 on 2018-09-14 09:14

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(default=web.models.generate_new_pid, max_length=13, unique=True, verbose_name='شناسه\u200cی عمومی')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('subtitle', models.CharField(blank=True, default='', max_length=128, verbose_name='زیرعنوان')),
                ('content', models.TextField(max_length=1024, verbose_name='محتوا')),
                ('event', models.CharField(blank=True, default='', help_text='تاریخ یک رویداد مهم برای موضوع وارد شده به همراه محل وقوع.', max_length=128, verbose_name='رویداد مهم')),
                ('image', models.ImageField(blank=True, default='', upload_to='images', verbose_name='تصویر')),
                ('image_caption', models.CharField(blank=True, default='', help_text='مکان و موقعیت گرفتن عکس به همراه معرفی افراد حاضر در عکس.', max_length=128, verbose_name='توضیح تصویر')),
                ('reference', models.CharField(blank=True, default='', help_text='نام کتاب، روزنامه، مجله یا آدرس سایت، بلاگ و... به همراه نام نویسنده', max_length=128, verbose_name='منبع')),
                ('website', models.EmailField(blank=True, default='', max_length=254, verbose_name='وب\u200cسایت')),
                ('author', models.EmailField(blank=True, default='', max_length=254, verbose_name='ایمیل نویسنده')),
                ('is_active', models.BooleanField(default=False, help_text='مشخص می\u200cکند که این صفحه در لیست نتایج قابل دیدن باشد یا نه.', verbose_name='فعال')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'صفحه',
                'verbose_name_plural': 'صفحه\u200cها',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1024, verbose_name='متن گزارش')),
                ('reporter', models.EmailField(max_length=254, verbose_name='ایمیل گزارش\u200cدهنده')),
                ('status', models.CharField(choices=[('pending', 'در انتظار'), ('processed', 'رسیدگی شده'), ('denied', 'رد شده')], default='pending', max_length=32, verbose_name='وضعیت رسیدگی')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Data', to_field='pid', verbose_name='صفحه')),
            ],
            options={
                'verbose_name': 'گزارش',
                'verbose_name_plural': 'گزارش\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='نام')),
                ('keyword', models.CharField(max_length=128, verbose_name='کلیدواژه')),
                ('is_active', models.BooleanField(default=True, help_text='مشخص می\u200cکند که این برچسب قابل استفاده باشد یا نه.', verbose_name='فعال')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب\u200cها',
            },
        ),
        migrations.AddField(
            model_name='data',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', related_query_name='tag', to='web.Tag', verbose_name='برچسب\u200cها'),
        ),
    ]

# Generated by Django 2.2 on 2021-08-05 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ra.base.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date and time')),
                ('lastmod', models.DateTimeField(db_index=True, verbose_name='last modification')),
                ('slug', models.SlugField(blank=True, help_text='For fast recall', unique=True, verbose_name='Identifier slug')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=512, null=True)),
                ('longitude', models.CharField(blank=True, max_length=512, null=True)),
                ('year_established', models.DateField(blank=True, null=True)),
                ('total_employees', models.CharField(blank=True, max_length=255, null=True)),
                ('business_type', models.CharField(blank=True, max_length=255, null=True)),
                ('main_products', models.CharField(blank=True, max_length=255, null=True)),
                ('total_annual_revenue', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('social_link', models.CharField(blank=True, max_length=255, null=True)),
                ('lastmod_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utility_company_lastmod_related', to=settings.AUTH_USER_MODEL, verbose_name='last modification by')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utility_company_related', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'abstract': False,
            },
            bases=(ra.base.models.DiffingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ScheduleBaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('time_from', models.TimeField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('time_to', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskUnitsPointsBaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_units_task', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('unit_task_description', models.TextField(blank=True, null=True)),
                ('points_on_unit_task', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat', models.FloatField(blank=True, null=True, verbose_name='Vat(%)')),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VatBusinessType', to='utility.BusinessType')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date and time')),
                ('lastmod', models.DateTimeField(db_index=True, verbose_name='last modification')),
                ('slug', models.SlugField(blank=True, help_text='For fast recall', unique=True, verbose_name='Identifier slug')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=32)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('nationalid', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True)),
                ('name_spouse', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=512, null=True)),
                ('longitude', models.CharField(blank=True, max_length=512, null=True)),
                ('lastmod_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utility_userprofile_lastmod_related', to=settings.AUTH_USER_MODEL, verbose_name='last modification by')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utility_userprofile_related', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'abstract': False,
            },
            bases=(ra.base.models.DiffingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.FloatField(blank=True, null=True, verbose_name='Tax(%)')),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TaxBusinessType', to='utility.BusinessType')),
            ],
        ),
        migrations.CreateModel(
            name='PredfinedPointsRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('units_points', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('task_description', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predfinedpointsrule_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predfinedpointsrule_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=512, null=True)),
                ('longitude', models.CharField(blank=True, max_length=512, null=True)),
                ('year_established', models.DateField(blank=True, null=True)),
                ('total_employees', models.CharField(blank=True, max_length=255, null=True)),
                ('business_type', models.CharField(blank=True, max_length=255, null=True)),
                ('main_products', models.CharField(blank=True, max_length=255, null=True)),
                ('total_annual_revenue', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('social_link', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.Company')),
            ],
        ),
    ]

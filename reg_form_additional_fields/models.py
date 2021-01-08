from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains the extra field "Country" that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, related_name='user+', on_delete=models.CASCADE)

    COUNTRIES = (
        ('TWN', 'Taiwan'),
        ('AFG', 'Afghanistan'),
        ('ALB', 'Albania'),
        ('DZA', 'Algeria'),
        ('ASM', 'American Samoa'),
        ('AND', 'Andorra'),
        ('AGO', 'Angola'),
        ('AIA', 'Anguilla'),
        ('ATA', 'Antarctica'),
        ('ATG', 'Antigua & Barbuda'),
        ('ARG', 'Argentina'),
        ('ARM', 'Armenia'),
        ('ABW', 'Aruba'),
        ('AUS', 'Australia'),
        ('AUT', 'Austria'),
        ('AZE', 'Azerbaijan'),
        ('BHS', 'Bahamas'),
        ('BHR', 'Bahrain'),
        ('BGD', 'Bangladesh'),
        ('BRB', 'Barbados'),
        ('BLR', 'Belarus'),
        ('BEL', 'Belgium'),
        ('BLZ', 'Belize'),
        ('BEN', 'Benin'),
        ('BMU', 'Bermuda'),
        ('BTN', 'Bhutan'),
        ('BOL', 'Bolivia'),
        ('BES', 'Caribbean Netherlands'),
        ('BIH', 'Bosnia'),
        ('BWA', 'Botswana'),
        ('BVT', 'Bouvet Island'),
        ('BRA', 'Brazil'),
        ('IOT', 'British Indian Ocean Territory'),
        ('VGB', 'British Virgin Islands'),
        ('BRN', 'Brunei'),
        ('BGR', 'Bulgaria'),
        ('BFA', 'Burkina Faso'),
        ('BDI', 'Burundi'),
        ('CPV', 'Cape Verde'),
        ('KHM', 'Cambodia'),
        ('CMR', 'Cameroon'),
        ('CAN', 'Canada'),
        ('CYM', 'Cayman Islands'),
        ('CAF', 'Central African Republic'),
        ('TCD', 'Chad'),
        ('CHL', 'Chile'),
        ('CHN', 'China'),
        ('HKG', 'Hong Kong'),
        ('MAC', 'Macau'),
        ('CXR', 'Christmas Island'),
        ('CCK', 'Cocos (Keeling) Islands'),
        ('COL', 'Colombia'),
        ('COM', 'Comoros'),
        ('COG', 'Congo - Brazzaville'),
        ('COK', 'Cook Islands'),
        ('CRI', 'Costa Rica'),
        ('HRV', 'Croatia'),
        ('CUB', 'Cuba'),
        ('CUW', 'Curaçao'),
        ('CYP', 'Cyprus'),
        ('CZE', 'Czechia'),
        ('CIV', 'Côte d’Ivoire'),
        ('PRK', 'North Korea'),
        ('COD', 'Congo - Kinshasa'),
        ('DNK', 'Denmark'),
        ('DJI', 'Djibouti'),
        ('DMA', 'Dominica'),
        ('DOM', 'Dominican Republic'),
        ('ECU', 'Ecuador'),
        ('EGY', 'Egypt'),
        ('SLV', 'El Salvador'),
        ('GNQ', 'Equatorial Guinea'),
        ('ERI', 'Eritrea'),
        ('EST', 'Estonia'),
        ('SWZ', 'Eswatini'),
        ('ETH', 'Ethiopia'),
        ('FLK', 'Falkland Islands'),
        ('FRO', 'Faroe Islands'),
        ('FJI', 'Fiji'),
        ('FIN', 'Finland'),
        ('FRA', 'France'),
        ('GUF', 'French Guiana'),
        ('PYF', 'French Polynesia'),
        ('ATF', 'French Southern Territories'),
        ('GAB', 'Gabon'),
        ('GMB', 'Gambia'),
        ('GEO', 'Georgia'),
        ('DEU', 'Germany'),
        ('GHA', 'Ghana'),
        ('GIB', 'Gibraltar'),
        ('GRC', 'Greece'),
        ('GRL', 'Greenland'),
        ('GRD', 'Grenada'),
        ('GLP', 'Guadeloupe'),
        ('GUM', 'Guam'),
        ('GTM', 'Guatemala'),
        ('GGY', 'Guernsey'),
        ('GIN', 'Guinea'),
        ('GNB', 'Guinea-Bissau'),
        ('GUY', 'Guyana'),
        ('HTI', 'Haiti'),
        ('HMD', 'Heard & McDonald Islands'),
        ('VAT', 'Vatican City'),
        ('HND', 'Honduras'),
        ('HUN', 'Hungary'),
        ('ISL', 'Iceland'),
        ('IND', 'India'),
        ('IDN', 'Indonesia'),
        ('IRN', 'Iran'),
        ('IRQ', 'Iraq'),
        ('IRL', 'Ireland'),
        ('IMN', 'Isle of Man'),
        ('ISR', 'Israel'),
        ('ITA', 'Italy'),
        ('JAM', 'Jamaica'),
        ('JPN', 'Japan'),
        ('JEY', 'Jersey'),
        ('JOR', 'Jordan'),
        ('KAZ', 'Kazakhstan'),
        ('KEN', 'Kenya'),
        ('KIR', 'Kiribati'),
        ('KWT', 'Kuwait'),
        ('KGZ', 'Kyrgyzstan'),
        ('LAO', 'Laos'),
        ('LVA', 'Latvia'),
        ('LBN', 'Lebanon'),
        ('LSO', 'Lesotho'),
        ('LBR', 'Liberia'),
        ('LBY', 'Libya'),
        ('LIE', 'Liechtenstein'),
        ('LTU', 'Lithuania'),
        ('LUX', 'Luxembourg'),
        ('MDG', 'Madagascar'),
        ('MWI', 'Malawi'),
        ('MYS', 'Malaysia'),
        ('MDV', 'Maldives'),
        ('MLI', 'Mali'),
        ('MLT', 'Malta'),
        ('MHL', 'Marshall Islands'),
        ('MTQ', 'Martinique'),
        ('MRT', 'Mauritania'),
        ('MUS', 'Mauritius'),
        ('MYT', 'Mayotte'),
        ('MEX', 'Mexico'),
        ('FSM', 'Micronesia'),
        ('MCO', 'Monaco'),
        ('MNG', 'Mongolia'),
        ('MNE', 'Montenegro'),
        ('MSR', 'Montserrat'),
        ('MAR', 'Morocco'),
        ('MOZ', 'Mozambique'),
        ('MMR', 'Myanmar'),
        ('NAM', 'Namibia'),
        ('NRU', 'Nauru'),
        ('NPL', 'Nepal'),
        ('NLD', 'Netherlands'),
        ('NCL', 'New Caledonia'),
        ('NZL', 'New Zealand'),
        ('NIC', 'Nicaragua'),
        ('NER', 'Niger'),
        ('NGA', 'Nigeria'),
        ('NIU', 'Niue'),
        ('NFK', 'Norfolk Island'),
        ('MNP', 'Northern Mariana Islands'),
        ('NOR', 'Norway'),
        ('OMN', 'Oman'),
        ('PAK', 'Pakistan'),
        ('PLW', 'Palau'),
        ('PAN', 'Panama'),
        ('PNG', 'Papua New Guinea'),
        ('PRY', 'Paraguay'),
        ('PER', 'Peru'),
        ('PHL', 'Philippines'),
        ('PCN', 'Pitcairn Islands'),
        ('POL', 'Poland'),
        ('PRT', 'Portugal'),
        ('PRI', 'Puerto Rico'),
        ('QAT', 'Qatar'),
        ('KOR', 'South Korea'),
        ('MDA', 'Moldova'),
        ('ROU', 'Romania'),
        ('RUS', 'Russia'),
        ('RWA', 'Rwanda'),
        ('REU', 'Réunion'),
        ('BLM', 'St. Barthélemy'),
        ('SHN', 'St. Helena'),
        ('KNA', 'St. Kitts & Nevis'),
        ('LCA', 'St. Lucia'),
        ('MAF', 'St. Martin'),
        ('SPM', 'St. Pierre & Miquelon'),
        ('VCT', 'St. Vincent & Grenadines'),
        ('WSM', 'Samoa'),
        ('SMR', 'San Marino'),
        ('STP', 'São Tomé & Príncipe'),
        ('SAU', 'Saudi Arabia'),
        ('SEN', 'Senegal'),
        ('SRB', 'Serbia'),
        ('SYC', 'Seychelles'),
        ('SLE', 'Sierra Leone'),
        ('SGP', 'Singapore'),
        ('SXM', 'Sint Maarten'),
        ('SVK', 'Slovakia'),
        ('SVN', 'Slovenia'),
        ('SLB', 'Solomon Islands'),
        ('SOM', 'Somalia'),
        ('ZAF', 'South Africa'),
        ('SGS', 'South Georgia & South Sandwich Islands'),
        ('SSD', 'South Sudan'),
        ('ESP', 'Spain'),
        ('LKA', 'Sri Lanka'),
        ('PSE', 'Palestine'),
        ('SDN', 'Sudan'),
        ('SUR', 'Suriname'),
        ('SJM', 'Svalbard & Jan Mayen'),
        ('SWE', 'Sweden'),
        ('CHE', 'Switzerland'),
        ('SYR', 'Syria'),
        ('TJK', 'Tajikistan'),
        ('THA', 'Thailand'),
        ('MKD', 'North Macedonia'),
        ('TLS', 'Timor-Leste'),
        ('TGO', 'Togo'),
        ('TKL', 'Tokelau'),
        ('TON', 'Tonga'),
        ('TTO', 'Trinidad & Tobago'),
        ('TUN', 'Tunisia'),
        ('TUR', 'Turkey'),
        ('TKM', 'Turkmenistan'),
        ('TCA', 'Turks & Caicos Islands'),
        ('TUV', 'Tuvalu'),
        ('UGA', 'Uganda'),
        ('UKR', 'Ukraine'),
        ('ARE', 'United Arab Emirates'),
        ('GBR', 'UK'),
        ('TZA', 'Tanzania'),
        ('UMI', 'U.S. Outlying Islands'),
        ('VIR', 'U.S. Virgin Islands'),
        ('USA', 'US'),
        ('URY', 'Uruguay'),
        ('UZB', 'Uzbekistan'),
        ('VUT', 'Vanuatu'),
        ('VEN', 'Venezuela'),
        ('VNM', 'Vietnam'),
        ('WLF', 'Wallis & Futuna'),
        ('ESH', 'Western Sahara'),
        ('YEM', 'Yemen'),
        ('ZMB', 'Zambia'),
        ('ZWE', 'Zimbabwe'),
        ('ALA', 'Åland Islands')
    )

    country = models.CharField(
        verbose_name="Country",
        choices=COUNTRIES,
        blank=True,
        max_length=5,
    )

    def __str__(self):
        result = '{0.user} {0.country}'
        return result.format(self)
